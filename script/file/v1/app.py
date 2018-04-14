import os
from mapper.mapper import createCourseMapper
from mapper.transcript import createTranscriptMapper
from mapper.template import createDegreeCourseTemplate

## Initializing
print('\n###### Start Initializing ######')
dir = os.getcwd()
Mpath = dir + '/equivalence_course/UM equivalence_course.csv'
print('Find Course Mapper: ' + Mpath)

## Init courseMapper
mapper = {}
print('\n###### Start Reading Mapper ######\n')
mapper = createCourseMapper(mapper, Mpath)
# key, val in mapper.items():
    # val.toString()
print('\n###### End Reading Mapper Successful ######\n')
print('\n------------------------------------------------\n')

## Init Template
template = {}
print('\n###### Start Creating Degree Check Sheet Template ######\n')
major = input('Please input student major ECE or ME: \n')
Mpath = dir + '/degree_progress_check_sheet/init/' + major + '.csv'
print('Initing Major Template: [' + major +'] Degree Check Sheet with Template: ' + Mpath)
assert Mpath
template = createDegreeCourseTemplate(template, Mpath)
#for key, val in template.items():
    #val.toString()
print('\n###### End Creating Degree Check Sheet Template Successful ######\n')
print('\n------------------------------------------------\n')

## Init Transcript
transcript = {}
print('\n###### Start Reading Transcript ######\n')
name = input('Please input a student transcript file name: \n')
Tpath = dir + '/transcript/' + name + '.csv';
print('\nFind Student: [' + name +'] Transcript: ' + Tpath)
assert Tpath
transcript = createTranscriptMapper(transcript, Tpath)
#for key, val in transcript.items():
    #val.toString()
print('\n###### End Reading Transcript Successful ######\n')
print('\n------------------------------------------------\n')

## Add Mapper Transcrit to Degree Course
print('\n###### Start Mapper Transcrit to Degree Course ######\n')
print('\n###### End Mapper Transcrit to Degree Course ######\n')
print('\n------------------------------------------------\n')
