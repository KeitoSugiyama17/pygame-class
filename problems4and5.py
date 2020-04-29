# problem 4
def find_min(arr):
    min = arr[0]
    n = len(arr)
    for i in range(0, n):
        if arr[i] < min:
            min = arr[i]
    print("This is the minimum:")
    return min

a = [325, 123, 21, 52, 789, 2, 32]
m = find_min(a)
print(m)

# problem 5

def find_sum(arr):
    sum = 0
    n = len(arr)
    for i in range (0, n):
        sum = arr[i] + sum
    return sum
def find_avr(arr):
    length = len(arr)
    sum = find_sum(arr)
    avr = sum / length
    print("This is the average:")
    return avr

a = [325, 123, 21, 52, 789, 2, 32]
m = find_avr(a)
print(m)
