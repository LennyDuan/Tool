import os
from mapper.mapper import createCourseMapper
from mapper.transcript import createTranscriptMapper
from mapper.template import createDegreeCourseTemplate

## Initializing
print('###### Start Initializing ######')
dir = os.getcwd()
Mpath = dir + '/equivalence_course/UM equivalence_course.csv'
print('Find Course Mapper: ' + Mpath)

## Init courseMapper
mapper = {}
print('###### Start Reading Mapper ######\n')
mapper = createCourseMapper(mapper, Mpath)
# key, val in mapper.items():
    # val.toString()
print('###### End Reading Mapper Successful ######\n')
print('------------------------------------------------\n')

## Init Transcript
transcript = {}
print('###### Start Reading Transcript ######\n')
name = input('Please input a student transcript file name: \n')
Tpath = dir + '/transcript/' + name + '.csv';
print('Find Student: [' + name +'] Transcript: ' + Tpath)
assert Tpath
transcript = createTranscriptMapper(transcript, Tpath)
for key, val in transcript.items():
    val.toString()
print('###### End Reading Transcript Successful ######\n')
print('------------------------------------------------\n')

## Init Template
template = {}
print('###### Start Creating Degree Check Sheet Template ######\n')
major = input('Please input student major ECE or ME: \n')
Mpath = dir + '/degree_progress_check_sheet/init/' + major + '.csv'
print('Initing Student: [' + name +'] Degree Check Sheet with Template: ' + Mpath)
assert Mpath
template = createDegreeCourseTemplate(template, Mpath)
print('###### End Creating Degree Check Sheet Template Successful ######\n')
print('------------------------------------------------\n')
