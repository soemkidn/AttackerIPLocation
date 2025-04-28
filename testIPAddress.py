import re

with open("payload.exe", "rb") as f:
    data = f.read()
    # 搜索IPv4模式（大端序）并输出地址
    for ip_match in re.finditer(b"\xAC\x1B\x2C\xBA", data):
        ip = ip_match.group()
        print(f"可疑IP: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]} | 文件偏移地址: 0x0040{ip_match.start():X}")

    # 搜索端口模式（大端序）并输出地址
    for port_match in re.finditer(b"\x11\\x5C", data):
        port = port_match.group()
        print(f"可疑端口: {port[0]*256 + port[1]} | 文件偏移地址: 0x0040{port_match.start():X}")