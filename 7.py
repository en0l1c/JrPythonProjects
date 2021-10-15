import requests
from time import sleep
import sys
url='https://api.nasa.gov/neo/rest/v1/feed?&api_key=ge7C4431vHE2TOtdGFD5zzRwOvINqreiGxfZETHy'

print("Connecting to NASA's API Server...\n")

response = requests.get(url)
print(response)


data = response.json()
total_elements = data['element_count']
#nearEarthObj = data['near_earth_objects']

#print(data["near_earth_objects"].keys())
print(f"Total Element Count: {total_elements}")
print("keys inside near_earth_objects:\n " + str(data['near_earth_objects'].keys()) + "\n------")


#print(data_all_dict['links'])
tmp = data['near_earth_objects']

# for dates in tmp['2021-10-12']:
#     # for key in dates.keys():
#     #     #print(key)
#     #     print("---")
#     print(dates["is_potentially_hazardous_asteroid"])

def printLoading(text):
    for c in text:
        print(c, end=''),
        sys.stdout.flush()
        sleep(0.5)

hazardous = 0 #counter to count total hazardous asteroids

print("Searching for hazardous objects: ")
total_velocities = []
total_diameters = []
for dates in data['near_earth_objects']: #pairnei tin kathe mera ksexwrista
    #print("\n--- Date: " + str(dates) + " ---")

    for each_date in tmp[dates]:
        #print(each_date["is_potentially_hazardous_asteroid"])
        if(each_date["is_potentially_hazardous_asteroid"] == True):
            hazardous += 1
        # print(each_date["close_approach_data"])

        #Maximum Diameter
        diameter = each_date['estimated_diameter']["kilometers"]["estimated_diameter_max"]
        total_diameters.append(float(diameter))
        #Maximum Velocity
        for each_daily_object in each_date["close_approach_data"]:
            
            #maximum velocity
            velocity = each_daily_object["relative_velocity"]["kilometers_per_second"]
            total_velocities.append(float(velocity)) #to kanoume float wste meta na mporoume na xrisimopoihsoume tin sunartisi max() gia na vroume to megisto tis listas

    printLoading('....')

max_velocity = max(total_velocities)
print(f"Maximum Velocity is: {max_velocity}")
print(f"Total hazardous: {hazardous}")
print("Est. maximum diameter : {}".format(max(total_diameters)))


