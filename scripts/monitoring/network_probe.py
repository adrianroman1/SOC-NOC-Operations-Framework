import socket
import datetime
import sys

# NOC Tool: Network Availability Monitor for RTO compliance
# Designed for high-frequency connectivity checks at Layer 4 (TCP)

def check_infrastructure_status(targets):
    """
    Performs a TCP handshake check against critical infrastructure targets.
    Essential for NOC environments to ensure RTO objectives are met.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n--- [NOC SESSION] {timestamp} ---")
    
    for host, port in targets.items():
        # Creăm socket-ul (AF_INET = IPv4, SOCK_STREAM = TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2.5) # Timeout optimizat pentru rețele enterprise
        
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"[UP] {host}:{port} - Service responsive. RTO Compliance: OK")
            else:
                print(f"[CRITICAL] {host}:{port} - SERVICE DOWN! Error Code: {result}")
        except socket.error as e:
            print(f"[ERROR] {host}:{port} - Network unreachable: {e}")
        finally:
            sock.close()

if __name__ == "__main__":
    # Monitorizare Servicii Enterprise (Exemple: Web Server, Database, BTP Connector)
    CRITICAL_TARGETS = {
        "127.0.0.1": 8080, # BTP Adapter Port
        "127.0.0.1": 443,  # SSL Gateway
        "127.0.0.1": 3306  # Database (Ex: MySQL for Diana/Valoris)
    }
    
    check_infrastructure_status(CRITICAL_TARGETS)
  
