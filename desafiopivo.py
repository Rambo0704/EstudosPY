def main():
    nums = [1,7,3,6,5,6]
    sum_left,sum_right = 0, sum(nums)
    for l,r in enumerate(nums):
        sum_right -= r
        if sum_left == sum_right:
            return l
        sum_left += r
    return -1
main()