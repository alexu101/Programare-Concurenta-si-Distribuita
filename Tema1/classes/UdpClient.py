import socket
import time

class UdpClient:
    def __init__(self, server_ip, server_port, file_object, size, operation):
        self.server_ip = server_ip
        self.server_port = server_port
        self.file = file_object
        self.size = size
        self.operation = operation
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_file(self):
        total_bytes_sent = 0
        messages_sent = 0
        start_time = time.time()

        data = self.file.read(self.size)
        while data:
            self.sock.sendto(data, (self.server_ip, self.server_port))
            total_bytes_sent += len(data)
            messages_sent += 1

            if self.operation == "stop-and-wait":
                # Wait for ACK
                self.sock.recvfrom(1024)

            data = self.file.read(self.size)

        # Send a message to indicate the end of file transmission
        self.sock.sendto(b"END", (self.server_ip, self.server_port))

        # Measure and print transmission time
        end_time = time.time()
        print(f"Transmission time: {end_time - start_time} seconds, Messages sent: {messages_sent}, Bytes sent: {total_bytes_sent}")

        self.sock.close()
