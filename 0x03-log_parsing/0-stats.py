#!/usr/bin/python3
"""
A script for parsing HTTP request logs.
"""

import sys
import signal
import re


def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    print_stats(total_size, status_counts)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0
log_format = re.compile(r'(?P<ip>[\d\.]+) - \[.*\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)')

try:
    for line in sys.stdin:
        match = log_format.match(line)
        if match:
            status_code = int(match.group("status"))
            file_size = int(match.group("size"))
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)
except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    sys.exit(0)

print_stats(total_size, status_counts)
