fruits = ['apple', 'banana', 'pear', 'grape']

# ! for/else
for fruit in fruits:
    print(fruit)
else:
    print('All fruits were printed')

##############################################
for fruit in fruits:
    print(fruit)
    if len(fruit) < 5:
        break
else:
    print('All fruits were printed')

##############################################
# for fruit in fruits:
#     if fruit == 'peach':
#         break
# else:
#     raise ValueError('No peach found in fruits')


# ! while/else
n = 0
while n < 5:
    n += 1
    print(n)
else:
    print('n = 5')


# ! try/else
# * For illustration
try:
    dangerous_call()
except OSError:
    log('OSError...')
else:
    after_call()

