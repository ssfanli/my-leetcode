#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: Ssfanli
@Time  : 2020/06/21 11:38 上午
@Desc  : 判断回文数（121, 232, ...）
"""


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

    def isPalindrome2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    s = Solution()
    num = [-12, 0, 3, 10, 20, 22, 99, 101, 123, 1234, 1221]
    for i in num:
        print(i, s.isPalindrome(i))
