import eliza_speech_enabled
import pyttsx3

# from time import sleep
engine = pyttsx3.init()

# A PRETTY BASIC CONVERSATION PROGRAM BETWEEN TWO INSTANCES OF ELIZA #

elizaOne = eliza_speech_enabled.Eliza()
elizaTwo = eliza_speech_enabled.Eliza()

# elizaOne gets to speak first
conversationStart = "Are you a computer?"
said = conversationStart  # latest spoken response
elizaOneSpeaks = True

while True:
    print(said)
    while said[-1] in '!.':
        said = said[:-1]
    if elizaOneSpeaks is True:
        response = elizaOne.respond(said)
        print("[Eliza One]: " + response)
        # say response out loud
        engine.say(response)
        engine.runAndWait()
        elizaOneSpeaks = False
        said = response
    else:
        response = elizaTwo.respond(said)
        print("[Eliza Two]: " + response)
        # say response out loud
        engine.say(response)
        engine.runAndWait()
        elizaOneSpeaks = True
        said = response

# eliza one speaks
# eliza two responds (wait 1 second)
# eliza one responds (wait 1 second)
# etc
