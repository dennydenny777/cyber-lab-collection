import sys
from modules.subdomains import enumerate_subdomains
from modules.alive import check_alive_hosts
from modules.scanner import scan_ports
from modules.report import generate_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 recon.py <target-domain-or-ip>")
        sys.exit(1)

    target = sys.argv[1]
    print(f"[+] Starting reconnaissance on: {target}")

    subdomains = []
    if not target.replace(".", "").isdigit():  # domain case
        print("[+] Enumerating subdomains...")
        subdomains = enumerate_subdomains(target)
    else:
        print("[+] Target is an IP, skipping subdomain enumeration")

    hosts = [target] + subdomains

    print("[+] Checking alive hosts...")
    alive_hosts = check_alive_hosts(hosts)
    print(f"[+] {len(alive_hosts)} alive hosts found\n")

    print("[+] Scanning ports...")
    scan_results = scan_ports(alive_hosts)
    print("[+] Port scanning completed\n")

    generate_report(target, subdomains, alive_hosts, scan_results)

if __name__ == "__main__":
    main()
