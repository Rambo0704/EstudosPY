def main():
    nums = [0, 1, 0, 3, 12]
    zeros = [num for num in nums if num == 0]
    non_zeros = [num for num in nums if num != 0]
    nums = non_zeros + zeros
    print(nums)
main()