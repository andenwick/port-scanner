# TCP Port Scanner

A fast, multi-threaded TCP port scanner written in Python.

## Features

- Scans a range of ports on any target host
- Multi-threaded scanning (100 concurrent threads) for speed
- Resolves hostnames to IP addresses
- Clean CLI interface with timing stats

## Usage

```bash
python port_scanner.py <target> [start_port] [end_port]
```

### Examples

```bash
# Scan common ports (1-1024) on localhost
python port_scanner.py localhost

# Scan specific port range
python port_scanner.py 192.168.1.1 80 443

# Scan a domain
python port_scanner.py example.com 1 1000
```

## Sample Output

```
Port Scanner
Target: localhost (127.0.0.1)
Started: 2026-01-26 17:00:00

Scanning localhost (ports 1-1024)...
----------------------------------------
  Port 22: OPEN
  Port 80: OPEN
  Port 443: OPEN
----------------------------------------
Scan complete. Found 3 open port(s).
Duration: 0:00:02.534
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## How It Works

Uses Python's `socket` library with `ThreadPoolExecutor` for concurrent port checking. Each port connection attempt has a 0.5 second timeout to balance speed and accuracy.

## Author

Anden Wickstrand
