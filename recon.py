import sys
from modules.subdomains import enumerate_subdomains
from modules.alive import check_alive_hosts
from modules.scanner import scan_ports
from modules.report import generate_report

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python recon.py <target>")
        sys.exit(1)

    target = sys.argv[1]

    print(f"[+] Starting recon on {target}")

    # Enumerate subdomains (if target is domain)
    if '.' in target and not target.replace('.', '').isdigit():
        subdomains = enumerate_subdomains(target)
        print(f"[+] Found subdomains: {subdomains}")
    else:
        subdomains = [target]  # If IP, treat as single host

    # Check alive hosts
    alive_hosts = check_alive_hosts(subdomains)
    print(f"[+] Alive hosts: {alive_hosts}")

    # Scan ports
    scan_results = scan_ports(alive_hosts)
    print(f"[+] Scan results: {scan_results}")

    # Generate report
    generate_report(target, subdomains, alive_hosts, scan_results)

    print("[+] Recon complete")
