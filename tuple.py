print('Tuple')
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

dimensions1=[200,50]
dimensions1[0]=250
print(dimensions1)


dimensions2 = (200,50)
print("Original dimensions: ")
for dimension in dimensions2:
    print(dimension)


dimensions2=(400,100)
print("\nModified dimensions:")
for dimension1 in dimensions2:
    print(dimension1)