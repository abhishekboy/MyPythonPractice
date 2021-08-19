odd='This is an odd number'
even='This is an even number'
#Here Print * 80 will only be executed inside for condition
for i in range (1,100):
    if i%2==0:
        print(even)
    else :
        print(odd)
print('*'*80)
'''Here Print * 80 will only be executed inside if condition'''
for i in range (1,100):
    if i%2==0:
        print(even)
    else :
        print(odd)
    print('*'*80)
#Here Print * 80 will only be executed inside else condition
for i in range (1,100):
    if i%2==0:
        print(even)
    else :
        print(odd)
        print('*'*80)