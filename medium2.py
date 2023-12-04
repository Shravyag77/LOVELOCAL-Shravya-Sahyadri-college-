def majority_elements(nums):
    if not nums:
        return []

    candidate1, candidate2, count1, count2 = None, None, 0, 0

    for num in nums:
        # If the current number is a candidate, increment the count
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        # If one of the candidates' count reaches zero, update the candidate
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        # If none of the candidates' count is zero, decrement both counts
        else:
            count1 -= 1
            count2 -= 1

    # After the first pass, we have two potential candidates
    # Now, count their occurrences to verify if they appear more than ⌊ n/3 ⌋ times
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    n = len(nums)
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result

# Take input for nums
nums = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Call the function and print the result
result = majority_elements(nums)
print("Elements appearing more than ⌊ n/3 ⌋ times:", result)
