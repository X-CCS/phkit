#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangdd
# date: 2020/2/17
"""
语音合成文本处理：
音素整理
辅音：
aa b c ch d ee f g h ii j k l m n oo p q r s sh t uu vv x z zh
元音：
a ai an ang ao e ei en eng er i ia ian iang iao ie in ing iong iu ix iy iz o ong ou u ua uai uan uang uen ueng uei ui un uo v van ve vn
音调：
1 2 3 4 5
字母：
Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz
英文：
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
标点：
! ? . , ; : " # ( )
注：!=!！|?=?？|.=.。|,=,，、|;=;；|:=:：|"="“|#=\s|(=(（[［{｛【<《|)=)）]］}｝】>》
预留：
0 6 7 8 9
其他：
_ ~ *


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

if __name__ == "__main__":
    print(__file__)
