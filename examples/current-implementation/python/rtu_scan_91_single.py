import socket
import struct
import time

IP = "STORAGE_INVERTER_IP"
PORT = 8899
SLAVE = 1

def crc16(data):
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return struct.pack("<H", crc)

def read_one(addr):
    frame = bytes([SLAVE, 3, addr >> 8, addr & 0xFF, 0, 1])
    frame += crc16(frame)

    with socket.create_connection((IP, PORT), timeout=2) as s:
        s.settimeout(2)
        s.sendall(frame)
        data = s.recv(64)

    if len(data) != 7:
        return None

    if data[:3] != bytes([SLAVE, 3, 2]):
        return None

    if data[-2:] != crc16(data[:-2]):
        return None

    return int.from_bytes(data[3:5], "big")

for addr in range(0, 80):
    try:
        val = read_one(addr)
        if val is not None:
            print(f"{addr:04d}: {val}")
    except Exception:
        pass
    time.sleep(0.15)
