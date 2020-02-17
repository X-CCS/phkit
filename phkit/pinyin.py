#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/2/17
"""
"""

from pypinyin import lazy_pinyin, Style


def han2pinyin(han, errors=None):
    """
    汉语文本转为拼音列表
    :param han: str,汉语文本字符串
    :param errors: function,对转拼音失败的字符的处理函数，默认保留原样
    :return: list,拼音列表
    """
    if errors is None:
        errors = "default"
    pin = lazy_pinyin(han, style=Style.TONE3, errors=errors, strict=True)
    return pin


if __name__ == "__main__":
    print(__file__)
    assert han2pinyin("拼音") == ['pin1', 'yin1']
    assert han2pinyin("汉字,a1") == ['han4', 'zi4', ',a1']
