import socket
import threading

# Server IP and port
HOST = '192.168.250.209'  # Replace with your server computer's IP
PORT = 65432

# List to keep track of connected clients
clients = []
client_lock = threading.Lock()


def broadcast(message, sender_conn):
    """Send a message to all clients except the sender"""
    with client_lock:
        for client in clients:
            if client != sender_conn:
                try:
                    client.send(message)
                except:
                    remove_client(client)


def handle_client(conn, addr):
    """Handle messages from a specific client"""
    print(f"[NEW CONNECTION] {addr} connected")
    welcome_msg = f"[SERVER] Client {addr} has joined the chat.\n".encode('utf-8')
    broadcast(welcome_msg, conn)

    while True:
        try:
            data = conn.recv(1024)
            if data:
                full_message = f"[{addr[1]}] {data.decode('utf-8').strip()}".encode('utf-8')
                print(f"Broadcasting: {full_message.decode('utf-8')}")
                broadcast(full_message, conn)
            else:
                break
        except Exception as e:
            print(f"[ERROR] Connection error {addr}: {e}")
            break

    remove_client(conn)
    print(f"[DISCONNECTED] {addr} disconnected")
    disconnect_msg = f"[SERVER] Client {addr} has left the chat.\n".encode('utf-8')
    broadcast(disconnect_msg, None)


def remove_client(conn):
    """Remove client from the list and close connection"""
    with client_lock:
        if conn in clients:
            try:
                conn.close()
            except:
                pass
            clients.remove(conn)


def server_write_messages():
    """Allow server to send messages manually to all clients"""
    while True:
        try:
            msg = input()  # Server types a message
            if msg.strip() != "":
                full_msg = f"[SERVER] {msg}".encode('utf-8')
                broadcast(full_msg, None)
        except Exception as e:
            print(f"[ERROR] Failed to send server message: {e}")


def start_server():
    """Start the server and accept new client connections"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}...")

    # Start a thread to allow server to send messages manually
    threading.Thread(target=server_write_messages, daemon=True).start()

    while True:
        try:
            conn, addr = server.accept()
            with client_lock:
                clients.append(conn)
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
            print(f"[ACTIVE CONNECTIONS] Current connections: {threading.active_count() - 2}")  # subtract main + server input threads
        except Exception as e:
            print(f"[ERROR] Server error: {e}")


if __name__ == "__main__":
    start_server()
