print("Demonstartion of list")

#Data : Heterogeneous
#ordered: Yes
#Indexed : Yes
#Mutable :Yes
#Duplicate :Yes

data=[11,21,51,101,21,11]     #duplicate
data1=[11,90.8,True,"Hello"]  # Heterogeneous


print("Data is Hetegogeneous:",data1)
print("Data is ordered:",data1)
print("Data at index 2:",data1[2])
print("Data with duplicate elements : ",data)

print("List is mutable")
data.append(201)
print("Data after append: ",data)
data.pop()
print("Data after pop : ",data)


