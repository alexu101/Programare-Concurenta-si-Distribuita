import socket
import time

class TcpServer:
    def __init__(self, ip, port, buffer_size, operation):
        self.ip = ip
        self.port = port
        self.buffer_size = buffer_size
        self.operation = operation
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(5)  # Listen for up to 5 connections
        print(f"TCP Server listening on {ip}:{port}")

    def listen(self):
        conn, addr = self.sock.accept()
        print(f"Connection from {addr}")
        start_time = time.time()
        total_bytes_read = 0
        messages_read = 0

        if self.operation == "streaming":
            while True:
                data = conn.recv(self.buffer_size)
                if not data:
                    break
                total_bytes_read += len(data)
                messages_read += 1
        else:  # stop-and-wait
            while True:
                data = conn.recv(self.buffer_size)
                if not data:
                    break
                total_bytes_read += len(data)
                messages_read += 1
                conn.sendall(b'ACK')  # Acknowledge receipt

        print(f"TCP, {self.operation}, {messages_read} messages read,{total_bytes_read} bytes read")

        conn.close()
