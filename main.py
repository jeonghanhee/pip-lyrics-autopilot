from sys import stdin, stdout, version_info
from json import dumps
from PyQt5.QtWidgets import QApplication
from threading import Thread
from caption import Caption
from communication import Communication

def main():
    app = QApplication([])
    communication = Communication()

    caption_thread = Caption(communication)
    native_message_thread = Thread(target=native_messaging_host, args=(communication,))

    caption_thread.start()
    native_message_thread.start()

    app.exec()

def native_messaging_host(communication):
    while True:
        try:
            message_length_bytes = stdin.buffer.read(4)
            if len(message_length_bytes) == 0:
                break
            message_length = int.from_bytes(message_length_bytes, byteorder='little')
            message = stdin.buffer.read(message_length).decode('utf-8')

            message = message[1:len(message)-1]

            communication.update_signal.emit(message)
        except Exception as e:
            error_response = {"error": str(e)}
            error_response_json = dumps(error_response)
            stdout.buffer.write(len(error_response_json).to_bytes(4, byteorder='little'))
            stdout.buffer.write(error_response_json.encode('utf-8'))
            stdout.buffer.flush()

if __name__ == "__main__" and version_info.major >= 3:
    main()