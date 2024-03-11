import socket
import time

class TcpClient:
    def __init__(self, server_ip, server_port, file_object, size, operation):
        self.server_ip = server_ip
        self.server_port = server_port
        self.file = file_object
        self.size = size
        self.operation = operation
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server_ip, self.server_port))

    def send_file(self):
        total_bytes_sent = 0
        messages_sent = 0
        start_time = time.time()

        data = self.file.read(self.size)
        while data:
            self.sock.sendall(data)
            total_bytes_sent += len(data)
            messages_sent += 1

            if self.operation == "stop-and-wait":
                # Wait for ACK
                self.sock.recv(1024) 

            data = self.file.read(self.size)

        # Measure and print transmission time
        end_time = time.time()
        print(f"Transmission time: {end_time - start_time} seconds, Messages sent: {messages_sent}, Bytes sent: {total_bytes_sent}")

        self.sock.close()
