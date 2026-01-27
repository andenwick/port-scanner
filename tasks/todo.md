# Port Scanner - Todo

## Plan
Create a basic Python port scanner that:
- Scans a target host for open ports
- Supports custom port range
- Shows results clearly

## Tasks
- [x] Create port_scanner.py with basic TCP scanning functionality
- [x] Add command-line argument parsing
- [x] Test the scanner

## Review
Created `port_scanner.py` - a simple TCP port scanner with:
- Socket-based TCP connection scanning
- Command-line args: target, start_port (default 1), end_port (default 1024)
- 1-second timeout per port
- Clean output showing open ports and scan duration

Tested successfully on localhost.
