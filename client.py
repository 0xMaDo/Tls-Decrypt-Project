import ssl
import socket
import os


HOST = '192.168.1.13'
PORT = 4443

keylog_file = '/home/client/tls_project/ssl_keys.log'


context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)


context.keylog_filename = keylog_file


context.load_cert_chain(certfile='client.crt', keyfile='client.key')


context.load_verify_locations('ca.crt')

context.check_hostname = False
context.verify_mode = ssl.CERT_REQUIRED


raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
raw_socket.connect((HOST, PORT))


tls_sock = context.wrap_socket(raw_socket, server_hostname='server')

try:
    print(f"[+] Connected! TLS version: {tls_sock.version()}")
    print(f"[+] Cipher used: {tls_sock.cipher()}")
    print(f"[+] Key log saved to: {keylog_file}")

 
    request = (
        "GET / HTTP/1.1\r\n"
        "Host: server\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    tls_sock.sendall(request.encode())

   
    response = b""
    while True:
        chunk = tls_sock.recv(4096)
        if not chunk:
            break
        response += chunk

    print(f"[*] Response from server:\n{response.decode()}")

except Exception as e:
    print(f"[!] Error: {e}")

finally:
    tls_sock.close()
