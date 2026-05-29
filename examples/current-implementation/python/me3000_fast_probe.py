import socket
import struct

IP = "STORAGE_INVERTER_IP"
PORT = 8899

def crc16(data):
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return struct.pack("<H", crc)

def query(slave, func, addr, count=1):
    frame = bytes([slave, func, addr >> 8, addr & 0xFF, count >> 8, count & 0xFF])
    frame += crc16(frame)

    try:
        with socket.create_connection((IP, PORT), timeout=0.25) as s:
            s.settimeout(0.25)
            s.sendall(frame)
            data = s.recv(64)
            if data:
                print(f"slave={slave} func={func} addr={addr} -> {data.hex(' ')}")
    except Exception:
        pass

for func in [3, 4]:
    for addr in [0, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 5000]:
        query(1, func, addr)
