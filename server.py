import ssl
import socket

HOST = '0.0.0.0'
PORT = 4443


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)


context.load_cert_chain(certfile='server.crt', keyfile='server.key')


context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations('ca.crt')  


raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
raw_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
raw_socket.bind((HOST, PORT))
raw_socket.listen(5)

print(f"[*] TLS Server listening on port {PORT}...")

while True:
    client_sock, addr = raw_socket.accept()
    print(f"[+] Connection from {addr}")

   
    tls_sock = context.wrap_socket(client_sock, server_side=True)

    try:
       
        request = tls_sock.recv(4096).decode()
        print(f"[*] Received request:\n{request}")

        
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Connection: close\r\n"
            "\r\n"
            "<html><body><h1>Hello from TLS Server!</h1></body></html>"
        )
        tls_sock.sendall(response.encode())

    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        tls_sock.close()
