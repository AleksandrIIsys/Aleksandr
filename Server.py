import socket
import json
def get_function(function_name, filepath):
    with open(filepath) as file:
        s = 'start'
        while True:
            s = file.readline()
            if s == '':
                break
            if 'def ' + function_name in s:
                indent = s.index('def ')
                f = ''
                f += s[indent:]
                while True:
                    s = file.readline()
                    if len(s) == 0:
                        return f
                    for i in range(indent + 1):
                        if s[i] != ' ':
                            return f
                    f += s[indent:]

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_addres = ('localhost',10001)
print('Starting up on {} port {}'.format(*server_addres))
sock.bind(server_addres)
sock.listen(5)
while True:
    print('waiting for a connection')
    connection, client_addres = sock.accept()
    try:
        print('connection from', client_addres)
        massage = bytes(get_function('f','Server\Summa.py'),"utf-8")
        connection.send(massage)
        while True:

            data = connection.recv(1000)
            udata = data.decode("utf-8")
            if data:
                pass
                print(udata)
            with open("Server\Result.json", "w") as write_file:
                json.dump(udata, write_file)

            connection.send(data)
            break
        else:
            print('no data from', client_address)
            break

    finally:
        print("Closing current connection")
        connection.close()
