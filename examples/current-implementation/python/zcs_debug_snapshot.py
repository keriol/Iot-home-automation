import socket, struct

DEVICES = {
    "pv_2200tl": "PV_INVERTER_IP",
    "me3000sp": "STORAGE_INVERTER_IP",
}

PORT = 8899
SLAVE = 1

WATCH = {
    "pv_2200tl": {
        "grid_voltage": (3, 0x000F, 0.1),
        "grid_frequency": (3, 0x000E, 0.01),
        "temperature": (3, 0x0010, 0.1),
        "dc_current_1_candidate": (3, 0x001B, 0.1),
        "dc_current_2_candidate": (3, 0x001C, 0.1),
        "dc_voltage_1_candidate": (3, 0x001D, 0.1),
        "dc_voltage_2_candidate": (3, 0x001E, 0.1),
        "pv_power_candidate_1": (3, 0x0020, 1),
        "pv_energy_candidate_1": (3, 0x0024, 1),
        "pv_energy_candidate_2": (3, 0x0025, 1),
        "pv_energy_candidate_3": (3, 0x0026, 1),
    },
    "me3000sp": {
        "grid_voltage": (3, 0x0206, 0.1),
        "battery_soc": (3, 0x0210, 1),
        "unknown_0212": (3, 0x0212, 1),
        "unknown_0213": (3, 0x0213, 1),
        "unknown_0215": (3, 0x0215, 1),
        "unknown_0216": (3, 0x0216, 1),
        "grid_export_candidate": (3, 0x0218, 1),
        "unknown_0219": (3, 0x0219, 1),
        "battery_voltage_candidate": (3, 0x0227, 0.01),
        "unknown_0231": (3, 0x0231, 1),
        "output_voltage": (3, 0x0230, 0.1),
    }
}

def crc16(data):
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return struct.pack("<H", crc)

def read_reg(ip, func, addr):
    frame = bytes([SLAVE, func, addr >> 8, addr & 255, 0, 1])
    frame += crc16(frame)

    with socket.create_connection((ip, PORT), timeout=1) as s:
        s.settimeout(1)
        s.sendall(frame)
        data = s.recv(64)

    if len(data) != 7:
        raise ValueError(data.hex(" "))
    if data[:3] != bytes([SLAVE, func, 2]):
        raise ValueError(data.hex(" "))
    if data[-2:] != crc16(data[:-2]):
        raise ValueError("bad crc " + data.hex(" "))

    return int.from_bytes(data[3:5], "big")

for device, ip in DEVICES.items():
    print(f"\n=== {device} {ip} ===")
    for name, (func, addr, scale) in WATCH[device].items():
        try:
            raw = read_reg(ip, func, addr)
            print(f"{name:30} addr={addr:#06x} raw={raw:<6} value={raw * scale}")
        except Exception as e:
            print(f"{name:30} addr={addr:#06x} ERR {e}")
