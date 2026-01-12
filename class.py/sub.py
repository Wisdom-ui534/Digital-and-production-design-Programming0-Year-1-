import matplotlib.pyplot as plt
import numpy as np

import kagglehub

# Download latest version
path = kagglehub.dataset_download("michaelacorley/disability-statistics-united-states-2018")

print("Path to dataset files:", path)

x = [1, 2,]
y = [2, 4,]

plt.plot(x, y)
#plt.show()


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

#plt.show()


x = ([0.00, 0.02,0.04,0.06,0.08,0.10,0.12,0.14,0.16])
y = (["White", "Black", "Alaska native", "Asian", "Native Hawaiian, ", "Other", "Two or more races", "White(Not  Hispanic or LAtino)", "Hispanic or latino "])
def menu():
     Welcome = input("""
                    [1]. Line chart
                    [2]. Histogram
                    [3]. Quit     
                    """)
     if Welcome == "1":
        Line_chart()

        menu()
     elif Welcome == "2":
        Histogram()
        menu()
     elif Welcome == "3":
         print("Exiting the terminal...")

def Line_chart():
    plt.plot(x,y)
    plt.show()
    





def Histogram():
    plt.hist(x,y)
    plt.show()


menu()
   


        

