import csv

import pandas as pandas
import requests
from math import sin, cos, sqrt, atan2, radians


class ParkingService():

    def __init__(self):
        pass

    def get_parking_lots(self, longitude, latitude):
        parking_info = self.get_parking_info(longitude=longitude, latitude=latitude)
        parking_lots = parking_info["result"]
        lots = []
        col_list = ["Longitude", "Latitude"]
        csv_data = pandas.read_csv('/Users/saifkotwal/Documents/inrix/flaskserver/service/Crime Data.csv',
                                   usecols=col_list)
        for lot in parking_lots:
            lat = lot['peps'][0]['pepPt'][1]
            lon = lot['peps'][0]['pepPt'][0]
            score = self.calculate_safety_score(
                        latitude=lat, longitude=lon, csv_data=csv_data
                    )
            category = self.get_category(score)
            lots.append({
                "street": lot["name"],
                "spaces": lot["spacesTotal"],
                "point": {
                    "lat": lat,
                    "lon": lon
                },
                "safety": {
                    "score": score,
                    "category": category
                }
            })
        return {
            "parkings": lots
        }


    def get_parking_info(self, longitude, latitude):
        token = self.get_auth()
        headers = {
            'Authorization': 'Bearer {}'.format(token)
        }
        response = requests.get(
            url="https://api.iq.inrix.com/lots/v3?point={}%7C{}&radius=300".format(latitude, longitude),
            headers=headers
        )
        response = response.json()
        return response

    def get_auth(self):
        response = requests.get("https://api.iq.inrix.com/auth/v1/appToken?appId=ypvefclmmk&hashToken=eXB2ZWZjbG1ta3xEOEpBcWVEQ3JINkZBOW83bUZndlM3aE9JNVBjeUU3YzJndDg5M0Fr")
        response = response.json()
        return (response.get("result", {}) or {}).get("token", "") or ""


    def calculate_safety_score(self, longitude, latitude, csv_data):
        R = 3961
        # lat = radians(latitude)
        # long = radians(longitude)
        # sum = 0
        # count = 0
        # threshold_max = 365
        # threshold_min = 12
        #
        # with open('/Users/saifkotwal/Documents/inrix/flaskserver/service/Crime Data.csv', newline='') as csvfile:
        #     spamreader = csv.reader(csvfile)
        #     count = 0
        #     for row in spamreader:
        #         if not count:
        #             count+=1
        #             continue
        #         dlon = radians(float(row[0])) - long
        #         dlat = radians(float(row[1])) - lat
        #         a = sin(dlat / 2) ** 2 + cos(lat) * cos(float(row[1])) * sin(dlon / 2) ** 2
        #         c = 2 * atan2(sqrt(a), sqrt(1 - a))
        #         dist = R * c
        #         if dist <= 1:
        #             sum += dist
        #             count += 1
        #
        # if count >= threshold_max:
        #     return 0
        #
        # elif count <= threshold_min:
        #     return 100
        # else:
        #     num = count - threshold_min
        #     denom = threshold_max - threshold_min
        #     dangerscore = num / denom
        #     return (10.0 - dangerscore) * 10
        lat = radians(latitude)
        long = radians(longitude)
        sum = 0
        count = 0
        threshold_max = 1000
        threshold_min = 100
        for i in range(0, len(csv_data['Longitude'])):
            dlon = radians(csv_data['Longitude'][i]) - long
            dlat = radians(csv_data['Latitude'][i]) - lat
            a = sin(dlat / 2) ** 2 + cos(lat) * cos(csv_data['Latitude'][i]) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            dist = R * c
            if dist <= 1:
                sum += dist
                count += 1

        if count >= threshold_max:
            return 0
        elif count <= threshold_min:
            return 100
        else:
            num = count - threshold_min
            denom = threshold_max - threshold_min
            dangerscore = num / denom
            return (10.0 - dangerscore) * 10

    def get_category(self, score):
        if score <= 30:
            return "high"
        elif score >= 70:
            return "low"
        return "med"