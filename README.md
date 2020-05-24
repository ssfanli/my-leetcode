# my-leetcode
leetcode weekly

## 用最少数量的箭引爆气球/20200404

### Topic
> 在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。
一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

>来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons

### Example
```text
输入:[[10,16], [2,8], [1,6], [7,12]]
输出:2

解释:
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。
```
### Impl
[find_min_arrow_shots.py](https://github.com/ssfanli/my-leetcode/blob/master/202004/find_min_arrow_shots.py)

## 两数之和/20200524

### Topic

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### [Code](https://github.com/ssfanli/my-leetcode/blob/master/202005/two_sum.py)

```python
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
```

## 整数反转/20200524

### Topic

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0

### [Code](https://github.com/ssfanli/my-leetcode/blob/master/202005/reverse.py)

```python
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
```