fruits = {'apple', 'banana', 'orange'}

# print(fruits[0]) ---> İndekslenemez.

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango', 'grape', 'apple'])

fruits.remove('mango')
fruits.discard('apple')
fruits.pop()

fruits.clear()

print(fruits)

# myList = [1,2,5,5,4,2,1]

# print(set(myList))