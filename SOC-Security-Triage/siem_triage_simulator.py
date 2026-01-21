import re

# SOC Tool: Diferentierea intre True si False Positives (Brute Force Detection)
def triage_siem_alerts(logs):
    threshold = 3
    attempts = {}
    
    for log in logs:
        if "Failed password" in log:
            ip = re.search(r'from (\d+\.\d+\.\d+\.\d+)', log).group(1)
            attempts[ip] = attempts.get(ip, 0) + 1
            
    for ip, count in attempts.items():
        if count >= threshold:
            print(f"[ALERT] True Positive: Brute Force detectat de la IP {ip} ({count} incercari).")
        else:
            print(f"[INFO] Analiza in curs: Alerta potential False Positive pentru IP {ip}.")

logs = [
    "Failed password for admin from 192.168.1.15",
    "Failed password for admin from 192.168.1.15",
    "Failed password for admin from 192.168.1.15"
]
triage_siem_alerts(logs)

