import socket

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143,
                443, 445, 3389, 8080, 8443, 3306, 5900]

def scan_ports(hosts):
    results = {}
    for host in hosts:
        open_ports = []
        print(f"[+] Scanning ports on {host} ...")
        for port in COMMON_PORTS:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                if sock.connect_ex((host, port)) == 0:
                    open_ports.append(port)
                    print(f"    ✅ Port {port} is open")
                sock.close()
            except Exception:
                pass
        results[host] = open_ports
    return results
