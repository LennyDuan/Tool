import os
from mapper.mapper import createCourseMapper
from mapper.transcript import createTranscriptMapper

## Initializing
print('###### Start Initializing ######')
dir = os.getcwd()
Mpath = dir + '/equivalence_course/UM equivalence_course.csv'
print('Find Course Mapper: ' + Mpath)

## Init courseMapper
print('###### Start Reading Mapper ######\n')
mapper = {}
mapper = createCourseMapper(mapper, Mpath)
for key, val in mapper.items():
    val.toString()
print('###### End Reading Mapper ######\n')
print('------------------------------------------------\n')


## Init Transcript
print('###### Start Reading Transcript ######\n')
transcript = {}
name = input('Please input a student transcript file name: \n')
Tpath = dir + '/transcript/' + name;
print('Find Student: [' + name +'] Transcript: ' + Tpath)
assert Tpath
transcript = createTranscriptMapper(transcript, Tpath)
for key, val in transcript.items():
    val.toString()
print('###### End Reading Transcript ######\n')
print('------------------------------------------------\n')
