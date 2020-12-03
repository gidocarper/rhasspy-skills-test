import json, os
import io, configparser

from rhasspyhermes.nlu import NluIntent
from rhasspyhermes_app import EndSession, HermesApp

from musicplayer import MuuzikPlayer

app = HermesApp("MusicApp")

def read_configuration_file():
    try:
        cp = configparser.ConfigParser()
        print(os.getcwd() + "/" + os.path.dirname(__file__) + "/config.ini")
        with io.open(os.getcwd() + "/" + os.path.dirname(__file__) + "/config.ini", encoding="utf-8") as f:
            cp.read_file(f)
        return {section: {option_name: option for option_name, option in cp.items(section)}
                for section in cp.sections()}
    except (IOError, configparser.Error):
        return dict()

def read_language_file(language):
    try:
        messages_json_content = open(os.getcwd() + "/" + os.path.dirname(__file__) + '/' + language + '.json')
        return json.load(messages_json_content)
    except:
        return {}

def get_slot_value_by_slot_name(intent, slot_name, default_value):
    jsonString = (NluIntent.to_json(intent))
    jsonIntent = json.loads(jsonString)
    slots = jsonIntent["slots"]

    for i in range(len(slots)):
        if slots[i]['slotName'] == slot_name:
            return slots[i]['value']['value']
    return default_value


def end_session(intent, sentence):
    print('session: ' + intent + ': ' + sentence)
    return EndSession(sentence)



############################################### Music Player  ###############################################

@app.on_intent("MusicPlayerAddToPlaylist")
async def MusicPlayerAddToPlaylist(intent: NluIntent):
    playlist_name = get_slot_value_by_slot_name(intent, 'playlist_name', None)
    sentence = music_player.addMp3ToPlaylist(playlist_name)
    return end_session('AddToPlaylist', sentence)

@app.on_intent("MusicPlayerRemoveFromPlaylist")
async def MusicPlayerRemoveFromPlaylist(intent: NluIntent):
    playlist_name = get_slot_value_by_slot_name(intent, 'playlist_name', None)
    sentence = music_player.removeMp3ToPlaylist(playlist_name)
    return end_session('RemoveFromPlaylist', sentence)

@app.on_intent("MusicPlayerAddToFavourites")
async def get_date(intent: NluIntent):
    sentence = music_player.addMp3ToPlaylist()
    return end_session('AddToFavouritesPlayMusic', sentence)

@app.on_intent("MusicPlayerPlayPlaylist")
async def MusicPlayerPlayPlaylist(intent: NluIntent):
    playlist_name = get_slot_value_by_slot_name(intent, 'playlist_name', None)
    sentence = music_player.playPlaylist(playlist_name)
    return end_session('MusicPlayerPlayPlaylist', sentence)

@app.on_intent("Stop")
async def Stop(intent: NluIntent):
    sentence = music_player.stop()
    return end_session('Stop', '')

@app.on_intent("Next")
async def Next(intent: NluIntent):
    sentence = music_player.next()
    return end_session('Next', sentence)

@app.on_intent("Previous")
async def Previous(intent: NluIntent):
    sentence = music_player.previous()
    return end_session('Previous', sentence)

@app.on_intent("MusicPlayerScanMusic")
async def MusicPlayerScanMusic(intent: NluIntent):
    sentence = music_player.scanMusic()
    return end_session('MusicPlayerScanMusic', sentence)

@app.on_intent("Training")
async def Training(intent: NluIntent):
    sentence = music_player.train()
    return end_session('MusicPlayerScanMusic', sentence)

@app.on_intent("MusicPlayerWhatIsPlaying")
async def MusicPlayerWhatIsPlaying(intent: NluIntent):
    sentence = music_player.what_is_playing()
    print(sentence)
    return end_session('ScanMusic', sentence)

@app.on_intent("MusicPlayerAddStars")
async def MusicPlayerAddStars(intent: NluIntent):
    stars = get_slot_value_by_slot_name(intent, 'stars', '')
    sentence = music_player.add_stars(stars)
    return end_session('MusicPlayerAddStars', sentence)

@app.on_intent("MusicPlayerPlayFavouriteMusic")
async def MusicPlayerPlayFavouriteMusic(intent: NluIntent):
    stars = get_slot_value_by_slot_name(intent, 'stars', '')
    sentence = music_player.play_music_with_stars(stars)
    return end_session('MusicPlayerPlayFavouriteMusic', sentence)



@app.on_intent("MusicPlayer")
async def get_date(intent: NluIntent):
    print(intent)
    music_albums = get_slot_value_by_slot_name(intent, 'music_albums', '')
    music_genres = get_slot_value_by_slot_name(intent, 'music_genres', '')
    music_titles = get_slot_value_by_slot_name(intent, 'music_titles', '')
    music_artists = get_slot_value_by_slot_name(intent, 'music_artists', '')
    #song = get_slot_value_by_slot_name(intent, 'song', None)

    sentence = music_player.play({
        "album": music_albums.lower(),
        "genre": music_genres.lower(),
        "title": music_titles.lower(),
        "artist": music_artists.lower()
    })
    return end_session('PlayMusic', sentence)




if __name__ == "__main__":
    config = read_configuration_file()
    language = read_language_file(config['setup']['language'])
    print(config)
    music_player = MuuzikPlayer(config['setup'], language)
    print('  jo jo jo')
    app.run()