import socket

def start_client():
    # Параметри клієнта
    host = '127.0.0.1'  # Локальний хост (той самий, що і у сервера)
    port = 65432        # Порт (той самий, що і у сервера)

    # Створення сокета TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Підключення до сервера
        client_socket.connect((host, port))
        print(f"Підключено до сервера {host}:{port}")

        # Надсилання повідомлення серверу
        message = "Привіт, сервере!"
        client_socket.send(message.encode('utf-8'))
        print(f"Відправлено повідомлення: {message}")

        # Отримання відповіді від сервера
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Відповідь від сервера: {response}")

    finally:
        # Закриття з'єднання
        client_socket.close()
        print("З'єднання закрито")

if __name__ == "__main__":
    start_client()
