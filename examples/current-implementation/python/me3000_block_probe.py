import socket, struct, time

IP="STORAGE_INVERTER_IP"
PORT=8899
SLAVE=1

def crc16(data):
    crc=0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return struct.pack("<H", crc)

def read(func, addr, count=8):
    frame=bytes([SLAVE,func,addr>>8,addr&255,count>>8,count&255])
    frame += crc16(frame)
    try:
        with socket.create_connection((IP,PORT), timeout=0.5) as s:
            s.settimeout(0.5)
            s.sendall(frame)
            data=s.recv(256)
    except Exception:
        return

    if len(data) >= 5:
        print(f"func={func} addr={addr:#06x} -> {data.hex(' ')}")

for func in [3,4]:
    for addr in [
        0x0000,0x0100,0x0200,0x0300,0x0400,0x0500,0x0600,0x0700,
        0x0800,0x0900,0x0a00,0x0b00,0x0c00,0x0d00,0x0e00,0x0f00,
        0x1000,0x1100,0x1200,0x1300,0x1400,0x1500,0x1600,0x1700,
        0x1800,0x1900,0x1a00,0x1b00,0x1c00,0x1d00,0x1e00,0x1f00,
        0x2000,0x2100,0x2200,0x3000,0x4000
    ]:
        read(func, addr)
        time.sleep(0.05)
