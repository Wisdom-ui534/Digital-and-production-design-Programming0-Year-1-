import pandas as pd 



data = {
    "Name" : ["Alex","Jamie", "Sam"],
    "Attendance" : [92, 85, 78],
    "Grade" : ["B", "C", "D"]

}




#Add  a new student 
data["Name"].append(str("Wisdom "))
data["Attendance"].append(int(97))
data["Grade"].append(str("A"))
#Add a new colounm 
data["Passed"] = ["Alex", "Wisdom ",  "Jamie", ""]
#change one attendace value 
print(data)

df = pd.DataFrame(data)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df)





#Activity 2 
df = pd.read_csv('students.csv')



print(df.to_string())

"""print(wf.head())
print(wf.info())"""

