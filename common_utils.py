import random
import string


def get_ramdom_str(length):
    """
    获取指定长度的随机字符串（包含大小写阿拉伯字母和非0数字）
    """
    lst = [random.choice(string.ascii_letters+string.digits[1::]) for i in range(length)]
    ret = ''.join(lst)
    return ret


