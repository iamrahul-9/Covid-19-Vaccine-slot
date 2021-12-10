import requests

pincode = "0"
while len(pincode) !=6:
    pincode = input("Enter the pincode for which you want the status: ")
    if len(pincode) < 6:
        print(f"Pincode is shorter than the actual length")
    elif len(pincode) > 6:
        print(f"Pincode is longer than the actual length")

req_date = input("Enter the Date to get status (Date format: DD-MM-YYYY): ")

url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={req_date}"
header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}
response = requests.get(url, headers=header)
data = response.json()

total_centers = len(data["centers"])
print()
print("                        *>>>>>>    RESULTS   <<<<<<<*                                ")
print("-------------------------------------------------------------------------------------")
print(f"Date: {req_date} | Pincode: {pincode} ")

if total_centers != 0:
    print(f"Total centers in your area is: {total_centers}")
else:
    print(f"Unfortunately !! Seems like no center in this area / Kindly re-check the Pincode")

print("-------------------------------------------------------------------------------------")
print()

for i in range(total_centers):
    print(f"[{i+1}] Center Name:", data["centers"][i]["name"])
    vac_fee = data["centers"][i]["fee_type"]
    print("-------------------------------------------------------------------------------------")
    print ("   Date      Vaccine Type    Vaccine Fee   Minimum Age    Available ")
    print ("  ------     -------------   -----------   ------------   ----------")
    this_session = data["centers"][i]["sessions"]

    for j in range(len(this_session)):
        print("{0:^12} {1:^12} {2:^13} {3:^14} {4:^16}".format(this_session[j]["date"],this_session[j]["vaccine"],vac_fee,this_session[j]["min_age_limit"],this_session[j]["available_capacity"]))
    print()