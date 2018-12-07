#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# Author: jacky
# Time: 14-2-22 下午11:48
# Desc: 短信http接口的python代码调用示例
import http.client
import urllib
import json
from common_utils import get_ramdom_str
from urllib.request import quote


# 参数的配置 请登录zz.253.com 获取以下API信息 ↓↓↓↓↓↓↓

# 创蓝接口域名
host = "smssh1.253.com"
# 创蓝API账号
account = "N0721527"
# 创蓝API密码
password = "jrOed4nN7H717c"

# 端口号
port = 80

# 版本号
version = "v1.1"

# 余额查询的URL
balance_get_uri = "/msg/balance/json"

# 普通短信发送的URL
sms_send_uri = "/msg/send/json"


def get_user_balance():
    """
    取账户余额
    """
    params = {'account': account, 'password': password}
    params = json.dumps(params)

    headers = {"Content-type": "application/json"}
    conn = http.client.HTTPConnection(host, port=port)
    conn.request('POST', balance_get_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


def send_sms(text, phone):
    """
    能用接口发短信
    """
    params = {'account': account, 'password': password, 'msg': quote(text), 'phone': phone, 'report': 'false'}
    params = json.dumps(params)

    headers = {"Content-type": "application/json"}
    conn = http.client.HTTPConnection(host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == '__main__':
    phone = "18827198456"
    # 设置您要发送的内容：其中“【】”中括号为运营商签名符号，多签名内容前置添加提交
    code = get_ramdom_str(6)
    text = "【253云通讯】您的验证码是%s" % code
    # 查账户余额
    print(get_user_balance())

    # 调用智能匹配模版接口发短信
    print(send_sms(text, phone))
