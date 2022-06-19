import socket
import os
from _thread import *

#author: Pawel Jurkiw
#email: 314275@uwr.edu.pl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 5027
counter = 0

try:
    s.bind((host, port))
except socket.error as err:
    print(str(err))

print('Waiting for connection')
s.listen()

def client_session(connection):
    connection.send(str.encode('Polaczenie nawiazane \r\n Tryb komend: QUIT - zakonczenie sesji, UPPER - tryb dataconversion z zamianą na wielkie litery i LOWER - tryb dataconversion z zamiana na male litery. \r\n \r\n'))
    
    while True:
        data = connection.recv(1024)
        command = data.decode('utf-8', 'ignore')

        if command == "QUIT":
            break
        elif command == "UPPER":
            connection.send(str.encode('\r\n Tryb dataconversion (UPPER) zapytania zostana zwrocone wielkimi literami jako odpowiedz (wyjście z trybu to sekwencja ENTER - . - ENTER) \r\n'))

            while True:
                data = connection.recv(1024)

                #end-of-data sprawdza czy znak to kropka, ponieważ poprzednie zapytanie wysyłamy za pomocą entera czyli '\r\n' po nim wpisujemy kropke i zatwierdzamy ponownie enterem 

                if data.decode('utf-8') == '.':
                    connection.send(str.encode('\r\n Tryb komend: QUIT - zakonczenie sesji, UPPER - tryb dataconversion z zamianą na wielkie litery i LOWER tryb dataconversion z zamiana na male litery. \r\n \r\n'))
                    break
                else:
                    connection.send(str.encode(str.upper(data.decode('utf-8'))))
        elif command == "LOWER":
            connection.send(str.encode('\r\n Tryb dataconversion (LOWER) zapytania zostana zwrocone malymi literami jako odpowiedz (wyjście z trybu to sekwencja ENTER - . - ENTER) \r\n'))

            while True:
                data = connection.recv(1024)

                if data.decode('utf-8') == '.':
                    connection.send(str.encode('\r\n Tryb komend: QUIT - zakonczenie sesji, UPPER - tryb dataconversion z zamianą na wielkie litery i LOWER tryb dataconversion z zamiana na male litery. \r\n \r\n'))
                    break
                else:
                    connection.send(str.encode(str.lower(data.decode('utf-8'))))
    connection.close()

while True:
    client, address = s.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_session, (client, ))
    counter += 1
    print('Client id: ' + str(counter))
s.close()
