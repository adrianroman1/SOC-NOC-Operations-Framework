import re
import logging

# SOC Tool: SIEM Triage Simulator for Brute Force & Log Analysis
# Aimed at reducing alert fatigue by distinguishing True Positives from False Positives.

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [SOC-TRIAGE] - %(message)s')
logger = logging.getLogger("SecurityAnalyst")

def triage_siem_alerts(logs, threshold=3):
    """
    Analyzes authentication logs to identify potential Brute Force attacks.
    Threshold: Number of failed attempts before escalating to True Positive.
    """
    logger.info(f"Analyzing {len(logs)} log entries for security anomalies...")
    
    # Regex pattern to extract IPv4 addresses from security logs
    ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    failed_attempts = {}

    for log in logs:
        if "Failed password" in log or "Invalid user" in log:
            match = re.search(ip_pattern, log)
            if match:
                ip = match.group(1)
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
    
    for ip, count in failed_attempts.items():
        if count >= threshold:
            logger.error(f"[ALERT] TRUE POSITIVE: Brute Force detected from {ip} ({count} failed attempts). Escalating to Incident Response.")
        else:
            logger.warning(f"[INFO] LOW PRIORITY: Potential False Positive for {ip} ({count} attempts). Monitoring source.")

if __name__ == "__main__":
    # Simulated raw log stream from a Linux/Cloud environment
    raw_security_logs = [
        "Jan 24 10:01:05 sshd[1234]: Failed password for root from 192.168.1.15 port 5522 ssh2",
        "Jan 24 10:01:08 sshd[1234]: Failed password for root from 192.168.1.15 port 5526 ssh2",
        "Jan 24 10:01:12 sshd[1234]: Failed password for root from 192.168.1.15 port 5530 ssh2",
        "Jan 24 10:05:00 sshd[1235]: Failed password for admin from 10.0.0.5 port 22 ssh2"
    ]
    
    triage_siem_alerts(raw_security_logs)
                       
