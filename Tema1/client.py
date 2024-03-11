import sys
from classes.TcpClient import TcpClient
from classes.UdpClient import UdpClient

IP = "127.0.0.1"
PROTOCOL_TCP = "tcp"
PROTOCOL_UDP = "udp"
MESSAGE_SIZE = 65535
BUFFER_SIZE = 1024

def main():
    if len(sys.argv) < 5:
        print("Usage: python client.py <protocol> <operation> <file> <size>")
        sys.exit(1)

    protocol = sys.argv[1]
    operation = sys.argv[2]
    file = sys.argv[3]
    size = int(sys.argv[4])

    if protocol not in [PROTOCOL_TCP, PROTOCOL_UDP]:
        print(f"Protocol {protocol} is not supported.")
        sys.exit(1)

    if operation not in ["streaming", "stop-and-wait"]:
        print(f"Operation {operation} is not supported.")
        sys.exit(1)

    if protocol == PROTOCOL_TCP:
        with open(file, "rb") as f:
            client = TcpClient(IP, 1080, f, size, operation)
            client.send_file()
    else:
        with open(file, "rb") as f:
            client = UdpClient(IP, 1081, f, size, operation)
            client.send_file()

if __name__ == "__main__":
    main()