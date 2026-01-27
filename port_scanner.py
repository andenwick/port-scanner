#!/usr/bin/env python3
"""
Basic TCP Port Scanner
Usage: python port_scanner.py <target> [start_port] [end_port]
"""

import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_port(target: str, port: int, timeout: float = 0.5) -> tuple[int, bool]:
    """Attempt to connect to a specific port. Returns (port, is_open)."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()
        return (port, result == 0)
    except socket.error:
        return (port, False)


def scan_ports(target: str, start_port: int, end_port: int) -> list[int]:
    """Scan a range of ports using threads and return list of open ports."""
    open_ports = []

    print(f"Scanning {target} (ports {start_port}-{end_port})...")
    print("-" * 40)

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, target, port): port
                   for port in range(start_port, end_port + 1)}

        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:
                print(f"  Port {port}: OPEN")
                open_ports.append(port)

    return sorted(open_ports)


def main():
    if len(sys.argv) < 2:
        print("Usage: python port_scanner.py <target> [start_port] [end_port]")
        print("Example: python port_scanner.py 192.168.1.1 1 1024")
        sys.exit(1)

    target = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    # Resolve hostname to IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Cannot resolve hostname '{target}'")
        sys.exit(1)

    print(f"\nPort Scanner")
    print(f"Target: {target} ({target_ip})")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    start_time = datetime.now()
    open_ports = scan_ports(target_ip, start_port, end_port)
    end_time = datetime.now()

    print("-" * 40)
    print(f"Scan complete. Found {len(open_ports)} open port(s).")
    print(f"Duration: {end_time - start_time}")


if __name__ == "__main__":
    main()
