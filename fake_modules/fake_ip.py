import random
import string

def ip(count=''):
    """
            无参数时，全部随机，count参数可指定ip一，二，三位，
                    例如：count='192'
            count='192.168'
            count='192.168.136'
    """
    begin1 = begin2 = begin3 = 0
    end1 = end2 = end3 = 255
    ip = count.split('.')
    try:
        if ip[0] != '':
            end1 = begin1 = int(ip[0])
            if ip[1] != '':
                end2 = begin2 = int(ip[1])
                if ip[2] != '':
                    end3 = begin3 = int(ip[2])
    except:
        pass
    try:
        return socket.inet_ntoa(struct.pack('>I', random.randint(begin1 * 16777216 + begin2 * 65536 + begin3 * 256,
                                                                 end1 * 16777216 + end2 * 65536 + end3 * 256 + 255)))
    except:
        return False

