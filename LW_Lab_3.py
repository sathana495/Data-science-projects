#Tuple()
#Tuple are immutable
#Tuple are ordered
#Tuple are allow duplicates
#Tuple are allow any data type
#Tuple are used to store multiple items in a single variable
#Tuple functions
#count() is used to count the number of occurrences of a specified value in a tuple.
a=(1,2,1,3,4,5,6,7,8,9,10)
print(a.count(1))

#index() is used to find the index of the first occurrence of a specified value in a tuple.
print(a.index(8))

#len() is used to find the length of a tuple.
print(len(a))

#max() is used to find the maximum value in a tuple.
print(max(a))

#min() is used to find the minimum value in a tuple.
print(min(a))   

#sum() is used to find the sum of all the elements in a tuple.
print(sum(a))

#sorted() is used to sort the elements of a tuple.
print(sorted(a))

#-----------------------------------------------------------------------------------------------------------------
#set{}
#Set is a collection which is unordered, unchangeable*, and unindexed.
#Set is allow any data type
#Set is allow duplicates
b={1,2,3,8,4,5}
b1=(1,2,3,4,5)
print(b)#it will remove the duplicates
#Set functions
 #add() is used to add an item to a set.
b.add(3)
print(b)
#clear() is used to remove all the elements from a set.
b.clear()
print(b)
#copy() is used to copy a set.
b.copy()
print(b)
#difference() is used to return a set containing the difference between two or more sets.
print(b.difference(b1))
#difference_update() is used to remove the items in this set that are also included in another set, specified as an argument.
b.difference_update(b1)
print(b)
print(b.intersection(b1))#it will return the common items between 2 sets
print(b.isdisjoint(b1))#it will return true if no items in set 1 is present in set 2
print(b.isdisjoint(b1))#it will return true if no items in set 2 is present in set 1
print(b.issuperset(b1))#it will return true if all items in set 1 are present in set 2
print(b.symmetric_difference(b1))#it will return a set that contains all items from both sets, except items that are present in both sets.
#b.symmetric_difference_update(b1)
print(b)
print(b.union(b1))#it will return a set that contains all items from both sets
print(b.issubset(b1))#it will return true if all items in set 2 are present in set 1
print(b1)
print(b)

#-------------------------------------------------------------------------------------------
#Dictionary{}
#Dictionary is a collection which is ordered, changeable and indexed.
#Dictionary is allow any data type
#Dictionary is allow duplicates in valuea not allowed in keys 
#Dictionary functions
a1={1:'apple',2:'banana',3:'cherry',4:'orange',5:'kiwi',6:'grape'}
print(a1.items())#it will return a view object that displays a list of dictionary's (key,value) tuple pairs.
print(a1.keys())#it will return a view object that displays a list of dictionary's keys.
print(a1.values())#it will return a view object that displays a list of dictionary's values.
print(a1.get(1))#it will return the value of the specified key
print(a1[1])#it will return the value of the specified key
a1.update({7:'mango'})#it will update the dictionary with the specified key-value pairs
print(a1)
print(a1.pop(1))#it will remove the item with the specified key name
print(a1)
print(a1.popitem())#it will remove the last inserted item (in versions before 3.7, a random item is removed instead)
print(a1)
a1.clear()#it will remove all the elements from the dictionary
print(a1)

#quiz 1 :Create a list with 5 numbers and print it.
list=[1,2,3,4,5]
print(list)

#quiz 2 :Add a new element to a list using append().
list.append(6)
print(list)

#quiz 3:Insert an element at index 2.
list.insert(2,'3')
print(list)

#quiz 4:Remove an element using remove()
list.remove(3)
print(list)

#quiz 5:Remove last element using pop().
print(list.pop())
print(list)

#quiz 6:Find the length of a list.
print(len(list))

#Access first and last element
print(list[::len(list)-1])

#Find maximum and minimum number.
list2=(1,2,3,4,5,6,7,7,7,7)
print(min(list2),max(list2))

#Find sum of all elements.
print(sum(list2))

#Count how many times a number appears
print(list2.count(7))



