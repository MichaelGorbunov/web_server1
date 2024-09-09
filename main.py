import os
# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer

from dotenv import load_dotenv


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    # def do_GET(self):
    #     """ Метод для обработки входящих GET-запросов """
    #     self.send_response(200)  # Отправка кода ответа
    #     self.send_header("Content-type", "application/json")  # Отправка типа данных, который будет передаваться
    #     self.end_headers()  # Завершение формирования заголовков ответа
    #     self.wfile.write(bytes("{'message': 'OK'}", "utf-8"))  # Тело ответа
    def do_GET(self):

        if self.path == "/":
            # Если запрошен корневой URL, отправляем страницу
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Читаем содержимое HTML-файла с контактами
            with open("contacts.html", "r", encoding="utf-8") as f:
                html_content = f.read()
            self.wfile.write(bytes(html_content, "utf-8"))
        else:
            # Если запрошен другой URL, отправляем 404 Not Found
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<h1>404 Not Found</h1>", "utf-8"))

    def do_POST(self):
        """Метод обработки входящих  POST-запросов"""
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    load_dotenv()
    # Для начала определим настройки запуска
    host_name = os.getenv("HOST_NAME")
    srv_port = int(os.getenv("SERVER_PORT"))
    # print(host_name, srv_port)
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((host_name, srv_port), MyServer)
    print(f"Server started http://{host_name}:{srv_port}")

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
