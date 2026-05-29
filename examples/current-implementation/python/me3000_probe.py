import socket
import struct
import time

IP = "STORAGE_INVERTER_IP"
PORT = 8899

def crc16(data):
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return struct.pack("<H", crc)

def query(slave, func, addr):
    frame = bytes([
        slave,
        func,
        addr >> 8,
        addr & 0xFF,
        0,
        1
    ])
    frame += crc16(frame)

    try:
        with socket.create_connection((IP, PORT), timeout=1) as s:
            s.settimeout(1)
            s.sendall(frame)
            data = s.recv(64)

        if len(data) >= 5:
            print(
                f"slave={slave} func={func} addr={addr} "
                f"-> {data.hex(' ')}"
            )

    except:
        pass

for slave in [1,2,3,4,5,10,11,247]:
    for func in [3,4]:
        for addr in [
            0,1,10,50,100,
            500,1000,1500,
            2000,3000,5000
        ]:
            query(slave, func, addr)
            time.sleep(0.05)
