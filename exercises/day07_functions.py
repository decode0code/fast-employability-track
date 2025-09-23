def square(x):
    return x**2
print(square(5))
print(square(-3))
print(square(20))
# This function takes a numb
# 
#
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(5))  


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))  
print(factorial(7))  

def max_in_list(numbers):
    return max(numbers)
nums = [4, 7, 1, 9, 3]
print(max_in_list(nums))  

def max_in_list_manual(numbers):
    max_num = numbers[0]  # start with first element
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(max_in_list_manual([4, 7, 1,50, 9, 3]))  
print(max_in_list_manual([-10, -3, -25, -1]))      

