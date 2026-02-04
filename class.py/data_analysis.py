def Task1():
    import pandas as pd 
    #load and explore the data
    #print the first  5 rows
    df =pd.read_csv('Animlas.csv')
    print(df.head())
    print(df.columns)
    print(df.info())



#Task1()


def Task2():
    import pandas as pd
    
    
    df = pd.read_csv("Animals.csv")
    
    
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    
    
    daily_avg = df.groupby("Date")[["Likes", "Shares", "Comments"]].mean()
    
    print("Total average  per day")
    print(daily_avg)
    #Work out which type of post receives the highest total interactions.
    df = pd.read_csv("Animals.csv")
    highest_interactions = df.groupby("Post Type")[["Likes", "Shares", "Comments"]].sum()
    highest_interactions["Total"] = highest_interactions["Likes"] + highest_interactions["Shares"] + highest_interactions["Comments"]
    highest_post_type = highest_interactions["Total"].idxmax()
    print("The post with the highest number of interactions: ", highest_post_type)
    print(highest_interactions)

    #Analyse how interactions change at different times of day.
    
#Task2()
def Task3():
    import pandas as pd
    import matplotlib.pyplot as plt

    
    df = pd.read_csv("Animals.csv")

    
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

    # If there's a Time column as string, combine with Date or convert to datetime
    # For simplicity, assume 'Time' column is HH:MM
    df["Time"] = pd.to_datetime(df["Time"], format="%H:%M").dt.hour  # extract hour

    # Calculate total interactions
    df["Total"] = df["Likes"] + df["Shares"] + df["Comments"]

    # Group by hour and sum interactions
    interactions_by_hour = df.groupby("Time")["Total"].sum()

    # Prepare x and y points for the line graph
    xpoint = interactions_by_hour.index  # hours 0-23
    ypoint = interactions_by_hour.values  # total interactions

    # Plot
    plt.figure(figsize=(10,5))
    plt.plot(xpoint, ypoint, marker='o', color='blue')
    plt.title("Total Interactions by Hour of Day")
    plt.xlabel("Hour of Day")
    plt.ylabel("Total Interactions")
    plt.xticks(range(0,24))  # show all hours
    plt.grid(True)
    plt.show()

Task3()

