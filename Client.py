import socket
import json
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10001)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

data = sock.recv(1000)
udata = data.decode("utf-8")

def get_function_name(f: str):
    s = f.split(' ')[1]
    return s[:s.index('(')].strip()
exec(udata + '\n' + get_function_name(udata) + '()')

with open("Client\data.json", "r") as read_file:
    jsondata = json.load(read_file)
b = bytes(str(jsondata),'utf-8')
sock.send(b)