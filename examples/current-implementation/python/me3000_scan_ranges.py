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

def query(func, addr, count=1):
    frame = bytes([SLAVE, func, addr >> 8, addr & 0xFF, count >> 8, count & 0xFF])
    frame += crc16(frame)

    try:
        with socket.create_connection((IP, PORT), timeout=0.35) as s:
            s.settimeout(0.35)
            s.sendall(frame)
            data = s.recv(128)
    except Exception:
        return None

    if not data:
        return None

    # exception response
    if len(data) == 5 and data[0] == SLAVE and data[1] == (func | 0x80):
        return f"EXC {data[2]}"

    if len(data) >= 7 and data[0] == SLAVE and data[1] == func and data[2] == 2:
        if data[-2:] != crc16(data[:-2]):
            return f"CRC_BAD {data.hex(' ')}"
        return int.from_bytes(data[3:5], "big")

    return f"RAW {data.hex(' ')}"

ranges = [
    range(0x0000, 0x0060),
    range(0x0100, 0x0180),
    range(0x0200, 0x0280),
    range(0x0300, 0x0380),
    range(0x0400, 0x0500),
    range(0x0500, 0x0600),
    range(0x0600, 0x0700),
    range(0x1000, 0x1080),
    range(0x2000, 0x2080),
]

for func in [3, 4]:
    print(f"\n========== FUNC {func} ==========")
    for rg in ranges:
        print(f"\n-- {rg.start:#06x}..{rg.stop-1:#06x} --")
        found = 0
        for addr in rg:
            res = query(func, addr)
            if isinstance(res, int):
                print(f"{addr:#06x} / {addr:04d}: {res}")
                found += 1
            time.sleep(0.02)
        if found == 0:
            print("no valid values")
