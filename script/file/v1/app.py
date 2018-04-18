import os
from mapper.mapper import createCourseMapper
from mapper.transcript import createTranscriptMapper
from mapper.template import createDegreeCourseTemplate
from mapper.category import createDegreeCourseCategory
from main import map, writeCSV

## Initializing
print('\n正在初始化...')
#print('\n###### Start Initializing ######')
dir = os.getcwd()
Mpath = dir + '/equivalence_course/UM equivalence_course.csv'
#print('Find Course Mapper: ' + Mpath)

## Init courseMapper
mapper = {}
#print('\n###### Start Reading Mapper ######\n')
mapper = createCourseMapper(mapper, Mpath)
# key, val in mapper.items():
    # val.toString()
#print('\n###### End Reading Mapper Successful ######\n')
#print('\n------------------------------------------------\n')

## Init Template
template = {}
category = {}
#print('\n###### Start Creating Degree Check Sheet Template ######\n')
major = input('请输入学生专业 ECE 或者 ME: \n')
Mpath = dir + '/degree_progress_check_sheet/init/' + major + '.csv'
print('\n请稍等, 初始化...')
#print('Initing Major Template: [' + major +'] Degree Check Sheet with Template: ' + Mpath)
assert Mpath
template = createDegreeCourseTemplate(template, Mpath)
#for key, val in template.items():
    #val.toString()

Cpath = dir + '/degree_progress_check_sheet/init/' + major + '_category.csv'
assert Cpath
category = createDegreeCourseCategory(category, Cpath)
#for key, val in category.items():
    #val.toString()

#print('\n###### End Creating Degree Check Sheet Template Successful ######\n')
print('\n初始化成功')
print('\n------------------------------------------------\n')

## Init Transcript
transcript = {}
#print('\n###### Start Reading Transcript ######\n')
print('\n开始输入数据...')
name = input('请输入成绩单文件名: \n')
Tpath = dir + '/transcript/' + name + '.csv';
#print('\nFind Student: [' + name +'] Transcript: ' + Tpath)
assert Tpath
transcript = createTranscriptMapper(transcript, Tpath)
#for key, val in transcript.items():
    #val.toString()
#print('\n###### End Reading Transcript Successful ######\n')
#print('\n------------------------------------------------\n')

## Add Mapper Transcrit to Degree Course
print('\n正在转换成绩单数据...\n')
#print('\n###### Start Mapper Transcrit to Degree Course ######\n')
for key, val in transcript.items():
    map(val, mapper, template)

#for key, val in template.items():
    #val.toString()
#print('\n###### End Mapper Transcrit to Degree Course ######\n')
#print('\n------------------------------------------------\n')

## Add Degree Course to Category
#print('\n###### Start Add Degree Course to Category ######\n')
for key, val in template.items():
    if val.category in category:
        cat = category[val.category]
        cat.addCourse(val)

# for key, val in category.items():
#     val.toString()

#print('\n###### End Add Degree Course to Category ######\n')
#print('\n------------------------------------------------\n')
print('\n------------------------------------------------\n')
## Create CSV Final File
print('\n转换成功，开始生成最终成绩表格...\n')
#print('\n###### Start Create Final CSV File ######\n')
Opath = dir + '/result/' + name + '.csv';
writeCSV(category, Opath, major)
print('\n表格生成成功成功，请查看学习成绩表: ' + Opath + '\n')
#print('\n###### Start Create Final CSV File ######\n')
print('\n------------------------------------------------\n')
