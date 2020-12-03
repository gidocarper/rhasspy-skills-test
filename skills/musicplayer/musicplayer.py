#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fnmatch
from tinytag import TinyTag
import os, re, requests, sys
import os.path
from os import path
import json
import pygame
import threading, random
NEXT = pygame.USEREVENT + 1
os.environ["SDL_VIDEODRIVER"] = "dummy"

class MuuzikPlayer:
    def __init__(self, config, language):
        self.language = language["musicPlayer"]
        self.information_path = config["information_path"]
        self.pattern = '*.mp3'
        self.playlist = []
        self.artist_list = []
        self.song_list = []
        self.current_track = 0
        self.pathToMusic = config['music_path'].split("\n")
        self.musicFile = []
        self.backgroundthread = None
        self.train_thread = None
        self.running = False
        self.stopTheMusic = False

    def setLanguage(self, language):
        self.language = language

    def scanMusic(self):
        print('test 1')
        numberOfSongsBeforeScan = self.countMySongs()

        rootPaths = ['/home/pi/Music']
        songlist = []
        artistlist = []
        album_list = []
        titlelist = []
        genre_list = []
        pattern = '*.mp3'
        print(rootPaths)
        for rootPath in rootPaths:
            for root, dirs, files in os.walk(rootPath):
                for filename in fnmatch.filter(files, pattern):
                    if path.exists(os.path.join(root, filename)):
                        try:
                            audiofile = TinyTag.get(os.path.join(root, filename))
                            print(audiofile)
                            album = str(audiofile.album)
                            title = str(audiofile.title)
                            genre = str(audiofile.genre)
                            albumArtist = str(audiofile.albumartist)
                            artist = str(audiofile.artist)
                            year = str(audiofile.year)

                            a = albumArtist
                            print(a)
                            if albumArtist == 'None':
                                print(artist)
                                a = artist
                            if title.strip() != '' and title.strip() not in titlelist:
                                titlelist.append(title.strip())

                            if album.strip() != '' and album.strip() not in album_list:
                                album_list.append(album.strip())

                            if genre.strip() not in genre_list:
                                genre_list.append(genre)

                            # print(genre + ' ' + a + ' ' + title + ' ' + os.path.join(root, filename))

                            if (a.strip()) not in artistlist:
                                artistlist.append(a)

                            songlist.append({
                                'song': '{} {} {} {}  {} {}  {} '.format(album.strip(), title.strip(), genre, albumArtist, artist, year,
                                                                         os.path.join(root, filename)),
                                'path': os.path.join(root, filename),
                                'artist': '{}'.format(a),
                                'song_name': '{}'.format(title)
                            })
                        except:
                            print('error')


        with open(self.information_path + '/musicFound.json', 'w') as f:
            json.dump(songlist, f, indent=4)

        print('writing in root')
        with open('/root/.config/rhasspy/profiles/de/slots/music_artists', "w") as txt_file:
            for line in artistlist:
                txt_file.write(re.sub('[^a-zA-Z0-9 ]', '', line) + "\n")
        print('finisched writing in root')


        with open(self.information_path + '/music_artists.ini', "w") as txt_file:
            for line in artistlist:
                txt_file.write(re.sub('[^a-zA-Z0-9 ]', '', line) + "\n")

        with open('/root/.config/rhasspy/profiles/de/slots/music_titles', "w") as txt_file:
            for line in titlelist:
                txt_file.write(re.sub('[^a-zA-Z0-9 ]', '', line) + "\n")

        with open(self.information_path + '/music_titles.ini', "w") as txt_file:
            for line in titlelist:
                txt_file.write(re.sub('[^a-zA-Z0-9 ]', '', line) + "\n")


        with open('/root/.config/rhasspy/profiles/de/slots/music_albums', "w") as txt_file:
            for line in album_list:
                txt_file.write(re.sub('[^a-zA-Z0-9 ]', '', line) + "\n")

        with open(self.information_path + '/music_albums.ini', "w") as txt_file:
            for line in album_list:
                txt_file.write(re.sub('[^a-zA-Z0-9 ]', '', line) + "\n")


        with open('/root/.config/rhasspy/profiles/de/slots/music_genres', "w") as txt_file:
            for line in genre_list:
                txt_file.write(re.sub('[^a-zA-Z0-9 ]', '', line) + "\n")

        with open(self.information_path + '/music_genres.ini', "w") as txt_file:
            for line in genre_list:
                txt_file.write(re.sub('[^a-zA-Z0-9 ]', '', line) + "\n")

        numberOfSongsAfterScan = self.countMySongs()
        if (numberOfSongsAfterScan < numberOfSongsBeforeScan):
            print(' neue Lieder')
            text = self.language["removedSongs"].format(numberOfSongsBeforeScan - numberOfSongsAfterScan)
            self.train()
            return text

        if (numberOfSongsAfterScan > numberOfSongsBeforeScan):
            print(' keine neue Lieder')
            text = self.language["foundNewSongs"].format(numberOfSongsAfterScan - numberOfSongsBeforeScan)
            #self.train(hermes, intentMessage)
            return text

            #return self.language["scanningIsDone"]
        print(' ende Scanning')
        #self.train(hermes, intentMessage)
        #TODO add found artists to slot artists
        #TODO check which songs are new and only add these artists to the artists slot
        # self.train('', hermes, intentMessage)
        return self.language["scanningIsDone"]


    def train(self):
        print('TRAINING')
        # hermes.publish("rhasspy/asr/" + intentMessage["site_id"] + "/train")
        r = requests.post('http://rhasspy:12101/api/train')
        #hermes.publish("hermes/tts/say", json.dumps({"text": 'Ich trainiere jetzt', "siteId": intentMessage["site_id"]}))
        return r


    def playPlaylist(self, playListName):
        if  path.isdir(self.information_path + '/playlists') == False:
            os.mkdir(self.information_path + '/playlists')

        musicFile = open(self.information_path + '/playlists')
        allSongs= json.load(musicFile)
        musicFile.close()
        return len(allSongs)


    def addToFavourites(self, playListName):
        print(self)
        if self.running:
            song = self.playlist(self.current_track)
            playListPath = self.information_path + '/Favourites.m3u'
            if path.exists(playListPath) == False:
                file = open(playListPath, "w+")
                file.append()
            else:
                with open(playListPath, 'a') as file:
                    file.write(song)
            return self.language["addMp3ToPlaylist"]["songAddedToPlaylist"]
        else:
            return self.language["addMp3ToPlaylist"]["noMusicIsRunning"]


    def addMp3ToPlaylist(self, playListName):
        if self.running:
            song = self.playlist(self.current_track)
            playListPath = self.information_path + '/playlists' + playListName +'.m3u'
            if path.exists(playListPath) == False:
                file = open(playListPath, "w+")
                file.append()
            else:
                with open(playListPath, 'a') as file:
                    file.write(song)
            return self.language["addMp3ToPlaylist"]["songAddedToPlaylist"]
        else:
            return self.language["addMp3ToPlaylist"]["noMusicIsRunning"]


    def removeMp3ToPlaylist(self, song):
        song = self.playlist(self.current_track)
        return song

    def getMp3FilesFromPlaylist(self, pathToPlayList):
        songs = []
        with open(pathToPlayList) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline().lower()
                if (".mp3" in line):
                    songs.append(line)
                cnt += 1
        return songs

    def countMySongs(self):
        try:
            musicFile = open(self.information_path  + '/musicFound.json')
            allSongs= json.load(musicFile)
            musicFile.close()
            return len(allSongs)
        except:
            return 0

    def play(self, music):
        self.playlist = []
        print(music)

        if not str(os.path.exists(self.information_path + '/musicFound.json')):
            print('play Musik')
            self.scanMusic()

        if len(self.musicFile) == 0:
            musicFile = open(self.information_path + '/musicFound.json')
            self.musicFile = json.load(musicFile)
            musicFile.close()

        title = music["title"].lower()
        album = music["album"].lower()
        artist = music["artist"].lower()
        genre = music["genre"].lower()


        i = 0
        while i < len(self.musicFile) -1:
            path = self.musicFile[i]['path']
            artist_temp = self.musicFile[i]['artist'].lower()
            song_temp = self.musicFile[i]['song_name'].lower()

            song = ' ' + self.musicFile[i]['song'].lower()
            i += 1

            if song.find(artist) > 0 \
                    or song.find(album) > 0 \
                    or song.find(title) > 0 \
                    or song.find(genre) > 0:
                self.playlist.append(path)
                self.artist_list.append(artist_temp)
                print(' artist_temp', artist_temp)
                print(' song_temp', song_temp)
                self.song_list.append(song_temp)

        self.current_track = 0
        if len(self.playlist) == 0:
            return self.language["notFound"]
        else:
            return self.playSong()


    def next(self):
        self.stop()
        print(' self.current_track', self.current_track)
        if self.current_track < len(self.playlist) - 1:
            self.current_track += 1
            self.playSong()
            print('AFTER 1 self.current_track', self.current_track)
            return self.language['nextSong']
        else:
            self.current_track = 0
            self.stop()
            print('AFTER 2 self.current_track', self.current_track)
            return self.language['playListEnded']

    def previous(self):
        if self.current_track == 0:
            self.current_track = len(self.playlist) - 1
        else:
            self.current_track -= 1
        self.playSong()
        return self.language['previuosSong']

    #Not implemented yet
    def repeat(self):
        self.playSong()
        return 'okay ich wieder hole'

    def stop(self):
        self.running = False
        self.stopTheMusic = True
        try:
            pygame.mixer.music.stop()
            pygame.quit()
        except Exception as ex:
            print('error while stopping but that is fine')
        # pygame.mixer.set_endevent(type)
        self.backgroundthread = None
        return self.language['stoppedTheMusic']

    def play_music_with_stars(self, stars):
        star_list_file_name = self.information_path + '/' + str(stars) + '_stars_list.json'
        star_list_file = open(star_list_file_name)
        star_list_file_list = json.load(star_list_file)
        star_list_file.close()
        self.playlist = star_list_file_list
        self.playSong()
        return  self.language['startedPlaying']

    def add_stars(self, stars):
        artist = self.artist_list[self.current_track]
        print(artist)
        song = self.song_list[self.current_track]
        print(song)
        path = self.playlist[self.current_track]
        print(path)
        star_list_file_name = self.information_path + '/' + str(stars) + '_stars_list.json'

        if not os.path.exists(star_list_file_name):
            print('Make new File')
            star_list_file_list = []
        else:
            star_list_file = open(star_list_file_name)
            star_list_file_list = json.load(star_list_file)
            star_list_file.close()
            print('loading file')

        write_new_file = True
        i = 0
        print(' total in file' +  str(len(star_list_file_list)))
        while i < len(star_list_file_list):
            #artist = star_list_file_list[i]['artist']
            #song = star_list_file_list[i]['song']
            #path = star_list_file_list[i]['path']

            if path == star_list_file_list[i]['path']:
                print(' found file')
                write_new_file = False
            i += 1

        if write_new_file:
            star_list_file_list.append({
                "song": song,
                "artist": artist,
                "path": path
            })
            with open(star_list_file_name, 'w') as f:
                json.dump(star_list_file_list, f, indent=4)


        print(star_list_file_list)

        return self.language['addedStars'].format(str(stars))


    def what_is_playing(self):
        print(self.current_track)
        print(self.playlist[self.current_track])
        artist = self.artist_list[self.current_track]
        song = self.song_list[self.current_track]

        print(artist)
        print(song)

        return self.language['whatIsPlaying'].format(song, artist)



    def playSong(self):
        # I am sure this is not the right way to use a thread but I have no clue how to play the music while
        # continueing the other scripts
        self.backgroundthread = None
        self.backgroundthread = threading.Thread(target=self.playing)
        self.backgroundthread.start()
        return self.language['startedPlaying']

    def playing(self):
        self.stopTheMusic = False
        # start first track
        self.tracks_number = len(self.playlist)
        NEXT = pygame.USEREVENT + 1
        print(' self.current_track ')
        print(self.current_track)
        print(' self.playlist ')
        print(self.playlist)

        # get the right speed of each song
        audiofile = TinyTag.get(self.playlist[self.current_track])
        pygame.mixer.init(frequency=audiofile.samplerate)
        print('-------------------------------------------------------------------')
        # sometimes needed I dont know why but on my rasp 4 I dont need this line anymore
        #try:
            #screen = pygame.display.set_mode((400, 300))
       # except Exception as ex:
        #    print('error but that is fine')

        print('-------------------------------------------------------------------')
        print(self.playlist)
        # start first track
        if path.exists(self.playlist[self.current_track]):
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(NEXT)

            self.running = True

            while pygame.mixer.music.get_busy():
               nothing = True

            if self.stopTheMusic == False:
                self.next()
        else:
            self.stop()



 

