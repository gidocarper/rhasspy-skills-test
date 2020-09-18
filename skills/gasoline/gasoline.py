#!/usr/bin/python3
# -*- coding: utf-8 -*-
# original code from https://github.com/hablijack  coverted and adapted to a rhasspy friendly environment by Gido Carper
# Gido also added 100 Cities with lantitude and longtitudes to be able to request gasoline prices in other cities

import requests, os, json



class Gasoline:

    def __init__(self, config):
        self.language = config["language"]
        self.config = config["config"]

    def setLanguage(self, intentMessage):
        self.language = intentMessage

    def find_city(self, city):
        citiesFile = open(os.path.dirname(os.path.abspath(__file__)) + '/cities.json')
        self.cities = json.load(citiesFile)
        citiesFile.close()

        i = 0
        while i < len(self.cities):
            json_city = self.cities[i]['city']
            lon = self.cities[i]['lon']
            lat = self.cities[i]['lat']
            i += 1
            if json_city.find(city) > 0 or city.lower() == json_city.lower():
                return {'city': json_city, 'longitude': lon, 'latitude': lat}

        return self.language["notFound"]


    def diesel_price(self, city):
        fuel_prices = self.get_fuelprices(city)
        response = ''

        if fuel_prices['status'] == 'ok':
            cheapest = {"diesel": 1000.0}
            for station in fuel_prices['stations']:
                if station['isOpen']:
                    if station['diesel'] <= cheapest['diesel']:
                        cheapest = station
                    response = self.language['diesel'].format(
                        format(cheapest["diesel"], '.2f').replace('.', ','),
                        cheapest["name"],
                        cheapest["street"].replace('str.', 'strasse'),
                        cheapest["houseNumber"],
                        cheapest["postCode"],
                        cheapest["place"]
            )
            return {"sentence": response.capitalize(),
                    "price": format(cheapest["e5"], '.2f').replace('.', ','),
                    "name": cheapest["name"],
                    "gasoline_type": "Diesel",
                    "address":{
                        "street": cheapest["street"],
                        "zipcode": cheapest["postCode"],
                        "city": cheapest["place"]}
                    }
        else:
            return  self.language['noInternet']

    def benzin_price(self, city):
        fuel_prices = self.get_fuelprices(city)
        response = ''
        print('fuel_prices',  fuel_prices)
        print(' fuel_prices[status]', fuel_prices['status'])
        if fuel_prices['status'] == 'ok':
            cheapest = {"e5": 1000.0}

            for station in fuel_prices['stations']:
                if station['isOpen']:
                    if station['e5']:
                        if station['e5'] < cheapest['e5']:
                            cheapest = station
                response = self.language['benzine'].format(
                    format(cheapest["e5"], '.2f').replace('.', ','),
                    cheapest["name"],
                    cheapest["street"].replace('str.', 'strasse'),
                    cheapest["houseNumber"],
                    cheapest["postCode"],
                    cheapest["place"]
            )
            return {"sentence": response.capitalize(),
                    "price": format(cheapest["e5"], '.2f').replace('.', ','),
                    "gasoline_type": "Benzin",
                    "name": cheapest["name"],
                    "address":{
                        "street": cheapest["street"],
                        "zipcode": cheapest["postCode"],
                        "city": cheapest["place"]}
                    }
        else:
            if fuel_prices['status'] == 'error':
               return {"sentence": self.language['error']}

        return {"sentence": self.language['noInternet']}


    def get_fuelprices(self, city):
        latitude = self.config['latitude']
        longitude = self.config['longitude']

        if city:
            city_config = self.find_city(city)

            if city_config['latitude']:
                latitude = city_config['latitude']
                longitude = city_config['longitude']
        print(' city', city)
        print(' latitude', latitude)
        print(' longitude', longitude)
        tankerkoenig_url = "{0}/json/list.php?lat={1}&lng={2}&rad={3}&sort={4}&type={5}&apikey={6}".format(
	       self.config['gasoline_base_url'],
            latitude,
            longitude,
            5,
            "dist",
            "all",
            self.config['tankerkoenig_api_key']
        )

        try:
            r = requests.get(tankerkoenig_url)
            json_obj = json.loads(r.content.decode('utf-8'))
            return json_obj
        except (requests.exceptions.ConnectionError, ValueError):
            print('error')
            return {"status": "error"}
