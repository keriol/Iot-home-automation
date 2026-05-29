import socket, struct, time

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

    with socket.create_connection((IP,PORT), timeout=0.8) as s:
        s.settimeout(0.8)
        s.sendall(frame)
        data=s.recv(512)

    if len(data) < 5 or data[0] != SLAVE or data[1] != FUNC:
        print(f"{addr:#06x}: RAW {data.hex(' ')}")
        return

    byte_count=data[2]
    expected=3+byte_count+2
    if len(data) < expected:
        print(f"{addr:#06x}: TRUNC {data.hex(' ')}")
        return

    payload=data[3:3+byte_count]
    regs=[int.from_bytes(payload[i:i+2],"big") for i in range(0,len(payload),2)]

    print(f"\n==== {addr:#06x} / {addr} ====")
    for i,v in enumerate(regs):
        print(f"{addr+i:#06x} / {addr+i:05d}: {v}")

for start in [
    0x0000, 0x0010, 0x0020, 0x0030,
    0x0200, 0x0210, 0x0220,
    0x0300, 0x0310, 0x0320,
    0x0400, 0x0410, 0x0420,
    0x0480, 0x0490,
    0x0500, 0x0510, 0x0520,
    0x0600, 0x0610,
    0x2000, 0x2010, 0x2020
]:
    try:
        read(start, 16)
    except Exception as e:
        pass
    time.sleep(0.1)
