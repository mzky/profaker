# -*- coding: utf-8 -*-

"""
根据需要生成随机仿真内容，如身份证，手机号，邮箱地址等
需要安装requests 可使用pip install requests方式快速安装，或屏蔽在线验证手机号代码
"""
import random
import requests
import socket
import string
import struct
import time

'''''''''''''''
1.生成和效验身份证
'''''''''''''''
def makeID18():
    u"""随机生成18为身份证"""
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    t = time.localtime()[0]  # 年份
    k = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
                                          random.randint(01, 99),
                                          random.randint(01, 99),
                                          random.randint(t - 80, t - 18),
                                          random.randint(1, 12),
                                          random.randint(1, 28),
                                          random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(k[i]) * ARR[i]
    return '%s%s' % (k, LAST[y % 11])


def MakeID(count, x=''):
    u"""生成15或18位身份证,参数count为位数,x为获取结尾为x的身份证"""
    if str(count) == '15':
        u'''生成15位身份证'''
        strID = makeID18()
        # logger.Success('makeID15:ok')
        return strID[0:6] + strID[8:17]
    elif str(count) == '18' and x != '':
        while True:
            strX = makeID18()
            if strX[17:18] == str(x).upper():
                # logger.Success('makeID18+X:ok')
                return strX
    elif str(count) == '18':
        return makeID18()
    # logger.Error('参数错误!')
    return u'参数错误!'


def CheckID(ID):
    u"""效验身份证号码,参数ID为15或18位身份证号"""
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    xlen = len(ID)
    if xlen != 18 and xlen != 15:
        # logger.Error('CheckID:身份证号码长度错误！')
        return u'身份证号码长度错误！'
    try:
        if xlen == 18:
            x2 = ID[6:14]
            x3 = time.strptime(x2, '%Y%m%d')
            if x2 < '19000101' or x3 > time.localtime():
                # logger.Error('CheckID:身份证出生时间错误，超过允许的时间范围！')
                return u'身份证出生时间错误，超过允许的时间范围！'
        else:
            x2 = time.strptime(ID[6:12], '%y%m%d')
    except:
        # logger.Error('CheckID:身份证出生时间错误，非合法时间！')
        return u'CheckID:身份证出生时间错误，非合法时间！'
    if xlen == 18:
        y = 0
        for i in range(17):
            y += int(ID[i]) * ARR[i]

        if LAST[y % 11] != ID[-1].upper():
            # logger.Error('CheckID:身份证效验码错误！')
            return u'身份证效验码错误！'
    # logger.Success('CheckID:ok')
    return u'YES，' + str(xlen) + u'位身份证号正确！'


def IDoldToNew(ID):
    u"""15位身份证号转18位身份证号，参数count为15位身份证"""
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    if len(ID) != 15:
        # logger.Error('IDoldToNew:身份证号码输入错误，身份证号码长度不为15位')
        return u'身份证号码输入错误，身份证号码长度不为15位'
    oldcard = '%s19%s' % (ID[:6], ID[6:])
    y = 0
    for i in range(17):
        y += int(oldcard[i]) * ARR[i]
    # logger.Success('IDoldToNew:ok')
    return '%s%s' % (oldcard, LAST[y % 11])


'''''''''''''''
2.生成手机号
'''''''''''''''
def MakePhone(status=0):
    u"""生成手机号,参数status为状态，1或其它值代表在线验证后的结果，0表示离线生成的结果"""
    while True:
        phone = random.choice(['134','135','136','137','138','139','150','151','152','157','158','159','187','188','130','131','132','155','156','185','186','133','153','180','189']) + ''.join(random.choice('0123456789') for i in range(8))
        if status == 0:
            # 无网络环境情况 ，但会出现少量不正确的手机号
            # logger.Success('MakePhone:offline ok')
            return phone
        else:
            # 为确保手机号正确,调用第三方接口进行验证
            status += 1
            try:
                r = requests.get('http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=' + phone, timeout=2)
                # print r.status_code #返回值200为正确
                obj = eval(r.text.split('=')[1], type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())
                if obj['telString'] == str(phone):
                    # logger.Success('MakePhone:online ok')
                    return phone
            except:
                if status >= 6:
                    # 尝试连接验证手机号大于5次后，不再进行验证，直接返回随机值
                    # logger.Success('MakePhone:网络异常！直接返回offline手机号！')
                    return phone
                    # logger.Success('MakePhone:手机号验证不通过，或网络异常！')


