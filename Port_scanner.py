import socket
#modulo importato

OPEN_PORTS = []

def get_host_ip_addr(target):
    try:
        ip_addr = socket.gethostbyname(target)
    except socket.gaierror as e:
        print(f"c'è stato un errore... {e}")
    else:
        return ip_addr
        
def scan_port(ip, port):  # Definizione della funzione a cui vengono passati due valori, ip e port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Andiamo a specificare il tipo o la famiglia di porte usate, inet vuol dire che sarà un IPV4 e socket stream che sarà un TCP
    sock.settimeout(1.0) #timeout
    conn_status = sock.connect_ex((ip, port))
    if conn_status == 0:
        OPEN_PORTS.append(port)
    sock.close()

if __name__ == "__main__":
    print("Porgramma scritto per solo scopo educativo !!!")
    target = input("Inserire Target: ")
    ip_addr = get_host_ip_addr(target)
    while True:
        try:
            port = int(input("Inserire Porta: "))
            scan_port(ip_addr, port)
            print(OPEN_PORTS)
        except KeyboardInterrupt:
            print("\nExciting...")
            break