#!/usr/bin/python3

import json
import sys
import struct
import os
from utils import *
from urllib.parse import quote_plus
from datetime import datetime
from Format import Format


PATH = f"{os.path.expanduser('~')}/.LeetMarker/app/"
ERROR_FILE = f"{PATH}ERROR"
WARNING_FILE = f"{PATH}WARNING"
LOG_FILE = f"{PATH}LOG"


def log(message: str, file_type: str):
    '''
        :message: is the message to log
        :file_type: is the type of log:
            - e <- error
            - l <- log
            - w <- warning
    '''

    if file_type not in {'e', 'w', 'l'}:
        return

    file = (LOG_FILE if file_type ==
            'l' else ERROR_FILE) if file_type != 'w' else WARNING_FILE
    char = ('* ' if file_type == 'l' else '') if file_type != 'w' else '[!] '

    with open(file, 'a+') as f:
        f.write(f"{char}{message}\n")


# Read a message from stdin and decode it.
def get_message(length=4):
    raw_length = sys.stdin.buffer.read(length)

    if not raw_length:
        sys.exit(0)
    message_length = struct.unpack('=I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode("utf-8")
    return json.loads(message)


# Encode message
def encode_message(message_content):
    encoded_content = json.dumps(message_content).encode("utf-8")
    encoded_length = struct.pack('=I', len(encoded_content))
    return {'length': encoded_length, 'content': struct.pack(f"{len(encoded_content)}s", encoded_content)}


# Send encoded message
def send_message(encoded_message):
    sys.stdout.buffer.write(encoded_message['length'])
    sys.stdout.buffer.write(encoded_message['content'])
    sys.stdout.buffer.flush()


# Encode message & send
def send(message: str):
    message = encode_message(message)
    send_message(message)


def main_native():
    while True:
        message = get_message()
        log(f"Received message: {message}", 'l')
        if message == "ping":
            log(f"pong! @ {datetime.now().strftime('%Y:%M:%d ~ %H:%m:%S')}", 'l')
            send("pong")

        elif '|' in message:
            headline, selected_text, link = message.split('-|||-')
            log(f"url: {link}, headline: {headline}, selected_text: {selected_text}", 'l')
            if not template_file_exists():
                create_template()

            format = Format()
            format.set_headline(headline)
            format.set_selected_text(selected_text)
            format.set_link(link)
            format.set_time()
            format.write()

            send("saved")


def main():
    date = datetime.now().strftime("%Y:%M:%d ~ %H:%m:%S")
    try:
        log(f"\n===== Started @ {date} =====", 'l')
        main_native()
    except Exception as e:
        log(f"\n===== FATAL ERROR @ {date}: {e} =====", 'e')


main()
