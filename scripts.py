from datetime import datetime
import math as maths
import random 
import time 


def condensedTimecode(past, present, frameMax):
    # format timecode in a condenced format as described in: 'IV.D Timecodes', take in the last stroke time, the current stroke time and the frameMax value, output the condenced timecode string, showing only the difference

    def roundFrame(frame):
        # calculate the frame value from microseconds into sections based off of `frameMax`
        sectionSize = 1000000 / frameMax
        return str(int(maths.floor(int(frame) / sectionSize)))

    # calculate all the variables required
    pastHour = past.strftime('%H:')
    presentHour = present.strftime('%H:')
    pastMinute = past.strftime('%M:')
    presentMinute = present.strftime('%M:')
    pastSecond = past.strftime('%S:')
    presentSecond = present.strftime('%S:')
    pastFrame = roundFrame(past.strftime('%f'))
    presentFrame = roundFrame(present.strftime('%f'))

    if pastHour != presentHour:
        # when the hour has changed, output a whole timestamp
        return presentHour + presentMinute + presentSecond + presentFrame
    if pastMinute != presentMinute:
        return presentMinute + presentSecond + presentFrame
    if pastSecond != presentSecond:
        return presentSecond + presentFrame
    if pastFrame != presentFrame:
        return presentFrame
    # if nothing has changed, no need for any output
    return ''


# --- condensedTimecode testing ---
frameMax = 24
past = datetime.now()
randSleep = random.randrange(0,10000)
time.sleep(randSleep / 1000)
present = datetime.now()

print("past : " + str(past))
print("randSleep : " + str(randSleep))
print("present : " + str(present))
print("condensedTimecode : " + condensedTimecode(past, present, frameMax))


# ------
