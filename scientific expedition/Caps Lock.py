def caps_lock(text):
    text = text.split('a')
    for i in range(len(text)):
        if i % 2 == 1:
            text[i] = text[i].upper()
    return ''.join(text)