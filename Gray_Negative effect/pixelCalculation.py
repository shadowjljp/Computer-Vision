result = {round(255*j/499.0) for j in range(500)}

print(len(result))
count =1
for x in result:
    print("Value in Set: {} and it is number {}".format(x,count))
    count=count+1