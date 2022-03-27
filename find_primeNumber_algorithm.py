# a = 100

# answer=[]

# x = [1]*(a+1)
# x[1] = 0

# for i in range(2,a):
#     if x[i] == 1:
#         j = 2
#         while i*j<=a:
#             x[i * j] = 0
#             j += 1

# for i in range(2,a+1):
#     if x[i] == 1:
#         answer.append(i)

# print(answer)

a = 100
answer = []

def isPrime(a):
    if a <= 3:
        if a == 2 or a == 3:
            return True
        else:
            return False
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return False
    return True
