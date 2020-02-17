#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/2/17
"""
"""
from .phoneme import py2ph
from .pinyin import han2pinyin


def han2phoneme(han, py_errors=None, ph_errors=None):
    out = []
    pys = han2pinyin(han, errors=py_errors)
    for py in pys:
        phs = py2ph(py, errors=ph_errors)
        out.extend(phs)
    return out


if __name__ == "__main__":
    print(__file__)
    assert han2phoneme("汉字转音素") == ['h', 'an', '4', 'z', 'iy', '4', 'zh', 'uan', '3', 'ii', 'in', '1', 's', 'u', '4']
    assert han2phoneme("汉,a1") == ['h', 'an', '4', ',a1']
