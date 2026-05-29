import time
import socket
import struct
import json
import paho.mqtt.client as mqtt

MQTT_HOST = "127.0.0.1"
MQTT_PORT = 1883
MQTT_USER = "zcs_poller"
MQTT_PASS = "$unP0w3r3d"

PV_IP = "PV_INVERTER_IP"        # SOFAR 2200TL
STORAGE_IP = "STORAGE_INVERTER_IP"   # SOFAR ME3000SP

PORT = 8899
SLAVE = 1
BASE_TOPIC = "home/zcs/energy"
POLL_SECONDS = 60
TIMEOUT_SECONDS = 3


def crc16(data):
    crc = 0xFFFF

    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1

    return struct.pack("<H", crc)


def read_register(ip, function, address):
    frame = bytes([SLAVE, function, address >> 8, address & 0xFF, 0, 1])
    frame += crc16(frame)

    with socket.create_connection((ip, PORT), timeout=TIMEOUT_SECONDS) as s:
        s.settimeout(TIMEOUT_SECONDS)
        s.sendall(frame)
        data = s.recv(64)

    if len(data) < 7:
        raise ValueError(f"short response {ip} {address:#06x}: {data.hex(' ')}")

    body = data[:5]
    received_crc = data[5:7]

    if data[:3] != bytes([SLAVE, function, 2]):
        raise ValueError(f"bad header {ip} {address:#06x}: {data.hex(' ')}")

    if received_crc != crc16(body):
        raise ValueError(f"bad crc {ip} {address:#06x}: {data.hex(' ')}")

    return int.from_bytes(data[3:5], "big")


def publish(client, key, value):
    client.publish(f"{BASE_TOPIC}/{key}", str(value), retain=True)


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(MQTT_USER, MQTT_PASS)
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_start()

    while True:
        try:
            pv_power = read_register(PV_IP, 3, 0x000C) * 10

            battery_soc = read_register(STORAGE_IP, 3, 0x0210)
            battery_voltage = round(read_register(STORAGE_IP, 3, 0x0227) * 0.01, 2)
            grid_voltage = round(read_register(STORAGE_IP, 3, 0x0206) * 0.1, 1)
            output_voltage = round(read_register(STORAGE_IP, 3, 0x0230) * 0.1, 1)

            raw_0231 = read_register(STORAGE_IP, 3, 0x0231)
            grid_export = raw_0231 * 2

            house_consumption = max(0, pv_power - grid_export)

            debug_0216 = read_register(STORAGE_IP, 3, 0x0216)
            debug_0218 = read_register(STORAGE_IP, 3, 0x0218)

            sensors = {
                "pv_power": pv_power,
                "grid_export": grid_export,
                "house_consumption": house_consumption,
                "battery_soc": battery_soc,
                "battery_voltage": battery_voltage,
                "grid_voltage": grid_voltage,
                "output_voltage": output_voltage,
                "debug_0216": debug_0216,
                "debug_0218": debug_0218,
                "debug_0231": raw_0231,
            }

            for key, value in sensors.items():
                publish(client, key, value)

            client.publish(f"{BASE_TOPIC}/state", json.dumps(sensors), retain=True)
            print(sensors)

        except Exception as e:
            print("ERR", repr(e))
            client.publish(f"{BASE_TOPIC}/last_error", repr(e), retain=False)

        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
