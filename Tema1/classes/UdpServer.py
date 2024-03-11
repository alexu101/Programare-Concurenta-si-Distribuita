import socket

class UdpServer:
    def __init__(self, ip, port, buffer_size, operation):
        self.ip = ip
        self.port = port
        self.buffer_size = buffer_size
        self.operation = operation
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.ip, self.port))
        print(f"UDP Server listening on {ip}:{port}")

    def recv_file(self):
        total_bytes_read = 0
        messages_read = 0

        while True:
            data, addr = self.sock.recvfrom(self.buffer_size)
            message = data.decode('utf-8')

            # Check for the end of transmission signal
            if message == "END":
                break

            total_bytes_read += len(data)
            messages_read += 1

            if self.operation == "stop-and-wait":
                # Send ACK for each received message immediately
                self.sock.sendto(b'ACK', addr)

        print(f"UDP, {self.operation}, {messages_read} messages read,{total_bytes_read} bytes read")
