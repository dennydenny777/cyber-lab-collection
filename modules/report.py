import os
from datetime import datetime

def generate_report(target, subdomains, alive_hosts, scan_results):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_content = []
    report_content.append("=" * 60)
    report_content.append(f"🔍 RECON REPORT")
    report_content.append(f"Target    : {target}")
    report_content.append(f"Generated : {timestamp}")
    report_content.append("=" * 60)

    if subdomains:
        report_content.append("\n🌐 Subdomains Found:")
        report_content.append("-" * 60)
        for s in subdomains:
            report_content.append(f"  • {s}")

    if alive_hosts:
        report_content.append("\n✅ Alive Hosts:")
        report_content.append("-" * 60)
        for host in alive_hosts:
            report_content.append(f"  • {host}")

    if scan_results:
        report_content.append("\n📡 Port Scan Results:")
        report_content.append("-" * 60)
        for host, ports in scan_results.items():
            report_content.append(f"\nHost: {host}")
            if ports:
                for port in ports:
                    report_content.append(f"  [OPEN] Port {port}")
            else:
                report_content.append("  No open ports found")

    # Summary
    total_open_ports = sum(len(p) for p in scan_results.values())
    report_content.append("\n📊 Summary:")
    report_content.append(f"  Total subdomains found : {len(subdomains)}")
    report_content.append(f"  Total alive hosts      : {len(alive_hosts)}")
    report_content.append(f"  Total open ports       : {total_open_ports}")
    report_content.append("=" * 60)
    report_content.append("📝 End of Report")
    report_content.append("=" * 60)

    # Linux-friendly results folder
    output_dir = os.path.expanduser("~/PROJECT/results")
    os.makedirs(output_dir, exist_ok=True)

    report_file = os.path.join(output_dir, f"recon_{target}.txt")
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report_content))

    # Print to console
    print("\n".join(report_content))
    print(f"[+] Report saved to {report_file}")
