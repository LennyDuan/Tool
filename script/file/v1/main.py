import csv
def map(transcript, mapper, template):
    code = transcript.code
    if mapper[code]:
        courseMapper = mapper[code]
        department = courseMapper.department
        equivalency = courseMapper.equivalency
        credits = courseMapper.credits

        for key, val in template.items():
            if(equivalency.upper() in key.upper()):
                #print(courseMapper.toString())
                val.grade = credits
                break
    else:
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
