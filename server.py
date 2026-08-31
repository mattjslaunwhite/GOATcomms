import socket
import threading

clients = {}  # Format: {conn: username}
addresses = {}

def broadcast(message, sender_conn=None):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                client.close()
                remove_client(client)

def remove_client(conn):
    if conn in clients:
        name = clients[conn]
        del clients[conn]
        del addresses[conn]
        print(f"[-] {name} disconnected.")
        broadcast(f"[Server] {name} has left the chat.\n".encode('utf-8'))
        send_user_list()

def send_user_list():
    user_list = ", ".join(clients.values())
    list_msg = f"[Active Users]: {user_list}\n".encode('utf-8')
    broadcast(list_msg)

def handle_client(conn, addr):
    try:
        # Receive username first
        username = conn.recv(1024).decode('utf-8').strip()
        clients[conn] = username
        addresses[conn] = addr
        print(f"[+] {username} connected from {addr}")
        
        broadcast(f"[Server] {username} has joined the chat.\n".encode('utf-8'), conn)
        send_user_list()

        while True:
            msg = conn.recv(2048)
            if not msg:
                break
            # Relay message with sender name
            formatted_msg = f"<{username}>: ".encode('utf-8') + msg
            broadcast(formatted_msg, conn)
    except:
        pass
    finally:
        conn.close()
        remove_client(conn)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("[*] Chat Server started on port 9999...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
