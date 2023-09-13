import socket

Dest_ip_address = input("Enter IP address: ")
port = input("Enter port number: ")
my_ip = "10.0.2.15"

try:
    port = int(port)
except ValueError:
    print("Invalid port number. Please enter a valid integer.")
    exit(1)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((my_ip, port))
    data_to_send = b'Hello, I am Windows, using UDP!'
    destination = (Dest_ip_address, port)
    s.sendto(data_to_send, destination)

    while True:
        received_data, sender_address = s.recvfrom(1024)
        print(f"Received from {sender_address}: {received_data.decode('utf-8')}")

        user_input = input(f"Enter the message to be sent to {Dest_ip_address} (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'
        if user_input:
            s.sendto(user_input.encode('utf-8'), destination)