# https://py.checkio.org/en/mission/secret-message/

import re


def find_message(message):
    message = re.sub('[^A-Z]', '', message)
    return message
