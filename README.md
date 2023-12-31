

# UDP Communication Script

This Python script is a simple implementation of UDP (User Datagram Protocol) communication. It allows you to send and receive messages over a network using the UDP protocol.

## How to Use

1. Run the script.
2. When prompted, enter the destination IP address and port number.
3. The script will bind a socket to your machine's IP address in my case (`100.64.7.1`) and the specified port number (you can easily change it from the script itself).
4. The script on other side will also bind to your other machine's IP adress and the specified (same) port number.
5. It will then send a message saying 'Hello, I am Windows, using UDP!' and recieve 'Hello, I am Linux' to the specified destination.
6. The script will then enter a loop where it waits for incoming messages and allows you to send messages.

## Features

- **UDP Communication**: This script uses Python's `socket` library to implement UDP communication.
- **Message Sending and Receiving**: The script can send and receive messages over the network.
- **User Interaction**: The script prompts the user for input and displays received messages.

## Requirements

- Python 3.x
- A network connection

## Note

Please ensure that the port number entered is an integer. If a non-integer value is entered, the script will print an error message and exit.

## Disclaimer

This script does not implement any form of encryption or security measures. It is recommended to use it in a secure and private network.

I hope this helps! Let me know if you need anything else.
