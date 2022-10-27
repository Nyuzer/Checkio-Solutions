# https://py.checkio.org/en/mission/follow-instructions/

def follow(instructions):
    x, y = 0, 0
    for i in instructions:
        if i == 'f':
            y += 1
        if i == 'b':
            y -= 1
        if i == 'l':
            x -= 1
        if i == 'r':
            x += 1
    return (x, y)
