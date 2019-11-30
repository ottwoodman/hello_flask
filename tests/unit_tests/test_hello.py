# -*- coding: utf8 -*-

# 引入待测试的代码
from app import hello


def test_hello_success():
    """
    test index, response successfully
    :return:
    """
    response = hello()  # response接受index()的返回结果
    assert response == 'Hello Flask!'  # 测试返回内容与预期返回内容相等
