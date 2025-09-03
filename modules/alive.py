import subprocess
import platform

def check_alive_hosts(hosts):
    alive = []
    ping_flag = "-n" if platform.system() == "Windows" else "-c"

    for host in hosts:
        try:
            print(f"[+] Pinging {host} ...")
            result = subprocess.run(
                ["ping", ping_flag, "1", host],
                capture_output=True, text=True
            )
            if "ttl=" in result.stdout.lower():
                alive.append(host)
                print(f"    ✅ {host} is alive")
            else:
                print(f"    ❌ {host} is unreachable")
        except Exception:
            print(f"    ❌ {host} ping failed")
    return alive
