import socket
import json
import os 

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_address = ('localhost', 49152)  # Use 'localhost' for local testing
server_socket.bind(server_address)
file_path = 'Farm_Data.json'
server_socket.listen(5)

#fist make empty dictionary (use later). 
#Then we want to split the string we recived with from each slash. Ex string: pH:6.8/EC:2/Date:2024-04-01 14:49:57
#Then enter each new entry into the dictionary, the keys are on the left of : and the keys on the right are the values
#If files already exist, then append onto the end, if not, make a new JSON file. 
def writeJson(log_message):
    new_entry = {}
    print(log_message)
    #each entry is seperated by a / 
    splitWordList = log_message.split('/')
    for entry in splitWordList:
        #each entry has a key and a value seperated by a :
        splitEntries = entry.split(';')
        new_entry[splitEntries[0]] = splitEntries[1]

    #print(new_entry)
    if os.path.exists(file_path):

        with open(file_path, 'r') as file:
            existing_data = json.load(file)

        existing_data.append(new_entry)

        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)
    #if JSON file doesn't exist, creates a new JSON file, a list and puts last entry in it. 
    else:
        listOfDictEntries = []
        listOfDictEntries.append(new_entry)
        with open(file_path, 'w') as file:
            json.dump(listOfDictEntries, file, indent=4)

    print(f"New entry added to '{file_path}' successfully.")


print(f"Server is listening on {server_address[0]}:{server_address[1]}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection established from {client_address}")
    
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:  # Check if no more data is received (client closed connection)
                print(f"Connection closed by {client_address}")
                break  # Exit the inner loop and wait for the next connection
            

            #f"{data.decode()}" is the string that was passed for the other computer
            #creates the JSON File
            writeJson(f"{data.decode()}")
            
            
            print(f"Received data from {client_address}: {data.decode()}")
            
            # Optionally, send a response back to the client
            response = "Message received!"
            client_socket.sendall(response.encode())
    
    finally:
        client_socket.close()
