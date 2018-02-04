print("Ex:4-1")
flavours=['tikka','bbq','supreme']
for flavour in flavours:
    print("I like"+" "+flavour.title()+" "+"pizza")
print("I really love pizza")

print("Ex:4-2")
Animals=['dog','cow','cat']
for Animal in Animals:
    print("A"+" "+Animal.title()+" "+"would make a great pet.")
print("Any of these animals would make a great pet!")


for value in range(1,6):
    print(value)


numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)

odd_numbers=list(range(1,11,2))
print(odd_numbers)


squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)


squares1=[]
for values in range(1,11):
    squares1.append(values**2)
print(squares1)


digits=[1,2,3,4,5,6,7,8,9,10]
print(min(digits))
print(max(digits))
print(sum(digits))

squares3=[value**2 for value in range(1,11)]
print(squares3)

