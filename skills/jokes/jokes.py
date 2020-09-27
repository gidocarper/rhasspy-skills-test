#!/usr/bin/python3
# -*- coding: utf-8 -*-
# original code from https://github.com/hablijack  coverted and adapted to a rhasspy friendly environment by Gido Carper
# Gido also added 100 Cities with lantitude and longtitudes to be able to request gasoline prices in other cities

import requests, os, json, random



class Jokes:

    def __init__(self, language):
        self.language = language
        return


    def tell_joke(self):
        random_joke = random.randint(0, 4)

        # Joke of the day Free https://jokes.one/api/joke/#python
        # you can only ask for 10 jokes per hours in the first joke api (which contains 3 different categories)
        # you can get a 10$/month authentication key though
        if random_joke == 2:
            joke_url = 'https://api.jokes.one/jod?category=animal'
            joke = self.get_jokes(joke_url)
            try:
                return joke["contents"]["jokes"][0]["joke"]["text"]
            except Exception as ex:
                random_joke = random.randint(0, 1)

        if random_joke == 3:
            joke_url = 'https://api.jokes.one/jod?category=blonde'
            joke = self.get_jokes(joke_url)
            try:
                return joke["contents"]["jokes"][0]["joke"]["text"]
            except Exception as ex:
                random_joke = random.randint(0, 1)

        if random_joke == 4:
            joke_url = 'https://api.jokes.one/jod?category=knock-knock'
            joke = self.get_jokes(joke_url)
            try:
                return joke["contents"]["jokes"][0]["joke"]["text"]
            except Exception as ex:
                random_joke = random.randint(0, 1)


        if random_joke == 0:
            joke_url = 'https://api.chucknorris.io/jokes/random'
            joke = self.get_jokes(joke_url)

            if joke['value']:
                return joke['value']

        if random_joke == 1:
            joke_url = 'https://official-joke-api.appspot.com/random_joke'
            joke = self.get_jokes(joke_url)

            if joke["setup"]:
                print(joke["setup"] + '. ' + joke["punchline"])
                return joke["setup"] + '. ' + joke["punchline"]


        return self.language['noInternet']

    def get_jokes(self, joke_url):
        try:
            r = requests.get(joke_url)
            json_obj = json.loads(r.content.decode('utf-8'))
            return json_obj
        except (requests.exceptions.ConnectionError, ValueError):
            return self.language['noInternet']
