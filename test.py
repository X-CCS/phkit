#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/2/18
"""
"""


def test_phkit():
    from phkit import text2phoneme, text2sequence, symbol_chinese
    text = "汉字转音素，TTS：《Text to speech》。"
    target = ['h', 'an', '4', '-', 'z', 'iy', '4', '-', 'zh', 'uan', '3', '-', 'ii', 'in', '1', '-', 's', 'u', '4', '-',
              ',', 'Tt', 'Tt', 'Ss', ':', '(', 'T', 'E', 'X', 'T', '#', 'T', 'O', '#', 'S', 'P', 'E', 'E', 'C', 'H',
              ')', '.', '-', '~', '_']
    result = text2phoneme(text)
    assert result == target

    target = [11, 32, 74, 2, 28, 51, 74, 2, 29, 59, 73, 2, 12, 46, 71, 2, 22, 56, 74, 2, 131, 95, 95, 94, 133, 136, 121,
              106, 125, 121, 135, 121, 116, 135, 120, 117, 106, 106, 104, 109, 137, 130, 2, 1, 0]
    result = text2sequence(text)
    assert result == target

    assert len(symbol_chinese) == 143


if __name__ == "__main__":
    print(__file__)
