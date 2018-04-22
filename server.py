import socket
import sys
import threading


class Server:
    def __init__(self):
        self.host = ''
        self.port = 50000
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except socket.error as message:
            if self.server:
                self.server.close()
            print("Could not open socket: " + message)
            sys.exit(1)

    def run(self):
        self.open_socket()
        running = 1
        while running:
            # handle the server socket
            try:
                (client, address) = self.server.accept()
            except OSError:
                running = 0;
            c = Client(client, address)
            c.start()
            self.threads.append(c)
            print("Zaakceptowano polaczenie z klientem na porcie:" + str(c.address[1]))

    def disconnect(self, client):
        self.threads.remove(client)
        if len(self.threads) < 1:
            self.server.close()
            print("Brak klientow koncze prace")


s = Server()


class Client(threading.Thread):
    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024

    def run(self):
        running = 1
        while running:
            try:
                data = self.client.recv(self.size)
                if data:
                    print("Odebralem wiadomosc (" + data.decode() + ") na porcie (" + str(
                        self.address[1]) + "), odsylam.")
                    self.client.send(data)
                else:
                    self.client.close()
                    running = 0
            except ConnectionResetError:
                print("Klient zakonczyl polaczenie na porcie:(" + str(self.address[1]) + ")")
                Server.disconnect(s, self)
                running = 0


s.run()
