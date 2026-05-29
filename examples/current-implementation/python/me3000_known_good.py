import socket, struct

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

def read(func, addr, count):
    frame=bytes([SLAVE,func,addr>>8,addr&255,count>>8,count&255])
    frame += crc16(frame)

    print(f"ASK func={func} addr={addr:#06x} count={count}")
    with socket.create_connection((IP,PORT), timeout=2) as s:
        s.settimeout(2)
        s.sendall(frame)
        data=s.recv(512)

    print("RAW", data.hex(" "))

for args in [
    (4, 0x1000, 10),
    (4, 0x2000, 10),
    (3, 0x0200, 10),
    (3, 0x2000, 10),
    (4, 0x0000, 10),
]:
    try:
        read(*args)
    except Exception as e:
        print("ERR", repr(e))
