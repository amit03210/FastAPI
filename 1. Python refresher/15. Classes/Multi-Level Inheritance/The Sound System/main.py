# EXERCISE 4: The Sound System
# Create a parent 'Speaker' with a 'volume' attribute and 'play' method.
# Create a child 'SmartSpeaker' that inherits from Speaker.
# Override the 'play' method in SmartSpeaker to first print "Connecting to WiFi..." 
# and then use super().play() to do the actual playing.

from smartSpeaker import SmartSpeaker
from speaker import Speaker

def main():
    sony = Speaker(100,20)
    boat = SmartSpeaker(150, 15, "Evangence")

    print(sony.play())
    print(boat.play())

if __name__ == '__main__':
    main()