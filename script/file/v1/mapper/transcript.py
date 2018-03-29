import csv
from objects import Transcript

def createTranscriptMapper(transcript, path):
    print('###### Initial Transcript ######\n')
    transcriptLists = csv.reader(open(path))
    for arr in transcriptLists:
        createTranscript(transcript, arr)
    print('###### End Initializing ######\n')
    return transcript;

def createTranscript(transcript, arr):
    code = arr[0]
    title = arr[1]
    if len(arr) > 2:
        score = arr[2]
    else:
        score = 'None'

    singleTranscript = Transcript(code, title, score)
    transcript[code] = singleTranscript
