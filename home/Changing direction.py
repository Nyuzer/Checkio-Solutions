# https://py.checkio.org/en/mission/changing-direction/

def changing_direction(nums):
    result = 0
    flag = 0
    sec_flag = 0
    prev_num = nums[0]
    for num in nums:
        if prev_num == num:
            continue
        elif flag == 0 and prev_num < num:
            prev_num = num
        elif flag == 1 and prev_num > num:
            prev_num = num
        else:
            prev_num = num
            if flag == 0:
                flag = 1
                if sec_flag == 0:
                    result -= 1
            elif flag == 1:
                flag = 0
            result += 1
        sec_flag += 1
    return result
