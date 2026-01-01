import pandas as pd
# s = pd.Series([10,20,30,40])
# print(s)

# data = {
#     "NAME" : ["deepak ", "mahanth","Aiman"],
#     "MARKS" : [67,78,89]
# }

# D = pd.DataFrame(data)
# print(D)

# s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# print(s)

#Series
# data ={"math":85,"science":90,"English":88}
# s = pd.Series(data)
# print(s)
# print(s["math"]) #aceesing the data
# # print(s[0])
# print(s.index)
# print(s.values)
# print(s.dtype)
# print(s.shape)

# s = pd.Series([10,20,30])
# print(s)

# s1 = pd.Series([10,20,30])
# s2 = pd.Series([1,2,3])
# print(s1+s2)
# print(s1*s2)

# s = pd.Series([10,25,30,5])
# print(s>20) #it gives the boolean values
# print(s[s>20]) #it gives the integer values

# s = pd.Series([10,None,30])
# print(s.isnull()) #it gives the boolean values
# print(s.fillna(0))# it gives the float values

# Task1:

# d = {"a":100,"b":200,"c":300}
# s = pd.Series(d)
# print(s)
# print(s+50) #task 2
# print(s>200)#task 3
# print(s.isnull)#task 4

# data = {
#     "name":["Deepak ","Rahul","Anita"],
#     "age":[20,21,22],
#     "marks":[85,90,88]
# }

# df = pd.DataFrame(data)
# print(df)

# print(df.shape)
# print(df.size)
# print(df.ndim)
# print(df.columns)
# print(df.index)
# print(df.head(2))
# print(df.tail())
# print(df.info())
# # print(df["name"])
# # print(df["name","age"])
# print(df.loc[0])

# task1:

data =[
    {"Name":"A","Marks":80,"Grade":"B"},
    {"Name":"B","Marks":90,"Grade":"A"},
    {"Name":"C","Marks":70,"Grade":"c"},
    
] 
df = pd.DataFrame(data)
print(df)
#task2
print(df.head(2))
print(df.info())

#task 3:
df["PASSED"]=["Yes","YES","NO"]
print(df)



