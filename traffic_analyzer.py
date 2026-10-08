from collections import Counter
log_file = "network_logs.txt"
source_ips = []
ports = []
with open(log_file, "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 6:
            source_ip = parts[2]
            port = parts[5]
            source_ips.append(source_ip)
            ports.append(port)
ip_counts = Counter(source_ips)
port_counts = Counter(ports)
print("===NETWORK TRAFFIC ANALYSIS REPORT ===")
print("Total connection:", len(source_ips))
print("\nsource IP Activity:")
for ip, count in ip_counts.items():
    print(f"{ip}: {count} connections")
    if count >= 3:
        print(f"ALERT:Repeated traffic from {ip}")
print("\nPort Activity:")
for port,count in port_counts.items():
    print(f"Port {port}: {count} connections") 