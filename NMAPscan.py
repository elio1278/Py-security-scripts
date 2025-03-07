import socket

def tcp_scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] TCP Port {port} is OPEN")
        sock.close()
    except Exception as e:
        print(f"[-] TCP Scan Error: {e}")

def udp_scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.sendto(b"\x00", (target, port)) 
        try:
            data, _ = sock.recvfrom(1024) 
            print(f"[+] UDP Port {port} is OPEN")
        except socket.timeout:
            print(f"[-] UDP Port {port} is FILTERED or CLOSED")
    except Exception as e:
        print(f"[-] UDP Scan Error: {e}")

def main():
    target = input("Enter target IP: ")
    scan_type = input("Enter scan type (tcp/udp/both): ").lower()
    ports = input("Enter ports (comma-separated): ")
    ports = [int(port.strip()) for port in ports.split(",")]

    if scan_type == "tcp":
        for port in ports:
            tcp_scan(target, port)
    elif scan_type == "udp":
        for port in ports:
            udp_scan(target, port)
    elif scan_type == "both":
        for port in ports:
            tcp_scan(target, port)
            udp_scan(target, port)
    else:
        print("Invalid scan type! Use 'tcp', 'udp', or 'both'.")

if __name__ == "__main__":
    main()
