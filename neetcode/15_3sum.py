""" 3Sum

> Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

- Note:

The solution set must not contain duplicate triplets.

- Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

import cProfile


def naive_solution(nums):
    size = len(nums)
    ret, added = list(), list()

    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                x, y, z = nums[i], nums[j], nums[k]
                idx = sorted((x, y, z))
                if x + y + z == 0 and idx not in added:
                    ret.append((x, y, z))
                    added.append(idx)
    return ret


def solution1(nums):
    nums.sort()
    ret = set()

    for i, x in enumerate(nums):
        if i >= 1 and nums[i - 1] == x:
            continue
        tmp = set()
        for y in nums[i + 1:]:
            if not y in tmp:
                tmp.add(-(x + y))
            else:
                ret.add((x, -(x+y), y))
    return ret


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4] * 100
    cProfile.run('print(solution1(nums))')
    cProfile.run('print(naive_solution(nums))')


