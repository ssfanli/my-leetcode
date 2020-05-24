#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: Ssfanli
@Time  : 2020/05/24 12:26 下午
@Desc  : 7. 整数反转
"""


class Solution:
    """other

    class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        rev_x = strx[::-1]
        if x < 0:
            rev_x = rev_x[-1] + rev_x[:-1]
        rev_x = int(rev_x)
        return rev_x if -2**31 < rev_x < 2**31 - 1 else 0

    """
    def reverse(self, x: int) -> int:

        range_min = -2**31
        range_max = 2**31 - 1

        if x == 0:
            return 0
        if x > 0:
            reverse_str = str(x)[:: -1]
            reverse_int = int(reverse_str)
            if range_min <= reverse_int <= range_max:
                return reverse_int
            else:
                return 0
        if x < 0:
            reverse_str = str(x)[1:][::-1]
            reverse_int = 0 - int(reverse_str)
            if range_min <= reverse_int <= range_max:
                return reverse_int
            else:
                return 0

    def reverse2(self, x: int) -> int:
        """:keyword

        运行时间最短，巧妙的运用while循环
        ipt = 123

        3 => ipt % 10
        计算结果 => res * 10 + tmp
        剔除末尾 => abs_x // 10

        while loop
        """
        res = 0
        abs_x = abs(x)

        while abs_x != 0:
            tmp = abs_x % 10
            res = res * 10 + tmp
            abs_x = abs_x // 10

        if x >= 0:
            return res if res <= 2**32 - 1 else 0
        else:
            return -res if -res >= -2**32 else 0


if __name__ == '__main__':
    sol = Solution()
    res = sol.reverse2(234444444444444)
    print(res)



