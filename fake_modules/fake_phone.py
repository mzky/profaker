import random
import requests
import socket
import string
import time

def phone(status=0):
    """生成手机号,参数status为状态，1或其它值代表在线验证后的结果，0表示离线生成的结果"""
    while True:
        phone = random.choice(['134','135','136','137','138','139','150','151','152','157','158','159','187','188','130','131','132','155','156','185','186','133','153','180','189']) + ''.join(random.choice('0123456789') for i in range(8))
        if status == 0:
            return phone
        else:
            status += 1
            try:
                r = requests.get('http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=' + phone, timeout=2)
                obj = eval(r.text.split('=')[1], type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())
                if obj['telString'] == str(phone):
                    return phone
            except:
                if status >= 6:
                    return phone
