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
connections = 0
currentID = 'white'


def thread_client(conn):
    global connections, currentID, board

    # var = board
    board.start_user = currentID
    data_string = pickle.dumps(board)

    if currentID == 'black':
        board.players = True

    conn.send(data_string)
    currentID = 'black'
    connections += 1

    if connections == 2:
        conn.send(data_string)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.decode().split()
        print(data)
        if 'select' in data:
            board.click(int(data[1]), int(data[2]))
        sendData = pickle.dumps(board)
        # print("Sending {}".format(sendData))
        conn.sendall(sendData)

    connections -= 1
    if connections < 2:
        board = Board()
        currentID = "white"
    print("Connection Closed")
    conn.close()


# print(pickle.dumps(board))
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(thread_client, (conn,))
