import os
import csv
from mapper.mapper import createCourseMapper
from mapper.transcript import createTranscriptMapper
from mapper.template import createDegreeCourseTemplate
from mapper.category import createDegreeCourseCategory

from main import map
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
category = {}
print('\n###### Start Creating Degree Check Sheet Template ######\n')
major = input('Please input student major ECE or ME: \n')
Mpath = dir + '/degree_progress_check_sheet/init/' + major + '.csv'
print('Initing Major Template: [' + major +'] Degree Check Sheet with Template: ' + Mpath)
assert Mpath
template = createDegreeCourseTemplate(template, Mpath)
#for key, val in template.items():
    #val.toString()

Cpath = dir + '/degree_progress_check_sheet/init/' + major + '_category.csv'
assert Cpath
category = createDegreeCourseCategory(category, Cpath)
#for key, val in category.items():
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
for key, val in transcript.items():
    map(val, mapper, template)

#for key, val in template.items():
    #val.toString()
print('\n###### End Mapper Transcrit to Degree Course ######\n')
print('\n------------------------------------------------\n')

## Add Degree Course to Category
print('\n###### Start Add Degree Course to Category ######\n')
for key, val in template.items():
    if(category[val.category]):
        cat = category[val.category]
        cat.addCourse(val)

# for key, val in category.items():
#     val.toString()

print('\n###### End Add Degree Course to Category ######\n')
print('\n------------------------------------------------\n')

## Create CSV Final File
print('\n###### Start Create Final CSV File ######\n')
Opath = dir + '/result/' + name + '.csv';
with open(Opath, 'w') as csv_file:
    wr = csv.writer(csv_file, delimiter=',')
    for key, val in template.items():
        wr.writerow(val)

print('\n###### Start Create Final CSV File ######\n')
print('\n------------------------------------------------\n')
