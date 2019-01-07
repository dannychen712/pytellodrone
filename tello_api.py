import threading
import socket
import time


class TelloApi:
    """
    Represents tello drone, handles udp connection up and down
    """

    def __init__(self):
        self.tello_address = ('192.168.10.1', 8889)

        host = ''
        port = 5002

        self.locaddr = (host, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.locaddr)
        self.new_message = True
        self.message = "ok"

        # create thread for something, not sure yet
        self.recvThread = threading.Thread(target=self.receive)
        self.recvThread.start()

    def receive(self):
        while True:
            data, server = self.sock.recvfrom(1518)
            self.message = data.decode(encoding="utf-8")
            print(self.message)
            self.new_message = True

    def do(self, message):
        self.wait()
        msg = message.encode(encoding="utf-8")
        self.sock.sendto(msg, self.tello_address)

    def wait(self):
        for i in range(100):
            if self.new_message and self.message == "ok":
                self.new_message = False
                break
            else:
                time.sleep(0.2)

    def close_connection(self):
        self.wait()
        self.sock.close()
        self.recvThread.exit()
