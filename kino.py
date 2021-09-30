import requests
import json
#import pandas as pd
#from datetime import datetime

gameId = 1100 #1100 for kino
n = 750000 #apo auton ton arithmo drawid kai epeita emfanizontai data
cnt_draws=1
cnt_days=0
Day = 1
listOfAllWinNums = []

def most_frequent(listofAllWinNums):
    return max(set(listOfAllWinNums), key = listOfAllWinNums.count)


while n < 904534:
    url = "https://api.opap.gr/draws/v3.0/" + str(gameId) + "/" + str(n)
    response = requests.get(url).text

    parsed_data = json.loads(response)

    winning_numbers = parsed_data['winningNumbers']['list']
    #even_numbers = parsed_data['winningNumbers']['sidebets']['evenNumbers']
    #odd_numbers = parsed_data['winningNumbers']['sidebets']['oddNumbers']

    listOfAllWinNums.extend(winning_numbers) #ola ta winning numbers se mia lista

    if cnt_days == 192:
        cnt_days == 0
        Day += 1

    print("\n")
    print("Day " + str(Day) + ", Draw(" + str(cnt_draws) + "): ")
    print("winning Numbers:")
    print(winning_numbers)
    print("Sum of winning numbers is: " + str(sum(winning_numbers)) + "\nAverage is:" + str(sum(winning_numbers)/20))
    print("\n")

    print("Most Frequent Number until now: " + str(most_frequent(listOfAllWinNums)))
    #print("Even Numbers:")
    #print(even_numbers)
    #print("Odd Numbers:")
    #print(odd_numbers)
    print("\n")

    #pd.set_option("display.max_rows", None, "display.max_columns", None) #show all row
    if n >= 750020:
        break
    else:
        n += 1
        cnt_days += 1
        cnt_draws += 1
print(listOfAllWinNums)
