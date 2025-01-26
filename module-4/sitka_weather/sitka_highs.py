# Make the following changes to the sitka_highs.py program:
# Open the program with instructions on how to use the menu; Highs, Lows, or Exit.
# When the program starts, allow the user to select whether they want to see the high temperatures or the low temperatures, or to exit.
# When the user selects 'lows', they should see a graph, in blue, that reflects the lows for those dates.
# Allow the program to loop until the user selects exit.
# When the user exits, provide an exit message.
# Use what elements you can from previous programs, perhaps including sys to help the exit process.

import csv
from datetime import datetime

from matplotlib import pyplot as plt

def open_graph():
    choice = input("Enter 'highs' to see high temperatures, 'lows' to see low temperatures, or 'exit' to exit the program: ")
    if choice == "exit":
        print("Exiting...")
        exit()
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # Get dates and high temperatures from this file.
        if choice == "highs":
            dates, highs = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                high = int(row[5])
                highs.append(high)
        # Plot the high temperatures.
        #plt.style.use('seaborn')
            fig, ax = plt.subplots()
            ax.plot(dates, highs, c='red')

        # Format plot.
            plt.title("Daily high temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
            plt.show()
        elif choice == "lows":
            dates, lows = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                low = int(row[6])
                lows.append(low)
            fig, ax = plt.subplots()
            ax.plot(dates, lows, c='blue')
            plt.title("Daily low temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
            plt.show()
    exit()
    


open_graph()