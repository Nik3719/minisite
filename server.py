import socket
import sys

def server() -> None:
    """  
    Эхо-сервер с обработкой разрыва соединения  
    """  
    HOST = '172.17.7.241'  
    PORT = 1500    

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Переиспользование порта
        server_socket.bind((HOST, PORT))   
        server_socket.listen(2)
        print(f"Server started on {HOST}:{PORT}")

        while True:  # Главный цикл для принятия новых соединений
            try:
                conn, address = server_socket.accept()  
                print("Connection from:", address)  

                while True:  # Цикл обработки одного соединения
                    try:
                        data = conn.recv(1024).decode()  
                        if not data:  
                            break  
                        print("Received:", data)  
                        conn.send(data.encode())
                    except ConnectionResetError:
                        print(f"Client {address} forcibly closed the connection")
                        break
                    except KeyboardInterrupt:
                        print("\nServer shutdown requested")
                        conn.close()
                        server_socket.close()
                        sys.exit(0)

            except KeyboardInterrupt:
                print("\nServer is shutting down...")
                break
            except Exception as e:
                print(f"Error with client {address}: {e}")
                continue

    finally:
        server_socket.close()
        print("Server stopped")

if __name__ == '__main__':  
    server()