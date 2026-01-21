import socket
import datetime

# NOC Tool: Monitorizarea disponibilității serviciilor pentru respectarea RTO
def check_infrastructure_status(targets):
    print(f"--- NOC Monitoring Session: {datetime.datetime.now()} ---")
    for host, port in targets.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        try:
            s.connect((host, port))
            print(f"[UP] {host}:{port} - In conformitate cu obiectivele RTO.")
        except Exception:
            print(f"[CRITICAL] {host}:{port} - DOWN! Actiune imediata necesara.")
        finally:
            s.close()

if __name__ == "__main__":
    # Monitorizare servere critice si aplicatii
    check_infrastructure_status({"127.0.0.1": 80, "127.0.0.1": 443})

