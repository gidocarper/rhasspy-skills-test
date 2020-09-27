import vlc
import threading, json, os

class Radio:
    def __init__(self, config):
        self.radio_station_url = ''
        self.radio_station_name = ''
        self.backgroundthread = None
        self.config = config
        self.language = config["config"]['setup']['language']
        self.messages = config["language"]
        self.noErrors = True
        self.instance = None
        self.player = None
        self.radio_station_list = None
        self.init_radio()

    def init_radio(self):
        try:
            radio_stations_list_file = open(os.path.dirname(__file__) + '/radio_station_' + self.language + '.json')
            self.radio_station_list = json.load(radio_stations_list_file)
            radio_stations_list_file.close()
        except:
            self.noErrors = False

        self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
        self.player = self.instance.media_player_new()


    def play_radio_station(self, radio_station):
        # to prevent that a thread is still runnning stop the radio
        self.stop_radio()

        if len(self.radio_station_list) == 0:
            self.noErrors = False
            return self.messages["Radio"]["error_radio_station_list"]

        i = 0
        while i < len(self.radio_station_list) -1:
            radio_station_url = self.radio_station_list[i]['url']
            radio_station_name = ' ' + self.radio_station_list[i]['name'].lower()
            i += 1

            if radio_station_name.find(radio_station.lower()) > 0:
                self.radio_station_url = radio_station_url
                self.radio_station_name = radio_station_name
                self.play_radio()
                return self.messages["Radio"]["playing"].format(self.radio_station_name)

        return self.messages["Radio"]["error_radio_station_not_found"]

    def play_radio(self):
        if self.noErrors:
            self.backgroundthread = None
            self.backgroundthread = threading.Thread(target=self.playingRadio)
            self.backgroundthread.start()

    def stop_radio(self):
        # it might be that there is no radio running
        try:
            self.player.stop()
        except:
            print("radio not started yet")

        self.radio_station_url = None
        self.radio_station_name = None
        self.backgroundthread = None
        return ''

    def playingRadio(self):
        if self.radio_station_url:
            radio_station_url = self.radio_station_url
        else:
            radio_station_url = 'http://stream.sunshine-live.de/house/mp3-192'

        media = self.instance.media_new(radio_station_url)
        self.player.set_media(media)
        self.player.play()
