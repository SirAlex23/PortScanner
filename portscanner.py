import socket
import sys
import time

def escanear_puertos(objetivo, puertos):
    
    print("\n--- Escáner de Puertos ---")
    
    try:
        # Intenta resolver el hostname a IP. Si ya es una IP válida, gethostbyname la devuelve.
        ip_objetivo = socket.gethostbyname(objetivo)
        print(f"[*] Objetivo: {ip_objetivo}")
    except socket.gaierror:
        # Esto sucede si pones un nombre de host mal escrito o si hay un problema de DNS/red.
        print("[!] ERROR: El hostname no pudo ser resuelto. Verifica la dirección.")
        sys.exit()
        
    inicio_tiempo = time.time()
    
    # Bucle principal para la lógica de escaneo
    for puerto in puertos:
        
        # Crea el objeto socket (AF_INET=IPv4, SOCK_STREAM=TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # Tiempo de espera bajo (0.5 segundos)
        
        # connect_ex devuelve 0 si el puerto está abierto, o un código de error.
        result = sock.connect_ex((ip_objetivo, puerto))
        
        if result == 0:
            print(f"[+] PUERTO ABIERTO: {puerto}")
        
        sock.close()
    
    fin_tiempo = time.time()
    tiempo_total = fin_tiempo - inicio_tiempo
    
    print(f"[*] Escaneo de {len(puertos)} puertos comunes completado.")
    print(f"[*] Tiempo Total: {tiempo_total:.2f} segundos")
    

if __name__ == "__main__":
    # Puertos comunes para un escaneo rápido
    puertos_comunes = [21, 22, 23, 25, 80, 443, 3306, 3389, 8080]
    ip_o_hostname = input("Ingrese la dirección IP o hostname a escanear: ")
    escanear_puertos(ip_o_hostname, puertos_comunes)