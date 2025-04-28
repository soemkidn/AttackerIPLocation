import re

with open("payload.exe", "rb") as f:
    data = f.read()
    # 搜索IPv4模式（大端序）
    ips = re.findall(b"\xAC\x1B\x2C\xBA", data)
    ports = re.findall(b"\\x11\\x5C", data)
    for ip in ips: print(f"可疑IP: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}")
    for port in ports: print(f"可疑端口: {port[0]*256 + port[1]}")