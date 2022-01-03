import socket
import threading
import os
from dotenv import load_dotenv
from ChinoResponse import ChinoResponse
from ChinoAI import ChinoAI

load_dotenv()

PORT = int(os.getenv('PORT'))
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = os.getenv('FORMAT')

# Header Portion
HEADER_LEN = 64 # may change later
HEADER_ID = 2 # max ID of 65,535

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Handles message details
def message_received(id: int, msg: str) -> bool:
    chino = ChinoAI()
    chino_response = chino.process_message(id, msg)
    if chino_response.get_id() == 5:
        print('Error: {}'.format(chino_response.get_msg()))
        return False
    else:
        print('Chino\'s response ({}): {}'.format(chino_response.get_id(), chino_response.get_msg()))
    return True
 
# Handles client connection
def handle_client(conn, addr):
    print('[CONNECTED] {}'.format(addr))

    connected = True
    while connected:
        # Figure out the length of the message
        msg_length = conn.recv(HEADER_LEN).decode(FORMAT)
        if msg_length:
            msg_id = int(conn.recv(HEADER_ID).decode(FORMAT))
            print('Message id: {}'.format(msg_id))
            if msg_id == 0:
                connected = False
            else:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                success = message_received(msg_id, msg)
                if not success:
                    print('Error: message format incorrect.')
    print('[DISCONNECT] {}'.format(addr))
    conn.close() 

 
# Start listening to clients
def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr ))
        thread.start()


print('[STARTING SERVER] Starting ChinoAI Server.')
print('[LISTENING] Chino is listening on {}:{}'.format(SERVER, PORT))
start()
