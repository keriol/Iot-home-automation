import socket
import struct
import time

def crc16(data):
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return struct.pack("<H", crc)

def read_regs(addr, count=10):
    frame = bytes([1, 3, addr >> 8, addr & 0xFF, count >> 8, count & 0xFF])
    frame += crc16(frame)

    with socket.create_connection(("PV_INVERTER_IP", 8899), timeout=1.5) as s:
        s.settimeout(1.5)
        s.sendall(frame)
        data = s.recv(1024)

    if len(data) < 5:
        return None

    byte_count = data[2]
    expected_len = 3 + byte_count + 2
    if len(data) < expected_len:
        print(f"addr={addr}: TRUNC {data.hex(' ')}")
        return None

    body = data[:3 + byte_count]
    recv_crc = data[3 + byte_count:expected_len]
    if recv_crc != crc16(body):
        print(f"addr={addr}: CRC BAD {data.hex(' ')}")
        return None

    payload = data[3:3 + byte_count]
    return [int.from_bytes(payload[i:i+2], "big") for i in range(0, len(payload), 2)]

for addr in range(0, 80):
    try:
        regs = read_regs(addr, 10)
        if regs is not None:
            print(f"{addr:04d}: {regs}")
    except Exception:
        pass
    time.sleep(0.05)
