#Data_Staructures or Core Data Types
#List
#List is a collection which is ordered and changeable. Allows duplicate members.
'''a=[1,2,3,5,4,5,6,7,8,9,8,'apple','banana','cherry']
print(a)
#accessing list items
print(a[0]) #first item
print(a[3]) #fourth item
print(a[-1]) #last item
print(a[-2]) #second last item
#slicing the list
print(a[0:5]) #first five items
print(a[5:10]) #items from index 5 to 10
print(a[10:13]) #items from index 10 to 13

# List allow duplicate members and alos any data type
# List functions

#append() is used to add an item to the end of the list.
a.append('grape')
print(a)
#extend() is used to add all the items of an iterable to the end of the list.
a.extend(['orange','kiwi'])
print(a)
#insert() is used to add an item at a specified index in the list.
a.insert(1,'mango')
print(a)
#index() is used to find the index of the first occurrence of a specified value in the list. It returns the index of the first occurrence of the value, or raises a ValueError if the value is not found.   
print(a.index(8))
#count() is used to count the number of occurrences of a specified value in the list.
print(a.count(8))
#pop()is used to remove and return the last item in a list[LIFO]
print(a.pop())
print(a)
#copy()is used to create a shallow copy of a list. 
b=a.copy()
print(b)# it is copy of a
print(a)
#remove() is used to remove the first occurrence of a specified value from the list
a.remove(5)
print(a)
#clear() is used to remove all the elements of a list
a.clear()
print(a)'''

#Tuple()
#maintain order of values
#its allow duplicates values
#its allow anydata types
'''b=('a','b','c','c','d',1)
print(b)
#store single 
c=10,
print(type(c))
#using constracter
a1=[1,2,3,4]
b1=tuple([a1])
print(type(b1))'''

#set{}
#doesn't maintain order
#doesn't allow duplicates valuse
#allow any data types
'''d={1,2,3,4,'apple'}
print(d)
d1={1}#store single values
print(type(d1))'''

#Dictionary
#its stored in values in key values pair
'''e={'name':'sathana','age':19}
print(e)# its maintain orders
e1={'name1':'sathana','name2':'sathana','age':19}#its allow duplicate values in values
#not allowed in keys
print(e1)'''

#quiz 1:Count how many even and odd numbers are present in a list.
'''def count_even_odd(number):
    even=0
    odd=0
    for i in number:
        if i%2==0:
            even+=1
        else:
            odd+=1

    print('even:',even)
    print('odd:',odd)    
a=[1,2,3,4,5,6,7,8,9]
count_even_odd(a)'''

#quiz 2:Remove duplicate elements from a list.
'''def remove_duplicates(numbers):
    unique_list = list(set(numbers))
    return unique_list

# Example
nums = [1, 2, 3, 2, 4, 5, 1, 6]
result = remove_duplicates(nums)

print("List after removing duplicates:", result)'''

#quiz 3:
'''def reverse_list(numbers):
    return numbers[::-1]
nums = [1, 2, 3, 4, 5]
print(reverse_list(nums))'''

#quiz 4:
'''def check_element(numbers, element):
    if element in numbers:
        print("Element exists in the list")
    else:
        print("Element does not exist in the list")


nums = [10, 20, 30, 40, 50]
check_element(nums, 30)'''

#quiz 5:Find the second largest element in a list.
'''def second_largest(numbers):
    numbers = list(set(numbers))  # Remove duplicates
    numbers.sort()
    return numbers[-2]
nums = [10, 20, 4, 45, 99]
print("Second largest element:", second_largest(nums))'''

#quiz 6:
'''def merge_lists(list1, list2):
    return list1 + list2


list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = merge_lists(list1, list2)
print(result)'''
#Quiz 7:
'''def sort_list(numbers):
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)

    print("Ascending Order:", ascending)
    print("Descending Order:", descending)


nums = [5, 2, 9, 1, 7]

sort_list(nums)'''
#quiz 8:
def square_list(numbers):
    squares = []

    for num in numbers:
        squares.append(num ** 2)

    return squares

# Example
nums = [1, 2, 3, 4, 5]
print(square_list(nums))


    
