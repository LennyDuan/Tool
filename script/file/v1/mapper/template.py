import csv
from objects import DegreeCourse
from mapper.number import createNbr
def createDegreeCourseTemplate(template, path):
    print('\n###### Initial Template ######\n')
    file = csv.reader(open(path))
    category = None
    for arr in file:
        category = createTemplate(template, arr, category)
    print('\n###### End Initializing ######\n')
    return template;

def createTemplate(template, arr, category):
    if (len(arr) == 1):
        category = arr[0]
    else:
        nbr = arr[0]
        course_name = arr[1]
        prerequisite = arr[2]
        corequisite = arr[3]
        chrs = arr[4]
        grade = arr[5]
        note = arr[6]

        degree = DegreeCourse(nbr, course_name, category, prerequisite,
        corequisite, chrs, grade, note)
        template[nbr] = degree

    return category
