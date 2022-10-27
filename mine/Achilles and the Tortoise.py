# https://py.checkio.org/en/mission/achilles-tortoise/

def chase(a1_speed, t2_speed, advantage):
    return advantage + float(t2_speed * advantage)/(a1_speed - t2_speed)
