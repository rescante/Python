import random

# result = dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0
result = random.random() * 100
result = int(random.uniform(1,100))
result = random.randint(1,100)

greetings = 'Hello there!'
names = ['yağmur','ali','deniz','cenk']
# result = names[random.randint(0,len(names)-1)]

result = random.choice(names)
result = random.choice(greetings)

liste = list(range(10))
random.shuffle(liste)

result = liste

liste = range(100)
result = random.sample(liste, 3)

print(result)