numbers = [1, 10, 7, 4, 18, 5]
letters = ['a','c','z','r','m','h']

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

numbers.append(49) # ---> En sona eleman ekler.
numbers.append(59)
numbers.insert(3, 78) # ---> Listenin herhangi bir yerine eleman ekler.
numbers.insert(-1, 52)

# numbers.pop() ---> Bir indeks numarası verilmezse listenin son elemanını siler.
# numbers.pop(0)
# numbers.pop(-1)
# numbers.remove(59)

numbers.sort()
numbers.reverse()

letters.sort()
letters.reverse()

print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(5))
print(letters.count('m'))

numbers.clear()
print(numbers)