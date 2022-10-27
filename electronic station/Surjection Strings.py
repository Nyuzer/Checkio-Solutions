# https://py.checkio.org/en/mission/isometric-strings/

def isometric_strings(str1, str2):
    num_1 = []
    num_2 = []
    num = 0
    if len(str1) == len(str2):

        for i in range(len(str1)):
            if str1[i] in str1[:i]:
                num_1.append(str1.find(str1[i]))
            else:
                num_1.append(num)
                num += 1

        num = 0
        for i in range(len(str2)):
            if str2[i] in str2[:i]:
                num_2.append(str2.find(str2[i]))
            else:
                num_2.append(num)
                num += 1

    return num_1 == num_2
