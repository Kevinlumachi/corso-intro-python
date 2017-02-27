from funzioni import make_sum
numbers = [1, 5, 7, 123, 15, 6, 8]

for n in numbers:
    print n
    
count = 0
for n in numbers:
    print 'Elemento %s: %s' % (count, n)
    count +=1

numbers = []

for n in range(0, 10):
    numbers.append(make_sum(n, 2))

print numbers



