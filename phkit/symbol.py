#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/2/16
"""
"""

_pad = '_'
_eos = '~'
_oov = '*'

# 中文音素表
# 辅音：27
_fuyin = [
    'aa', 'b', 'c', 'ch', 'd', 'ee', 'f', 'g', 'h', 'ii', 'j', 'k', 'l', 'm', 'n', 'oo', 'p', 'q', 'r', 's', 'sh',
    't', 'uu', 'vv', 'x', 'z', 'zh'
]

# 元音：43
_yuanyin = [
    'a', 'ai', 'an', 'ang', 'ao', 'e', 'ei', 'en', 'eng', 'er', 'i', 'ia', 'ian',
    'iang', 'iao', 'ie', 'in', 'ing', 'iong', 'iu', 'ix', 'iy', 'iz', 'o', 'ong', 'ou', 'u', 'ua', 'uai', 'uan',
    'uang', 'uen', 'ueng', 'uei', 'ui', 'un', 'uo', 'v', 'van', 've', 'vn', 'ng', 'uong'
]

# 音调：5
_yindiao = ['1', '2', '3', '4', '5']

# 字母：26
_alphabet = 'Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz'.split()

# 英文：26
_english = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()

# 标点：9
_biaodian = '! ? . , ; : " # ( )'.split()
# 注：!=!！|?=?？|.=.。|,=,，、|;=;；|:=:：|"="“|#=\s|(=(（[［{｛【<《|)=)）]］}｝】>》

# 其他：5
_other = '0 6 7 8 9'.split()

# 字母和符号：64
# 用于英文
_character = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'"(),-.:;? ')

# 字母、数字和符号：74
# 用于英文或中文（中文转为拼音字符串）
_character_digit = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\'"(),-.:;? ')

# 中文音素：144
# 支持中文环境、英文环境、中英混合环境
symbol_zh = [_pad, _eos] + _fuyin + _yuanyin + _yindiao + _alphabet + _english + _biaodian + _other

# 英文音素：66
# 支持英文环境
symbol_en = [_pad, _eos] + _character

# 简单音素：76
# 支持英文、中文环境，中文把文字转为拼音
symbol_simple = [_pad, _eos] + _character_digit
