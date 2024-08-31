#Question 1
#Write a Python program that multiplies all the items in a list.
#Sample list= [2, 3, 6]
#Result = 36
import math
Sample_list= [2, 3, 6]
print(math.prod(Sample_list))

#Question 2
#Write a Python program to get a list, sorted in increasing order by the last element in each tuple, from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
Sample_List = ([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
Sample_List.sort(key = lambda x:x[-1])
print(Sample_List)

#Question 3
#Write a Python program that combines two dictionaries by adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Expected result: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

CombinedDictionary = (d1 | d2)
print(CombinedDictionary)

#Question 5
#Write a program to sort a tuple by its float element.
#For example: list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
#Expected result: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
list.sort(reverse=True)
print(list)

#Question 6
#Write a Python program to create a set.
#Examples : {0, 1, 2, 3, 4}
#Write a Python program to iteration over sets.
#Write a Python program to add members in a set and to remove items from a given set.
# Write a Python program to create a set.
SampleSets = {0,1,2,3,4,5}
# Write a Python program to iteration over sets.
for SampleSet in SampleSets:
    print(SampleSet)
# Write a Python program to add members in a set
SampleSets.add("Micheal")
SampleSets.add("Thriller")
# and to remove items from a given set.
SampleSets.remove("Thriller")
print(SampleSets)
