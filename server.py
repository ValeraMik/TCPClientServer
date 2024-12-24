import socket

def start_server():
    # Параметри сервера
    host = '127.0.0.1'  # Локальний хост
    port = 65432        # Порт для з'єднання

    # Створення сокета TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Очікування до 5 клієнтів
    print(f"Сервер запущено на {host}:{port}")

    while True:
        # Прийняття з'єднання від клієнта
        client_socket, client_address = server_socket.accept()
        print(f"З'єднання встановлено з {client_address}")

        # Отримання даних від клієнта
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Отримано повідомлення: {data}")

        # Відповідь клієнту
        response = f"Сервер отримав ваше повідомлення: {data}"
        client_socket.send(response.encode('utf-8'))

        # Закриття з'єднання
        client_socket.close()
        print("З'єднання закрито\n")

if __name__ == "__main__":
    start_server()
