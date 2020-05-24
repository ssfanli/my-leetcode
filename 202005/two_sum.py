#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: Ssfanli
@Time  : 2020/05/24 12:06 下午
@Desc  : 1. 两数之和
"""

from typing import List


"""topic
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """:keyword

        example:
        l = [2, 3, 5, 10]
        i loop in l[0: len(l) - 1] => [2, 3, 5]
        j loop in l[i + 1: len(l)] => when i ==2 and j in [3, 5, 10]
        """
        l = len(nums)
        for i in range(l - 1):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':

    ipt = [_ for _ in range(20)]
    t = 35
    sol = Solution()
    print(sol.twoSum(ipt, t))