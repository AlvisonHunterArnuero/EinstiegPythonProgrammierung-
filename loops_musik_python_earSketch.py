# Go to https://earsketch.gatech.edu to run this script
# Script_name: MY HOT HOUSE SUMMER MIX 2021
# Author: Made with ♥ in Python 3 by Alvison Hunter - May 21st, 2021
# Description: Quick sound loop sample using Python to set the instructions
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj

# EarSketch is a free educational programming environment. Its core purpose
# is to teach coding in two widely used languages, Python and JavaScript,
# through music composing and remixing.

from earsketch import *

init()
setTempo(120)
# DRUMS
fitMedia(RD_UK_HOUSE_MAINBEAT_3, 1, 1, 5)
fitMedia(RD_UK_HOUSE_MAINBEAT_15, 1, 5, 9)
fitMedia(RD_UK_HOUSE_MAINBEAT_3, 1, 9, 13)
fitMedia(RD_UK_HOUSE_MAINBEAT_15, 1, 13, 17)

# BASS
fitMedia(HIPHOP_BASSSUB_001, 2, 1, 5)
fitMedia(HIPHOP_BASSSUB_004, 2, 5, 9)
fitMedia(HIPHOP_BASSSUB_001, 2, 9, 13)
fitMedia(HIPHOP_BASSSUB_004, 2, 13, 17)

# CHORDS
fitMedia(HOUSE_DEEP_AIRYCHORD_002, 3, 1, 5)
# VOLUME FX - Val, start track, Val, end track
setEffect(3, VOLUME, GAIN, -40, 1, 5, 2)
fitMedia(HOUSE_DEEP_CHORD_001, 3, 5, 9)
fitMedia(RD_UK_HOUSE__5THCHORD_2, 3, 9, 13)
fitMedia(HOUSE_DEEP_CHORD_001, 3, 13, 17)
# VOLUME FX - Val, start track, Val, end track
setEffect(3, VOLUME, GAIN, 5, 16, -55, 17)

# VOCAL 1
fitMedia(YG_TECHNO_VOX_1, 4, 3, 5)
fitMedia(CIARA_SET_VOX_HOOK_HARMONY, 4, 9, 13)
fitMedia(COMMON_LOVE_VOX_ADLIB_2, 4, 15, 17)
setEffect(4, REVERB, REVERB_TIME, 200)

# VOCAL 2
fitMedia(COMMON_LOVE_VOX_ADLIB_1, 5, 1, 3)
fitMedia(CIARA_MELANIN_VOX_CIARA_1, 5, 5, 9)
fitMedia(COMMON_LOVE_VOX_ADLIB_1, 5, 13, 15)
setEffect(5, DELAY, DELAY_TIME, 500)

# End of the song
finish()
