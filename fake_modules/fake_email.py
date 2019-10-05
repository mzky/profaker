import random
import string
from fake_modules.utils.tools import get_number,get_lowercase,get_letter,get_mix

def _email():
    """生成邮箱地址"""
    array1 = ['126.com', '163.com', 'sina.com', 'sohu.com', 'yahoo.com.cn', 'gmail.com','yahoo.com']
    array2 = ['qq.com']

    array = random.choice([array1,array2])
    address = random.choice(array)
    if array == array2:
        salt = get_number(9)
        if salt.startswith('0'):
            user = '1' + salt
        else:
            user = salt
    else:
        user = get_lowercase(random.randint(6,10))

    fake_email = user + '@' + address
    return fake_email

def email(n=1):
    '''
    生成随机邮箱
    n = 1 return str
    n > 1 return list for str
    '''
    s = []
    for i in range(n):
        s.append(_email())
    if len(s) == 1:
        return s[0]
    else:
        return s
