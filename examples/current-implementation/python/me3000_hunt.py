import socket, struct

IP="PV_INVERTER_IP"   # quello che rispondeva bene
PORT=8899
SLAVE=1
FUNC=3

def crc16(data):
    crc=0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return struct.pack("<H", crc)

def read(addr,count=16):
    frame=bytes([SLAVE,FUNC,addr>>8,addr&255,count>>8,count&255])
    frame += crc16(frame)

    with socket.create_connection((IP,PORT), timeout=1.5) as s:
        s.settimeout(1.5)
        s.sendall(frame)
        data=s.recv(512)

    print(f"\nADDR {addr}")
    print("RAW:",data.hex(" "))

    if len(data) < 5:
        return

    bc=data[2]
    payload=data[3:3+bc]

    regs=[]
    for i in range(0,len(payload),2):
        regs.append(int.from_bytes(payload[i:i+2],"big"))

    for i,v in enumerate(regs):
        print(f"{addr+i:04d}: {v}")

for a in [
    0,16,32,48,
    64,80,96,
    112,128,144,
    160,176,192,
    208,224,240
]:
    try:
        read(a)
    except Exception as e:
        print("ERR",a,e)
