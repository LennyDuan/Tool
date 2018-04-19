import csv
from objects import Transcript

def createTranscriptMapper(transcript, path):
    #print('###### Initial Transcript ######\n')
    transcriptLists = csv.reader(open(path))
    for arr in transcriptLists:
        createTranscript(transcript, arr)
    #print('###### End Initializing ######\n')
    return transcript;

def createTranscript(transcript, arr):
    code = arr[0]
    title = arr[1]
    score = arr[2]
    credits = arr[3]
    if(len(arr) > 4):
        category = arr[4]
    else:
        category = ''

    singleTranscript = Transcript(code, title, score, credits, category)
    transcript[code] = singleTranscript
