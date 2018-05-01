""" 645 Set Mismatch

> The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

> Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

- Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

- Note:

    - The given array size will in the range [2, 10000].
    - The given array's numbers won't have any order.

"""


def find_error_nums(nums):
    n, x, seen = 1, 1, set()
    for i, item in enumerate(nums):
        if i + 1 not in nums:
            x = i + 1
        if item in seen:
            n = item
        else:
            seen.add(item)
    return [n, x]


def find_error_nums_by_sum(nums):
    delta = sum(set(nums))
    n = len(nums)
    return [sum(nums) - delta, n * (n + 1) // 2 - delta]


if __name__ == '__main__':
    nums = [1, 2, 2, 4]
    print(find_error_nums(nums))

