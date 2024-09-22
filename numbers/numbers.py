import random

n = ["random", "admin", "root", "shuffle"]


print(random.randrange(0,20,2))
print(random.randint(1, 30))

random.shuffle(n)
print(n)

random.seed(10)
print(random.random())

# print(random.getstate())

print(random.getrandbits(8))

print(random.choice(n))