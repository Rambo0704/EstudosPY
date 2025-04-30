def main():
    nums = [2, 1, 4, 3, 5]
    k = 10
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
          sum +=  nums[j]
          if sum * (j - i + 1)<k:
             count += 1
    print("Contagem final:", count)
main()
