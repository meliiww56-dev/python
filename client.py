import socket
import threading
import sys

# =========================
# CONFIGURATION
# =========================
# Use the server's actual IP address if connecting from another computer
HOST = '192.168.250.209'  # <-- replace with your server's LAN IP
PORT = 65432

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# =========================
# FUNCTION TO RECEIVE MESSAGES
# =========================
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                # Print received message
                sys.stdout.write(message)
                sys.stdout.flush()
            else:
                print("\n[DISCONNECTED] Server closed the connection.")
                client.close()
                break
        except Exception as e:
            print(f"\n[ERROR] Connection error: {e}")
            client.close()
            break

# =========================
# FUNCTION TO SEND MESSAGES
# =========================
def send_messages():
    while True:
        try:
            msg = input()  # User input
            client.send(msg.encode('utf-8'))  # Send to server
        except Exception as e:
            print(f"[ERROR] Sending message failed: {e}")
            client.close()
            break

# =========================
# START CLIENT CONNECTION
# =========================
def start_client():
    try:
        client.connect((HOST, PORT))
        print(f"[CONNECTED] Connected to server {HOST}:{PORT}\n")

        # Start threads for receiving and sending messages
        threading.Thread(target=receive_messages, daemon=True).start()
        threading.Thread(target=send_messages, daemon=True).start()

        # Keep main thread alive
        while True:
            pass

    except ConnectionRefusedError:
        print(f"[ERROR] Cannot connect to server {HOST}:{PORT}. Make sure server is running.")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")

if __name__ == "__main__":
    start_client()
