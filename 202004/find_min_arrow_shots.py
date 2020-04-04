#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: Ssfanli
@Time  : 2020/04/04 1:19 下午
@Desc  : 452. 用最少数量的箭引爆气球
"""
"""题目
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。
一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons
"""


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        # init arrow
        arrow = 1
        # 思路
        # 按照sublist end排序，依次比较其余各子列表x_start和first_list_end
        # 如果x_start > first_list_end，arrow + 1，first_list_end更新为x_end
        points.sort(key=lambda x: x[-1])
        first_list_end = points[0][-1]
        for x_start, x_end in points[1:]:
            if x_start > first_list_end:
                arrow += 1
                first_list_end = x_end

        return arrow


if __name__ == '__main__':
    ipt = [[10, 16], [2, 8], [1, 6], [7, 12], [0, 3], [-1, 5], [100, 200]]
    sol = Solution()
    res = sol.findMinArrowShots(ipt)
    print(res)

