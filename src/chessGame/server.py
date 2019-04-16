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
    data_string = pickle.dumps(board)
    conn.send(data_string)
    while True:
        try:
            data = conn.rect(8192*2)
            data = data.decode()
            if not data:
                break
            else:
                if data.count('select') > 0:
                    _all = data.split(' ')
                    col = int(_all[1])
                    row = int(_all[2])
                    color = _all[3]
                    board.click(col, row)
        except Exception as e:
            print(e)
            break


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(thread_client, (conn,))
