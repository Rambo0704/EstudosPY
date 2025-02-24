imp
def main():
    nums = [3, 5, 1, 2, 6, 4]
    nums_ordenados = []

    while nums:
        menor = nums[0]
        for num in nums:
            if num < menor:
                menor = num
    
    
    print(menor)

main()
