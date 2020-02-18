#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/2/16
"""
### sequence
转为序列的方法，文本转为音素列表，文本转为ID列表。
"""
from .phoneme import shengyun2ph_dict, char2ph_dict
from .pinyin import text2pinyin, split_pinyin
from .symbol import _chain, _eos, _pad, symbol_chinese
from .convert import fan2jian, quan2ban
import re

# 分隔英文字母
_en_re = re.compile(r"([a-zA-Z]+)")

ph2id_dict = {p: i for i, p in enumerate(symbol_chinese)}
id2ph_dict = {i: p for i, p in enumerate(symbol_chinese)}

assert len(ph2id_dict) == len(id2ph_dict)


def text2phoneme(text):
    """
    文本转为音素，用中文音素方案。
    中文转为拼音，按照清华大学方案转为音素，分为辅音、元音、音调。
    英文全部大写，转为字母读音。
    英文非全部大写，转为英文读音。
    标点映射为音素。
    :param text: str,正则化后的文本。
    :return: list,音素列表
    """
    out = []
    text = normalize_chinese(text)
    text = normalize_english(text)
    pys = text2pinyin(text, errors=py_errors)
    for py in pys:
        if type(py) is str:
            fuyuan, diao = split_pinyin(py)
            if fuyuan in shengyun2ph_dict:
                phs = shengyun2ph_dict[fuyuan].split()
                phs.append(diao)
            else:
                phs = []
        else:
            phs = list(py)
        if phs:
            out.extend(phs)
            out.append(_chain)
    out.append(_eos)
    out.append(_pad)
    return out


def text2sequence(text):
    phs = text2phoneme(text)
    seq = phoneme2sequence(phs)
    return seq


def phoneme2sequence(src):
    out = []
    for w in src:
        if w in ph2id_dict:
            out.append(ph2id_dict[w])
    return out


def sequence2phoneme(src):
    out = []
    for w in src:
        if w in id2ph_dict:
            out.append(id2ph_dict[w])
    return out


def py_errors(text):
    out = []
    for p in text:
        if p in char2ph_dict:
            out.append(char2ph_dict[p])
    return tuple(out)


def normalize_chinese(text):
    text = quan2ban(text)
    text = fan2jian(text)
    return text


def normalize_english(text):
    out = []
    parts = _en_re.split(text)
    for part in parts:
        if not part.isupper():
            out.append(part.lower())
        else:
            out.append(part)
    return "".join(out)


if __name__ == "__main__":
    print(__file__)
