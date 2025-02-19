# 18/2--------task

# 17. Finding the frequency of elements in an array.
    # arr = [10, 30, 10, 20, 10, 20, 30, 10]  O/p: 10=> 4 30 =>2  20=> 2


arr = [10, 30, 10, 20, 10, 20, 30, 10]
frequency = {}

for element in arr:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

for key, value in frequency.items():
    print(f'{key} => {value}')


# 19.check if array is subset of another array or not .if the arr2 contains elements which are there in arr1 then it is a subset of an array.
# arr1=[1,3,4,5,2]
# arr2=[2,4,3,1,7.5.15]
# output: arr1 is subset of arr2
# Print arr2 is subset or not subset of arr1
# let arr1=[2,21,5,7,3,5,7,3,1,6,14,44];
# let arr2=[7,3,1];


def is_subset(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return set2.issubset(set1)

arr1 = [2, 21, 5, 7, 3, 5, 7, 3, 1, 6, 14, 44]
arr2 = [7, 3, 1]

if is_subset(arr1, arr2):
    print("arr2 is a subset of arr1")
else:
    print("arr2 is not a subset of arr1")


# Wap to concate all duplicate numbers in an array.
# Input:[10, 30, 10, 20, 10, 20, 30, 10]  

arr = [10, 30, 10, 20, 10, 20, 30, 10]
sum_of_duplicates = 0
frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num, count in frequency.items():
    if count > 1:
        concatenated_number = int(str(num) * count)
        sum_of_duplicates += concatenated_number

print(sum_of_duplicates)

# 10101010 + 3030 + 2020 = 10101010 + 3030 + 2020 = 10106060

# 10. Wap to concate all duplicate numbers in an array.
# Input:[23,33,200,785]       Output:30


arr = [23, 33, 200, 785]
sum_of_duplicates = 0
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for num, count in freq.items():
    if count > 1:
        concatenated_number = int(str(num) * count)
        sum_of_duplicates += concatenated_number

print(sum_of_duplicates)

# 20) Wap to print the number of pairs formed by the array of elements
#  Input: 10 20 10 30 20 20	  Output: 2 pairs
#  Input: 30 50 30 50 20 50 50 20 50 50    Output : 5 pairs

def count_pairs(arr):
    frequency = {}
    pairs = 0

    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    for count in frequency.values():
        pairs += count // 2

    return pairs

arr1 = [10, 20, 10, 30, 20, 20]
arr2 = [30, 50, 30, 50, 20, 50, 50, 20, 50, 50]

print(f'Output: {count_pairs(arr1)} pairs') 
print(f'Output: {count_pairs(arr2)} pairs')