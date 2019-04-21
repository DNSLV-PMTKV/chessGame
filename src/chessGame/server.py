import socket
from _thread import *
from board import Board
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '127.0.0.1'
port = 4444

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print('Waiting connection')
board = Board()


def thread_client(conn):
    var = pickle.dumps(board)
    conn.send(var)
    while True:
        data = conn.recv(1024)
        # reply = data
        if not data:
            break
        print(data.decode())
        conn.send(var)
    conn.close()


# print(pickle.dumps(board))
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(thread_client, (conn,))
