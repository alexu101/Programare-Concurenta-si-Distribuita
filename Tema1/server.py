# Write a program that measure the time to transfer various amount of data (500MB, 1GB (1.5
# milion of WhatsApp messages, 4000 photos, 10.000 emails or reuse a large buffer)) under
# various conditions (Make sure you are sending bytes. Do not use higher-level functions that
# assume you are writing strings.)
# Requirements for implementation:
# A) Supported protocols as parameters (for both client/server): UDP, TCP
# B) Message size: 1 to 65535 bytes
# C) Two mechanisms should be implemented: streaming and stop-and-wait (acknowledge is
# performed before the sending of the next message)
# Requirements for output:
# A) After each server session, the server will print: used protocol, number of messages read,
# number of bytes reads
# B) At the end of execution, the client will print: transmission time, number of sent messages,
# number of bytes sent.
# Language: you can use any language for implementation. The program must run on a Linux
# system.
# Evaluation:
# • Client/Server Code
# • A pdf/word/plain text document with details regarding options for client/server and with
# statistics regarding performed tests.
# Hint: Your system architecture can have a two-tier architecture or a multi-tier one. (e.g. a middle tier
# can perform queuing/scheduling of clients request, connection management, traffic monitoring,
# connection to a back-end database et.al.)

import sys
from classes.TcpServer import TcpServer
from classes.UdpServer import UdpServer

IP = "127.0.0.1"
PROTOCOL_TCP = "tcp"
PROTOCOL_UDP = "udp"
MESSAGE_SIZE = 65535
BUFFER_SIZE = 1024

def main():
    if len(sys.argv) < 3:
        print("Usage: python server.py <protocol> <operation>")
        sys.exit(1)

    protocol = sys.argv[1]
    operation = sys.argv[2]

    if protocol not in [PROTOCOL_TCP, PROTOCOL_UDP]:
        print(f"Protocol {protocol} is not supported.")
        sys.exit(1)

    if operation not in ["streaming", "stop-and-wait"]:
        print(f"Operation {operation} is not supported.")
        sys.exit(1)

    if protocol == PROTOCOL_TCP:
        server = TcpServer(IP, 1080, BUFFER_SIZE, operation)
        server.listen()
    else:
        server = UdpServer(IP, 1081, BUFFER_SIZE, operation)
        server.recv_file()

    #python server.py [protocol] [operation]

if __name__ == "__main__":
    main()