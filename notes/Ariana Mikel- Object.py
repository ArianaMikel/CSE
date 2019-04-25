class Television(object):
    def __init__(self, sound, channel):
        # These are attributes that a television has
        # These should all be relevant to our program
        self.signal = True
        self.screen = True
        self.speakers = 2
        self.chassis = True
        self.volume = sound
        self.power = False
        self.channel = channel
        self.remote = True

    def turn_on(self):
        self.power = True

    def turn_off(self):
        self.power = False

    def volume_change(self, volume):
        if not self.power:
            print("The TV is not turned on.")
            return
        if not self.remote:
            print("You do not have a remote")
            return
        if not self.speakers:
            print("You do not have any speakers")
            return
        if not self.screen:
            print("You do not have a screen.")
            return
        self.volume = volume
        print("Your volume is at ")
        print(volume)

    def change_channel(self, channel):
        if not self.power:
            print("The TV is not turned on.")
            return
        if not self.remote:
            print("You do not have a remote")
            return
        if not self.speakers:
            print("You do not have any speakers")
            return
        if not self.screen:
            print("You do not have a screen.")
            return
        self.channel = channel
        print("You are watching " + channel)


my_TV = Television(100, "PBS")
my_TV.turn_on()
my_TV.change_channel("ABC")
my_TV.turn_off()
my_TV.volume_change(30)
my_TV.turn_on()
my_TV.volume_change(30)
