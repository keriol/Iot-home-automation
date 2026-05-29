import socket
import struct
import time

def crc16_modbus(data: bytes) -> bytes:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return struct.pack("<H", crc)

def read_holding(ip, port, slave, address, count, timeout=3):
    # Modbus RTU: slave, function 03, start address, count, crc
    frame = bytes([
        slave,
        0x03,
        (address >> 8) & 0xFF,
        address & 0xFF,
        (count >> 8) & 0xFF,
        count & 0xFF,
    ])
    frame += crc16_modbus(frame)

    with socket.create_connection((ip, port), timeout=timeout) as s:
        s.settimeout(timeout)
        print(f"SENT {ip}:{port} slave={slave} addr={address} count={count} -> {frame.hex(' ')}")
        s.sendall(frame)
        data = s.recv(1024)
        print(f"RECV {data.hex(' ')}")

    if len(data) < 5:
        return None

    if data[0] != slave or data[1] != 0x03:
        print("Unexpected header")
        return None

    byte_count = data[2]
    payload = data[3:3 + byte_count]
    recv_crc = data[3 + byte_count:3 + byte_count + 2]
    calc_crc = crc16_modbus(data[:3 + byte_count])

    if recv_crc != calc_crc:
        print(f"CRC mismatch recv={recv_crc.hex(' ')} calc={calc_crc.hex(' ')}")
    else:
        print("CRC OK")

    regs = []
    for i in range(0, len(payload), 2):
        regs.append(int.from_bytes(payload[i:i+2], "big"))

    return regs

ips = ["PV_INVERTER_IP", "STORAGE_INVERTER_IP"]
slaves = [1, 2, 247]
addresses = [0, 1, 100, 200, 300, 400, 500, 1000]

for ip in ips:
    print(f"\n================ {ip} ================")
    for slave in slaves:
        for address in addresses:
            try:
                regs = read_holding(ip, 8899, slave, address, 10)
                print("REGS:", regs)
            except Exception as e:
                print(f"ERR slave={slave} addr={address}: {repr(e)}")
            time.sleep(0.2)
