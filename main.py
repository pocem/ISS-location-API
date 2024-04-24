import requests
import smtplib
import datetime
import time

MY_LAT = 999
MY_LNG = 999

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_lng = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
print(f"Current longitude of ISS {iss_lng}")
print(f"Current latitude of ISS {iss_lat}")

response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

my_mail = "@gmail.com"
password = "relu pkyk hpkl ctbz"

time_now = datetime.datetime.now().hour



def in_range():
    if iss_lng in range(7, 17) and iss_lat in range(50, 60):
        return True

def is_night():
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if in_range() and is_night():

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)

            connection.sendmail(from_addr=my_mail, to_addrs=f"{my_mail}",
                                msg=f"Subject: ISS\n\nGO CHECK OUT THE SKY ISS IS ABOVE YOU")