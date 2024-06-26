import socket
import ssl
import struct
from concurrent.futures import ThreadPoolExecutor

DNS_SERVER = '1.1.1.1'  
DNS_PORT = 853          
LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 53535     
MAX_WORKERS = 10        

def init_tls_socket():
    context = ssl.create_default_context()
    wrapped_socket = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=DNS_SERVER)
    wrapped_socket.connect((DNS_SERVER, DNS_PORT))
    return wrapped_socket

def process_dns_query(dns_query, client_addr, udp_socket):
    try:
        with init_tls_socket() as tls_socket:
            query_length = struct.pack("!H", len(dns_query))
            tls_socket.sendall(query_length + dns_query)

            response = b''
            while True:
                part = tls_socket.recv(4096)
                if not part:
                    break
                response += part

            if response:
                response = response[2:]  
                udp_socket.sendto(response, client_addr)
    except Exception as e:
        print(f"Error processing DNS query: {e}")

def start_proxy():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((LISTEN_IP, LISTEN_PORT))
    print(f"n26-dns-tls-proxy is now listening on {LISTEN_IP}:{LISTEN_PORT}")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while True:
            dns_query, client_addr = udp_socket.recvfrom(512)
            executor.submit(process_dns_query, dns_query, client_addr, udp_socket)

if __name__ == "__main__":
    start_proxy()
