import socket
import datetime

#When sending a string, each '/' represents a new entry.
#Key value pairs are seperated with a :
#EXAMPLE: ("pH:6.8/EC:2/Date:09.07.2005)

# Sender (client) parameters
server_ip = '174.164.61.190'  # for website server, 174.164.61.190. For Local device, localhost
server_port = 49152  

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (receiver)
client_socket.connect((server_ip, server_port))

# Send a string message

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
message = ("pH:6.8/EC:2/Date:" + formatted_datetime)
client_socket.sendall(message.encode())

client_socket.close()
