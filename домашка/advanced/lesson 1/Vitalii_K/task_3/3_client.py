import socket
import struct

n1 = 111
n2 = 222
x_pack = struct.pack('ii', n1, n2)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 11111))
s.send(x_pack)
y_pack = s.recv(100)
s.close()

y_unpack = struct.unpack('i', y_pack)
y = y_unpack[0]
print(y)
