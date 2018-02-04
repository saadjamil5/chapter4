players=['charles','martina','micheal','florence','eli']
print(players[0:3])

players1=['charles','martina','micheal','florence','eli']
print(players1[1:3])


players2=['charles','martina','micheal','florence','eli']
print(players2[:4])


players3=['charles','martina','micheal','florence','eli']
print(players3[2:])


players4=['charles','martina','micheal','florence','eli']
print(players4[-3:])


players5=['charles','martina','micheal','florence','eli']
print("Here are the first three players on my team:")
for player5 in players5:
    print(player5.title())


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
print("My favorite foods are:")
print(my_foods1)
print("\nMy friend's favourite foods are:")
print(friend_foods1)