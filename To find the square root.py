#To find the square root for positive numbers
print('To find the square root for positive numbers:')

num=int(input('Enter a number:'))
num_sqrt=num**0.5
print('The square root of %0.3f is %0.3f'%(num,num_sqrt))

'''__________________________________________________________'''


#To find the square root for real or complex numbers

import cmath
num=eval(input('Enter a complex number:'))
num_sqrt=cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))



'''________________________________________________________________'''
