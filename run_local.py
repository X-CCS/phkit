#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2019/12/1
"""
local
"""
import logging

logging.basicConfig(level=logging.INFO)


def run_text2phoneme():
    from phkit.sequence import text2phoneme, text2sequence
    text = "汉字转音素，TTS：《Text to speech》。"
    out = text2phoneme(text)
    print(out)
    # ['h', 'an', '4', '-', 'z', 'iy', '4', '-', 'zh', 'uan', '3', '-', 'ii', 'in', '1', '-', 's', 'u', '4', '-', ',',
    # 'Tt', 'Tt', 'Ss', ':', '(', 'T', 'E', 'X', 'T', '#', 'T', 'O', '#', 'S', 'P', 'E', 'E', 'C', 'H', ')', '.', '-',
    #  '~', '_']
    out = text2sequence(text)
    print(out)
    # [11, 32, 76, 2, 28, 51, 76, 2, 29, 59, 75, 2, 12, 46, 73, 2, 22, 56, 76, 2, 133, 97, 97, 96, 135, 138, 123, 108,
    # 127, 123, 137, 123, 118, 137, 122, 119, 108, 108, 106, 111, 139, 132, 2, 1, 0]


if __name__ == "__main__":
    print(__file__)
    run_text2phoneme()
    from phkit.sequence import symbol_chinese
    from phkit.symbol import _lower
    print(set(_lower) - set(symbol_chinese))
