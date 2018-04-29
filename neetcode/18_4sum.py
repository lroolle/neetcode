""" 4Sum

> Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

- Note:

The solution set must not contain duplicate quadruplets.

- Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""


def solution(nums, target):
    nums.sort()
    ret = list()

    for i, x in enumerate(nums):
        for y in nums[i+1:]:
            tmp = set()
            for z in nums[i+2:]:
                if not z in tmp:
                    tmp.add(target - x - y - z)
                else:
                    _ret = sorted([x, y, target - x - y - z, z])
                    if not _ret in ret:
                        ret.append(_ret)
    return ret


def solution1(nums, target):
    import itertools
    ret = list()
    p = itertools.permutations(nums, 4)
    for item in p:
        item = sorted(item)
        if sum(item) == target and item not in ret:
            ret.append(item)
    return ret


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    print(solution(nums, 0))
    nums = [-2,1,6,-2,0,4,-8,7,-3,4,5,0,-4]
    print(solution1(nums, 0))

