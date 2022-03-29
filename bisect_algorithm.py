import bisect

a = [33, 99, 77, 70, 89, 90, 100]
c = 'FDCBA'
answer = []

for i in a:
    b = bisect.bisect([60,70,80,90],i)
    grade = c[b]
    answer.append(grade)

print(answer)