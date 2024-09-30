# Rectify the code in each cell and explain the error in comments 

# Syntax Error
# print("python errors   
print("python errors")

#Key Error
# mydictionary = {True: "hello", False: "bye", '3': "python"}
# mydictionary['True'] 
mydictionnary={True:"hello",False:"bye", '3':"python"}
mydictionnary[True]

# indentation error 
# i = 14
# while i < 78:
# print(i)  
# i += 1
i=14
while i<78:
    print(i)
i+=1

# StopIteration
# it = iter([1, 2, 3])
# next(it)
# next(it)
# next(it)
# next(it)  
it=iter([1,2,3])
next(it)
next(it)
next(it)

# TypeError 
# 15 + '15' 
'15'+'15'

# ValueError
# int('python')   
print('python')

# NameError 
# print(language) 
name = "python"
print(name)

# ZeroDivisionError 
# x = 19 / 0  

try:
    x = 19 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")