import alsaaudio

class Volume:
    def __init__(self,language):
        self.language = language['volumeControl']

        #for some this can be Master instead of PCM if you get errors try Master
        try:
            self.alsaaudioMixer = alsaaudio.Mixer('PCM')
        except Exception as ex:
            self.alsaaudioMixer = alsaaudio.Mixer('Master')
        self.beforeMuting = self.alsaaudioMixer.getvolume()[0]
        self.volume = self.alsaaudioMixer.getvolume()[0]

    def set_language(self, intentMessage):
        self.language = intentMessage


    def mute_volume(self):
        print('mute', self.beforeMuting)
        self.beforeMuting = self.alsaaudioMixer.getvolume()[0]
        self.volume = 0
        self.alsaaudioMixer.setvolume(0)

    def unmute_volume(self):
        print('un mute', self.beforeMuting)
        self.volume = self.beforeMuting
        self.alsaaudioMixer.setvolume(self.beforeMuting)

    def set_volume(self, volume):
        if volume > 0:
            volume = int(volume / 10) * 10
        self.volume = volume
        self.beforeMuting = self.get_real_volume(volume)
        self.alsaaudioMixer.setvolume(self.get_real_volume(volume))
        return self.language["setVolume"].format(volume)

    def get_volume(self):
        return self.alsaaudioMixer.getvolume()[0]

    def increase_volume(self):
        return self.set_volume(min(100,self.get_volume + 10))

    def decrease_volume(self):
        return self.set_volume(min(100, self.get_volume - 10))

    # it seems one needs to map the PCM to get the real %  see:
    # https://forum-raspberrypi.de/forum/thread/42097-lautstaerke-per-befehl-aendern/#
    def get_real_volume(self, volume):
        switcher = {
            0: 0,
            2: 0,
            10: 43,
            20: 60,
            30: 70,
            40: 77,
            50: 83,
            60: 87,
            70: 91,
            80: 94,
            90: 97,
            100: 100
        }
        return switcher.get(volume)

