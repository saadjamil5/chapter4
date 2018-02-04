print("Ex:4-3")
for value in range(0,21):
    print(value)


print("Ex:4-4")
for value in range(1,1000000):
    print(value)

print("Ex:4-6")
odd_numbers=list(range(1,20,2))
print(odd_numbers)


print("Ex:4-10")
food=['bbq','afghani','chicken','mutton']
print(food)
print(food[0:3])
print(food[1:3])
print(food[1:4])

print("Ex:4-11")
my_pizza=['bbq','afghani','chicken','mutton']
friend_pizzas=['bbq','afghani','chicken','mutton']
my_pizza.append('tandoori')
print(my_pizza)
friend_pizzas.append('creamy')
print(friend_pizzas)
for list1 in my_pizza:
    list1=my_pizza
print('My Favourite pizzas are')
print (list1)
for list2 in friend_pizzas:
    list2=friend_pizzas
print('My friend favourite pizzas are ')
print(list2)