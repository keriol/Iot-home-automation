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

def read(func, addr, count=10):
    frame=bytes([SLAVE,func,addr>>8,addr&255,count>>8,count&255])
    frame += crc16(frame)

    with socket.create_connection((IP,PORT), timeout=1) as s:
        s.settimeout(1)
        s.sendall(frame)
        data=s.recv(512)

    if len(data) < 5 or data[0] != SLAVE:
        return None

    if data[1] == (func | 0x80):
        return None

    if data[1] != func:
        return None

    bc=data[2]
    payload=data[3:3+bc]
    return [int.from_bytes(payload[i:i+2],"big") for i in range(0,len(payload),2)]

tests = [
    (3, 0x0200), (3, 0x0210), (3, 0x0220), (3, 0x0230),
    (3, 0x0300), (3, 0x0310), (3, 0x0320),
    (3, 0x0400), (3, 0x0410), (3, 0x0420),
    (4, 0x1000), (4, 0x1010), (4, 0x1020), (4, 0x1030),
    (4, 0x2000),
]

for func, addr in tests:
    try:
        regs = read(func, addr, 10)
        if regs:
            print(f"\nfunc={func} addr={addr:#06x}")
            for i,v in enumerate(regs):
                print(f"{addr+i:#06x} / {addr+i:05d}: {v}")
    except Exception as e:
        print(f"ERR func={func} addr={addr:#06x}: {e}")
    time.sleep(0.1)
