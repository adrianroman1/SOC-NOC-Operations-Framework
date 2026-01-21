import socket
import datetime

# Monitorizarea disponibilității serviciilor critice (NOC Dashboard)
def check_service_status(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((ip, port))
        print(f"[{datetime.datetime.now()}] SUCCESS: Service on {ip}:{port} is UP.")
    except:
        print(f"[{datetime.datetime.now()}] ALERT: Service on {ip}:{port} is DOWN!")
    finally:
        s.close()

# Verificare servere interne/cloud
if __name__ == "__main__":
    check_service_status("127.0.0.1", 80) # HTTP
    check_service_status("127.0.0.1", 443) # HTTPS
