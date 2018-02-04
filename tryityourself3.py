players5=['charles','martina','florence','eli']
print(players5[0:3])




players1=['charles','martina','florence','eli']
print(players1[1:3])


players2=['charles','martina','florence','eli']
print(players2[:4])

players3=['charles','martina','florence','eli']
print(players3[2:])

players4=['charles','martina','florence','eli']
print(players3[-3:])

print("Looping Through a Slice")
players=['charles','martina','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)


my_foods1=['pizza','falafel','carrot cake']
friend_foods1=my_foods1[:]
my_foods1.append('cannoli')
friend_foods1.append('ice cream')

print("My favourite foods are:")
print(my_foods1)

print("\nMy friend's favourite foods are:")
print(friend_foods1)
