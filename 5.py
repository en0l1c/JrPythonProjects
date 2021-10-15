import requests 
from collections import Counter


url = 'https://qrng.anu.edu.au/API/jsonI.php?length=1000&type=uint8'

print("Conecting to ANU server and waiting for response...\n")
response = requests.get(url)

num_list = response.json()['data']


list1 = []
duplicates = [] #edw tha boun ta duplicates, oste na diaxwristoun argotera mesa stin for loop kai na min ksanatypwnontai kathe fora poy ta vriskei o compiler mesa stin lista
# print(type(nums))

for number in num_list:
    number = int(number)
    num_mod = number%20
    list1.append(num_mod)
    
    #print(num_mod)

print("--- Statistics ---")

for i in list1:
    cnt = list1.count(i)
    percent = cnt/len(list1)*100.0
    prec_percent = round(percent,2)#set precision till 2 decimal places

    if cnt == 1: #auta
        print(f'Number: {i}, appeared {cnt} times which means {prec_percent}%')

    elif cnt > 1:
        if i not in duplicates:
            duplicates.append(i)
            print(f'Number: {i}, appeared {cnt} times which means {prec_percent}%')
#print("Duplicates are {duplicates}")

    

#print(Counter(list1))

