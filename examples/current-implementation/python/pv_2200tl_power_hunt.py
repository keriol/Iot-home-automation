import socket, struct, time

IP="PV_INVERTER_IP"
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

def read_reg(addr):
    frame=bytes([SLAVE,FUNC,addr>>8,addr&255,0,1])
    frame += crc16(frame)

    with socket.create_connection((IP,PORT), timeout=1) as s:
        s.settimeout(1)
        s.sendall(frame)
        data=s.recv(64)

    # accetta risposte tipo: 01 03 02 XX XX CRC CRC [extra]
    if len(data) < 7:
        raise ValueError(data.hex(" "))

    body=data[:5]
    recv_crc=data[5:7]

    if data[:3] != bytes([SLAVE,FUNC,2]):
        raise ValueError(data.hex(" "))

    if recv_crc != crc16(body):
        raise ValueError("bad crc " + data.hex(" "))

    return int.from_bytes(data[3:5],"big"), data.hex(" ")

for addr in range(0, 80):
    try:
        raw, hx = read_reg(addr)
        if raw != 0:
            print(f"{addr:04d} / {addr:#06x}: raw={raw:<6} x1={raw:<8} x0.1={raw*0.1:<8.1f} x0.01={raw*0.01:<8.2f} hex={hx}")
    except Exception:
        pass
    time.sleep(0.08)
