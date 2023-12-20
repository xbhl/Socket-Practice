import socket
import sys

server_config = {
    "ip": "google.com",
    "port": 8080
}


class SocketClient:
    def __init__(self, host: str, port: int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.host: str = host
        self.port: int = port

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            print(f"[INFO] Connected to {self.host} on port {self.port}")
        except socket.error as e:
            print(f"[ERROR] Connection failed: {e}")
            sys.exit()

    def send(self):
        try:
            self.socket.sendall(b'Test')
            print("[INFO] Sent")
        except socket.error as e:
            print(f"[ERROR] Error during sending: {e}")

    def receive(self):
        try:
            print("t")
            b = self.socket.recv(1024)
            print(repr(b))
        except Exception as e:
            print(f"[ERROR] Socket not receiving: {e}")


def main():
    sock = SocketClient(server_config["ip"], server_config["port"])
    sock.connect()
    sock.send()
    sock.receive()


if __name__ == "__main__":
    main()