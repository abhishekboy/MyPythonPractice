odd='This is an odd number'
even='This is an even number'
try:
    for i in range (1,5.8):
        if i%2==0:
            print('inside first loop:'+ str(i))
            for i in range (1,3):
                print('inside second loop')
                print(even)
        else :
            print(odd)
    print('*'*80)
except:
    print('There is an error in program')
finally:
    print('Program is finished')


try:
    for i in range (1,10):
        if i%2==0:
            raise Exception("Unknown Error")
            print('inside first loop:'+ str(i))
            for i in range (1,3):
                print('inside second loop')
                print(even)
        else :
            print(odd)
    print('*'*80)
except Exception as e:
    print('There is an error in program ' +str(e))

finally:
    print('Program is finished')