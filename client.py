import socket
import threading
import sys

SERVER_IP = '127.0.0.1'  # Change to server IP if hosting remotely
PORT = 9999

def receive_messages(client):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if not message:
                break
            sys.stdout.write('\r' + ' ' * 80 + '\r') # Clear current input line
            print(message, end='')
            sys.stdout.write('You: ')
            sys.stdout.flush()
        except:
            print("\n[!] Disconnected from server.")
            break

def start_client():
    name = input("Enter your chat name/alias: ").strip()
    if not name:
        name = "Anonymous"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER_IP, PORT))
    except Exception as e:
        print(f"[!] Could not connect to server: {e}")
        return

    # Send username to server
    client.send(name.encode('utf-8'))
    print(f"[*] Connected as {name}. Type your messages below (type 'quit' to exit).")

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        try:
            sys.stdout.write('You: ')
            sys.stdout.flush()
            message = input()
            if message.lower() == 'quit':
                break
            if message.strip():
                client.send(message.encode('utf-8'))
        except KeyboardInterrupt:
            break

    client.close()

if __name__ == "__main__":
    start_client()