'''''''''''''''
3.生成指定长度的随机数
'''''''''''''''
def MakeNum(count=10):
    u"""指定长度随机数，参数count为位数，默认10"""
    num = int(str(random.random()).split('.')[1])
    while len(str(num)) < count:
        num = num * num
    # logger.Success('MakeNum:ok')
    return str(num)[0:count]


'''''''''''''''
4.生成随机用户名，包括中文用户和英文用户，参数为位数
'''''''''''''''
def MakeUser(Language='cn', count=2):
    u"""生成随机用户名，参数Language为中文用户或英文用户，参数count为用户名位数"""
    if Language.lower() == 'cn':
        array1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱',
                  '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢',
                  '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌',
                  '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛',
                  '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮',
                  '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵',
                  '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅',
                  '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        array2 = ['秀', '娟', '英', '华', '慧', '巧', '美', '娜', '静', '淑', '惠', '珠', '翠', '雅', '玉', '萍', '红',
                  '娥', '玲', '芬', '芳', '燕', '彩', '春', '菊', '兰', '凤', '梅', '琳', '素', '云', '莲', '真', '环',
                  '雪', '荣', '爱', '妹', '霞', '香', '莺', '媛', '艳', '瑞', '凡', '佳', '嘉', '琼', '勤', '珍', '贞',
                  '莉', '桂', '叶', '璧', '璐', '娅', '琦', '晶', '妍', '茜', '秋', '珊', '莎', '锦', '黛', '倩', '婷',
                  '姣', '婉', '娴', '瑾', '颖', '露', '瑶', '怡', '婵', '雁', '蓓', '仪', '荷', '丹', '蓉', '眉', '君',
                  '琴', '蕊', '薇', '菁', '梦', '岚', '苑', '柔', '竹', '霭', '凝', '晓', '欢', '霄', '枫', '芸', '菲',
                  '寒', '欣', '滢', '伊', '亚', '宜', '可', '姬', '舒', '影', '荔', '枝', '思', '丽', '秀', '飘', '育',
                  '馥', '琦', '晶', '妍', '茜', '秋', '珊', '莎', '锦', '黛', '青', '倩', '婷', '宁', '蓓', '纨', '苑',
                  '婕', '馨', '瑗', '琰', '韵', '融', '园', '艺', '咏', '卿', '聪', '澜', '纯', '毓', '悦', '昭', '冰',
                  '爽', '琬', '茗', '羽', '希', '伟', '刚', '勇', '毅', '俊', '峰', '强', '军', '平', '保', '东', '文',
                  '辉', '明', '永', '健', '世', '广', '志', '义', '兴', '良', '海', '山', '仁', '波', '贵', '福', '生',
                  '龙', '元', '全', '国', '胜', '学', '祥', '才', '发', '武', '新', '清', '飞', '彬', '富', '顺', '信',
                  '子', '杰', '涛', '昌', '成', '康', '星', '天', '达', '安', '岩', '中', '茂', '进', '林', '有', '坚',
                  '和', '彪', '诚', '先', '敬', '震', '振', '壮', '会', '思', '群', '豪', '心', '邦', '承', '乐', '功',
                  '松', '善', '厚', '庆', '磊', '民', '友', '裕', '河', '哲', '江', '超', '亮', '政', '谦', '亨', '奇',
                  '固', '之', '轮', '翰', '朗', '伯', '宏', '言', '鸣', '朋', '斌', '梁', '栋', '维', '启', '克', '伦',
                  '翔', '旭', '鹏', '泽', '辰', '士', '以', '建', '家', '致', '树', '炎', '德', '行', '时', '泰', '盛']
        front = array1[random.randint(0, len(array1) - 1)]
        last = ''
        for i in range(count - 1):
            last = last + array2[random.randint(0, len(array2) - 1)]
        # logger.Success('MakeUser:cn username ok')
        return "%s%s" % (front.decode("utf-8"),last.decode("utf-8"))
    elif Language.lower() == 'en':
        array3 = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h',
                  'g', 'f', 'e', 'd', 'c', 'b', 'a']
        enName = ''
        for i in range(count):
            enName = enName + array3[random.randint(0, len(array3) - 1)]
        # logger.Success('MakeUser:en username ok')
        return enName.capitalize()
    else:
        # logger.Error('MakeUser:参数错误！')
        return '参数错误！'


