from multiprocessing import Pipe, Process
import random
import time

def genera_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
def clasifica_ip(ip):
    primer_octeto = int(ip.split('.')[0])
    if 0 <= primer_octeto <= 127:
        return 'A'
    elif 128 <= primer_octeto <= 191:
        return 'B'
    elif 192 <= primer_octeto <= 223:
        return 'C'
    elif 224 <= primer_octeto <= 239:
        return 'D'
    else:
        return 'E'


def valida_ip():
    pass

def proceso1_generar_ips(conn):

    
    for i in range(10):
        ip = genera_ip()
        print(f"IP generada #{i+1}: {ip}")
        conn.send(ip)
    
    # Enviar señal de finalización
    conn.send(None)
    conn.close()



def proceso2_filtrar_ips(conn_entrada, conn_salida):

    
    ips_filtradas = 0
    ips_descartadas = 0
    
    while True:
        ip = conn_entrada.recv()
        
        if ip is None:  # Señal de finalización
            break
        
        clase = clasifica_ip(ip)
        
        if clase in ['A', 'B', 'C']:
            print(f"IP {ip} (Clase {clase}) - ACEPTADA")
            conn_salida.send((ip, clase))
            ips_filtradas += 1
        else:
            print(f"IP {ip} (Clase {clase}) - RECHAZADA")
            ips_descartadas += 1
    
    # Enviar señal de finalización
    conn_salida.send((None, None))
    conn_entrada.close()
    conn_salida.close()
    
    print(f"Finalizado - Filtradas: {ips_filtradas}, Rechazadas: {ips_descartadas}")


def proceso3_mostrar_ips(conn):

    
    contador = 0
    
    while True:
        ip, clase = conn.recv()
        
        if ip is None:  
            break
        
        contador += 1
        print(f"{contador}. IP: {ip:<15} → Clase: {clase}")

def main():
    tiempo_inicio = time.time()
    

    conn1_send, conn1_recv = Pipe()
    conn2_send, conn2_recv = Pipe()
    

    p1 = Process(target=proceso1_generar_ips, args=(conn1_send,))
    p2 = Process(target=proceso2_filtrar_ips, args=(conn1_recv, conn2_send))
    p3 = Process(target=proceso3_mostrar_ips, args=(conn2_recv,))
    
    # Lanzar los procesos en orden
    p1.start()
    p2.start()
    p3.start()
    
    # Esperar a que todos terminen
    p1.join()
    p2.join()
    p3.join()
    
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio


if __name__ == "__main__":
    main()