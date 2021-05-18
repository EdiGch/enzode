users = ('Grzegorz','Mateusz', 'Kamil', 'Łukasz', 'Krzysztof')
# print(users)
# perator dostępu [ ]
# print(users[0])
# print(users[1])
# print(users[4])
# print(users[-1])
# print(users[-2])
# print(users[-5])

# Wycinanie
#users[1:3]
# print(users[1:3])
# print(users[2:4])
# print(users[:3])
# print(users[2:])
# print(users[:-1])
# print(users[-2:])


# print(users[0:4:2])
# print(users[4:0:-1])
# print(users[::3])
# print(users[::-1])

# Len()

# testList = []
# print(testList, 'length is', len(testList))
#
# testList = [1, 2, 3]
# print(testList, 'length is', len(testList))
#
# testTuple = (1, 2, 3)
# print(testTuple, 'length is', len(testTuple))
#
# testRange = range(1, 10)
# print('Length of', testRange, 'is', len(testRange))

# [10,20,50,100,200]
# []
# list()
# print(len([10,20,50,100]))
# liczby = [10,20,30,50]
# print(liczby[2])
# print(100 in liczby)
# print(100 not in liczby)

# numery = [20,40,80,160]
# numery[0] = 10
# print(numery)
#
# liczby = [10,20,50,100]
# liczby.append(200)
# print(liczby)

# liczby = [10,20,50,100]
# liczby.insert(0,5)
# print(liczby)
#
# numery = [20,40,80,160]
# numery[1:3] = [1,2]
# print(numery)

liczby = {10,20,50,100, 10, 100}
print(liczby)
print(len(liczby))

a = {1,2,3}
b = {2,3,4}
print(a | b)
print(a - b)
print(a & b)
print(a ^ b)

liczby.add(200)
print(liczby)