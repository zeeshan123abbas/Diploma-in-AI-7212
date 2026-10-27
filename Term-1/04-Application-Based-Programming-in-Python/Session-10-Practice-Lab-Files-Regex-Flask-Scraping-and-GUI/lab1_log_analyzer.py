# lab1_log_analyzer.py
# Practice: file reading + regular expressions + exceptions (Sessions 06-07)
import re
from collections import Counter

LOG_FILE = "server.log"
line_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+)\s+(.*)$")
email_pattern = re.compile(r"user=([\w.]+@[\w.]+)")
ip_pattern = re.compile(r"ip=(\d+\.\d+\.\d+\.\d+)")

levels = Counter()
failed_logins = Counter()
ips = set()

try:
    with open(LOG_FILE, encoding="utf-8") as f:
        for line in f:
            match = line_pattern.match(line.strip())
            if not match:
                continue                      # skip lines that do not fit
            date, time, level, message = match.groups()
            levels[level] += 1
            email = email_pattern.search(message)
            if level == "ERROR" and email and "login failed" in message:
                failed_logins[email.group(1)] += 1
            ip = ip_pattern.search(message)
            if ip:
                ips.add(ip.group(1))
except FileNotFoundError:
    print("Log file not found:", LOG_FILE)
else:
    print("Lines per level :", dict(levels))
    print("Failed logins   :", dict(failed_logins))
    print("Unique IPs      :", sorted(ips))
    # write a short report file
    with open("log_report.txt", "w", encoding="utf-8") as out:
        out.write(f"Errors: {levels['ERROR']}\n")
        for user, count in failed_logins.items():
            out.write(f"{user} failed {count} time(s)\n")
    print("Report saved to log_report.txt")
