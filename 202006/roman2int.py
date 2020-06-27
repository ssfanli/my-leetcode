#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: Ssfanli
@Time  : 2020/06/27 11:04 上午
@Desc  : roman to int
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """思路
        1. 将罗马数字单个字符和双字符存为字典
        2. 循环判断，for循环依次遍历两个字典（先双后单）判断k是否在s里，如果在则求和并将对应字符替换为空
        3. 当s为空则返回count
        """

        roman_single = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_double = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        count = 0
        while s:
            for k, v in roman_double.items():
                if k in s:
                    count += s.count(k) * v
                    s = s.replace(k, '')
            for k, v in roman_single.items():
                if k in s:
                    count += s.count(k) * v
                    s = s.replace(k, '')
        else:
            return count

    def romanToInt2(self, s):
        """by other
        """
        x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        y = 0
        for i in range(len(s)):
            if i < len(s) - 1 and x[s[i]] < x[s[i+1]]:
                y -= x[s[i]]
            else:
                y += x[s[i]]
        return y


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MCMXCIV'))







