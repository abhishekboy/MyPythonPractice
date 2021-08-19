for i in range(1,13):
    print('number is {0} square is {1} cube is {2}' .format(i,i**2,i**3))
print('*'*80)
for i in range(1,13):
    print('number is {0:2} square is {1:3} cube is {2:4}' .format(i,i**2,i**3))
print('*' * 80)
for i in range(1, 13):
    print('number is {0:2} square is {1:<3} cube is {2:<4}'.format(i, i ** 2, i ** 3))


pi=22/7
print(pi)
print('value of pi is {0}'.format(pi))
print('value of pi is {0:12}'.format(pi))
print('value of pi is {0:12f}'.format(pi))
print('value of pi is {0:12.50f}'.format(pi))
print('value of pi is {0:52.50f}'.format(pi))
print('value of pi is {0:62.50f}'.format(pi))
print('value of pi is {0:62.53f}'.format(pi))
