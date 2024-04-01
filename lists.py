fruits_sam=["apple","carrot","banana","pineapple"]
fav=(1,8,90)
fruits_sam.append('guava')
fruits_sam.extend(fav)
fruits_sam.remove('banana')
#remove a value from list

fruits_sam.pop(1)
#remove a value from list as (index) we mentioned earlier in the paranthesis if we don't mention the specific inex then lst elemet will be popped out

fruits_sam.insert(0,'farooqi')
#insert the 2nd argument as a value to the list in the place of 1st argument(index before we add it)
print(fruits_sam)


collection=[199,667,78,56]
collection.sort()#sort values in the list indefault values sorted by ascending or alphabetical 
print(collection)

print(collection.index(199))#find the position of the value in collection list

collection.sort(reverse=True)#to sort descnding use argument (reverse=True)
print(collection)
