import random
import string
import time

def make_id():
    """随机生成18为身份证"""
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    t = time.localtime()[0]  # 年份
    k = '{:0>2}{:0>2}{:0>2}{:0>4}{:0>2}{:0>2}{:0>3}'.format(random.randint(10, 99),
                                                            random.randint(1, 99),
                                                            random.randint(1, 99),
                                                            random.randint(t - 80, t - 18),
                                                            random.randint(1, 12),
                                                            random.randint(1, 28),
                                                            random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(k[i]) * ARR[i]
    return '%s%s' % (k, LAST[y % 11])

def check_id(ID):
    '''
    检查身份证是不是符合要求 ARP为每个数字的权重
    '''
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    xlen = len(str(ID))
    if xlen != 18:
        return False
    try:
        if xlen == 18:
            x2 = ID[6:14]
            x3 = time.strptime(x2, '%Y%m%d')
            if x2 < '19000101' or x3 > time.localtime():
                return False
        else:
            x2 = time.strptime(ID[6:12], '%y%m%d')
    except:
        return False
    if xlen == 18:
        y = 0
        for i in range(17):
            y += int(ID[i]) * ARR[i]

        if LAST[y % 11] != ID[-1].upper():
            return False
    return True

