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
# key, val in mapper.items():
    # val.toString()
print('###### End Reading Mapper Successful ######\n')
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
print('###### End Reading Transcript Successful ######\n')
print('------------------------------------------------\n')

## Init Output
print('###### Start Creating Degree Check Sheet ######\n')
Dpath = dir + '/degree_progress_check_sheet/' + name;
print('Initing Student: [' + name +'] Degree Check Sheet: ' + Dpath)

print('###### End Creating Degree Check Sheet Successful ######\n')
print('------------------------------------------------\n')
