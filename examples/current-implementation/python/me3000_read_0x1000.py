import socket, struct

IP="STORAGE_INVERTER_IP"
PORT=8899
SLAVE=1
FUNC=4

def crc16(data):
    crc=0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return struct.pack("<H", crc)

def read(addr, count):
    frame=bytes([SLAVE,FUNC,addr>>8,addr&255,count>>8,count&255])
    frame += crc16(frame)

    with socket.create_connection((IP,PORT), timeout=1) as s:
        s.settimeout(1)
        s.sendall(frame)
        data=s.recv(512)

    print(f"RAW {data.hex(' ')}")

    if len(data) < 5 or data[1] != FUNC:
        return

    byte_count=data[2]
    payload=data[3:3+byte_count]
    regs=[int.from_bytes(payload[i:i+2],"big") for i in range(0,len(payload),2)]

    for i, val in enumerate(regs):
        print(f"{addr+i:#06x} / {addr+i:05d}: {val}")

for start in [0x1000, 0x1010, 0x1020, 0x1030, 0x1040]:
    print(f"\n==== start {start:#06x} ====")
    try:
        read(start, 16)
    except Exception as e:
        print("ERR", repr(e))