'''''''''''''''
5.生成随机邮箱地址
'''''''''''''''
def MakeMail(count=12):
    u"""生成邮箱地址，参数count为邮箱位数,如参数过小，直接输出最短邮箱，例如：a@a.a"""
    array1 = ['@126.com', '@163.com', '@sina.com', '@sohu.com', '@yahoo.com.cn', '@qq.com', '@bjca.org.cn']
    last = array1[random.randint(0, len(array1) - 1)]
    if count < 5:
        # logger.Error('MakeMail:参数过小，无法生成！')
        return u'参数过小，无法生成！'
    elif count == 8:
        try:
            last = '@qq.com'
            salt = ''.join(random.sample(string.ascii_letters + string.digits, int(count - len(last))))
            # logger.Success('MakeMail:ok')
            return salt + last
        except:
            # logger.Error('MakeMail:执行异常！')
            return u'执行异常！'
    elif count == 9:
        try:
            last = random.choice(['@qq.com', '@163.com', '@126.com'])
            salt = ''.join(random.sample(string.ascii_letters + string.digits, int(count - len(last))))
            # logger.Success('MakeMail:ok')
            return salt + last
        except:
            # logger.Error('MakeMail:执行异常！')
            return u'执行异常！'
    elif count >= 10 | count <= 13:
        try:
            last = random.choice(['@qq.com', '@163.com', '@126.com', '@sina.com', '@sohu.com'])
            salt = ''.join(random.sample(string.ascii_letters + string.digits, int(count - len(last))))
            # logger.Success('MakeMail:ok')
            return salt + last
        except:
            # logger.Error('MakeMail:执行异常！')
            return u'执行异常！'
    elif count > 13:
        try:
            salt = ''.join(random.sample(string.ascii_letters + string.digits, int(count - len(last))))
            # logger.Success('MakeMail:ok')
            return salt + last
        except:
            # logger.Error('MakeMail:执行异常！')
            return u'执行异常！'
    else:
        salt1 = ''.join(random.sample(string.ascii_letters, 1))
        salt2 = ''.join(random.sample(string.ascii_letters, count - 4))
        # logger.Success('MakeMail:ok')
        return salt2 + '@' + salt1 + '.' + salt1


'''''''''''''''
5.生成IP地址
'''''''''''''''
def MakeIP(count=''):
    u"""
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
        # logger.Error('未输入参数或参数错误!')
    try:
        # logger.Success('MakeIP:ok')
        # inet_pton()支持IPV6；inet_ntoa仅支持IPV4
        return socket.inet_ntoa(struct.pack('>I', random.randint(begin1 * 16777216 + begin2 * 65536 + begin3 * 256,
                                                                 end1 * 16777216 + end2 * 65536 + end3 * 256 + 255)))
    except:
        # logger.Error('参数输入错误!')
        return u'参数输入错误!'


'''''''''''''''
全部测试内容
'''''''''''''''
def test():
    print u'==========1.身份证号=========='
    print MakeID(15)
    print MakeID(18)
    print MakeID(18, 1)  # 生成位数为1的身份证号
    print MakeID(18, 'X')  # 生成位数为X的身份证号
    print CheckID(MakeID(15))
    print CheckID(MakeID(18))
    print CheckID(IDoldToNew(MakeID(15)))
    print u'==========2.手机号=========='
    print MakePhone(0)
    print MakePhone(1)
    print MakePhone()
    print u'==========3.随机数=========='
    print MakeNum(2)  # 3位随机数
    print MakeNum(20)  # 20位随机数
    print MakeNum()
    print u'==========4.用户名=========='
    print MakeUser()
    print MakeUser('Cn', 4)
    print MakeUser('cN', 3)
    print MakeUser('cn', 2)
    print MakeUser('EN', 6)
    print MakeUser('en', 20)
    print u'==========5.邮箱=========='
    print MakeMail(6)
    print MakeMail(7)
    print MakeMail(8)
    print MakeMail(9)
    print MakeMail(10)
    print MakeMail()
    print MakeMail(5)
    print MakeMail(4)
    print MakeMail(13)
    print MakeMail(14)
    print u'==========5.IP地址=========='
    print MakeIP()
    print MakeIP('192')
    print MakeIP('192.168')
    print MakeIP('192.168.136')


if __name__ == '__main__':
    test()
    #print CheckID("871662191607071315")
