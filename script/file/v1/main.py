import csv
from objects import DegreeCourse

def map(transcript, mapper, template):
    code = transcript.code
    if mapper[code]:
        courseMapper = mapper[code]
        department = courseMapper.department
        equivalency = courseMapper.equivalency
        credits = courseMapper.credits
        course_name = courseMapper.title
        prerequisite = '-'
        corequisite = '-'

        inTempate = False
        for key, val in template.items():
            if(equivalency.upper() in key.upper()):
                #print(courseMapper.toString())
                val.grade = credits
                val.note = '转自:' + code
                inTempate = True
                break

        # Need to Add to Template
        if not inTempate:
            if equivalency and not 'NULL':
                ## Put course in to category with equivalency CODE
                nbr = equivalency
                note = '转自:' + code
                # No courseList now, need to Initializing...
                # findDepartment = courseList[nbr]
                # degreeCourse = DegreeCourse(nbr, course_name, findDepartment,
                # prerequisite, corequisite, credits, credits,note)
                # template[nbr] = degreeCourse
                print('Put course in to category')
            else :
                nbr = code
                node = '课程: ' + nbr + ' 无对应课号'
                degreeCourse = DegreeCourse(nbr, course_name, department,
                prerequisite, corequisite, credits, credits, note)
                template[nbr] = degreeCourse
                print('Put course in to category')

    # Need to Add to Template
    else:
        # No code found in Map, should be General/IB with origin Data
        print('Cannot find the course' + transcript)

def writeCSV(category, path, major):
    name = input("请输入学生姓名：")
    id = input("请输入学生学号：")
    with open(path, 'w') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        title = "name,"
        title += name
        title += ",Student ID:,"
        title += id
        csv_file.write(title)
        csv_file.write('\n')
        csv_file.write('\n')
        for key, val in category.items():
            cat_head = ""
            cat_head += val.name
            cat_head += ","
            cat_head += str(val.required)
            cat_head += " credits required,"
            cat_head += str(val.completed)
            cat_head += " credits completed"
            cat_degreeCourses = val.degreeCourses
            csv_file.write(cat_head)
            csv_file.write('\n')
            csv_file.write('Nbr,Course Name,Prerequisite,Corequisite,Crs,Grade,Note')
            csv_file.write('\n')
            for course in cat_degreeCourses:
                wr.writerow(course)
            csv_file.write('\n')
            csv_file.write('\n')
