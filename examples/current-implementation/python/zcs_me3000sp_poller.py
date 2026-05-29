import json, socket, struct, time
import paho.mqtt.client as mqtt

IP = "STORAGE_INVERTER_IP"
PORT = 8899
SLAVE = 1
MQTT_HOST = "127.0.0.1"
MQTT_USER = "zcs_poller"
MQTT_PASS = "$unP0w3r3d"
BASE = "home/zcs/me3000sp"

REGISTERS = {
    "grid_voltage": (0x0206, 0.1, "V"),
    "battery_soc": (0x0210, 1, "%"),
    "house_power": (0x0216, 1, "W"),
    "grid_export_power": (0x0218, 1, "W"),
    "output_voltage": (0x0230, 0.1, "V"),
}

def crc16(data):
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return struct.pack("<H", crc)

def read_reg(addr):
    frame = bytes([SLAVE, 3, addr >> 8, addr & 255, 0, 1])
    frame += crc16(frame)

    with socket.create_connection((IP, PORT), timeout=1) as s:
        s.settimeout(1)
        s.sendall(frame)
        data = s.recv(64)

    if len(data) != 7:
        raise ValueError(f"incomplete response: {data.hex(' ')}")
    if data[:3] != bytes([SLAVE, 3, 2]):
        raise ValueError(f"bad header: {data.hex(' ')}")
    if data[-2:] != crc16(data[:-2]):
        raise ValueError(f"bad crc: {data.hex(' ')}")

    return int.from_bytes(data[3:5], "big")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.connect(MQTT_HOST, 1883, 60)
client.loop_start()

while True:
    payload = {}
    for name, (addr, scale, unit) in REGISTERS.items():
        try:
            raw = read_reg(addr)
            value = round(raw * scale, 3)
            payload[name] = value
            client.publish(f"{BASE}/{name}", value, retain=True)
            client.publish(f"{BASE}/{name}_raw", raw, retain=True)
        except Exception as e:
            client.publish(f"{BASE}/{name}_error", str(e), retain=False)

    client.publish(f"{BASE}/state", json.dumps(payload), retain=True)
    print(payload)
    time.sleep(10)
