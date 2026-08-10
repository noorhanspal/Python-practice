list=[20,77,88,24,99,100]
largest=list[0]
second_largest=list[0]
for i in list:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i
print("The second largest number is:",second_largest)
   