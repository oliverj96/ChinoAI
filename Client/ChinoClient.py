import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

# Header Portion
HEADER_LEN = 64 # may change later
HEADER_ID = 2 # max ID of 65,535

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) 

def sendmessage(id: int, msg: str):
    message = msg.encode(FORMAT)
    # Serialize msg length
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER_LEN - len(send_length))
    
    # Serialize id length
    message_id = str(id).encode(FORMAT)
    message_id += b' ' * (HEADER_ID - len(message_id))

    client.send(send_length)
    client.send(message_id)
    client.send(message)
    

sendmessage(1, "Hello Chino!")
sendmessage(0, '')