#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/2/17
"""
## phkit
phoneme toolkit: 音素相关的文本处理工具箱。

### 安装

```
pip install -U phkit
```

todo:
文本正则化处理
数字读法
字符读法
常见规则读法


文本转拼音
pypinyin
国标和alnum转换

anything转音素
字符
英文
汉字
OOV

进阶:
分词
命名实体识别
依存句法分析
"""

__version__ = "0.0.3"

version_doc = """
### 版本
v{}
""".format(__version__)

from .symbol import __doc__ as doc_symbol
from .sequence import __doc__ as doc_sequence
from .pinyin import __doc__ as doc_pinyin
from .phoneme import __doc__ as doc_phoneme
from .number import __doc__ as doc_number
from .convert import __doc__ as doc_convert

from .convert import fan2jian, jian2fan, quan2ban, ban2quan
from .number import say_digit, say_decimal, say_number
from .pinyin import text2pinyin, split_pinyin
from .sequence import text2sequence, text2phoneme, phoneme2sequence, sequence2phoneme
from .sequence import symbol_chinese, ph2id_dict, id2ph_dict

if __name__ == "__main__":
    print(__file__)
