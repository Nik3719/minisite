import socket

def client() -> None:
    """
    Эхо-клиент, подключающийся к серверу
    """
    HOST = '217.71.129.139' 
    PORT = 5652              

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаем сокет
    client_socket.connect((HOST, PORT))  # Подключаемся к серверу (кортеж в скобках!)

    message = input(" >> ")  # Вводим данные

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # Отправляем данные

        data = client_socket.recv(1024).decode()  # Получаем ответ
        print('Received from server: ' + data)

        message = input(" >> ")  # Повтор ввода

    client_socket.close()  # Закрываем соединение

if __name__ == '__main__':
    client()