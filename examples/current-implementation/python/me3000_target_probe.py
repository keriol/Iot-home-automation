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

def q(func, addr, count=10):
    frame=bytes([SLAVE, func, addr>>8, addr&255, count>>8, count&255]) + crc16(bytes([SLAVE, func, addr>>8, addr&255, count>>8, count&255]))
    try:
        with socket.create_connection((IP,PORT), timeout=0.4) as s:
            s.settimeout(0.4)
            s.sendall(frame)
            data=s.recv(256)
    except Exception as e:
        return None

    print(f"func={func} addr={addr} count={count} -> {data.hex(' ')}")

for func in [3,4]:
    for addr in [0,1,16,32,256,512,768,1024,1025,1030,1040,1050,1100,1150,4096,8192]:
        q(func, addr, 10)
