class CourseList:

    def __init__(self, code, name_en, credit, category)

    def toString(self):
        print('Course ' + self.code + ' : [' + self.name_en +
         '] Credits: [' +  self.credit + '] Category: [' + self.category + ']')

class DegreeCategory:

    def __init__(self, name, required):
        self.name = name
        self.required = required
        self.completed = 0
        self.degreeCourses = []

    def addCourse(self, degreeCourse):
        self.degreeCourses.append(degreeCourse)
        if degreeCourse.chrs:
            self.completed += int(degreeCourse.chrs)

    def toString(self):
        print('Category: [' + self.name +'] Required Creds: [' + self.required +']')
        for ele in self.degreeCourses:
            print(ele.toString())
        print('Completed Cred: [' + str(self.completed) + ']\n')

class DegreeCourse:

    def __init__(self, nbr, course_name, category,
    prerequisite, corequisite, chrs, grade, note):
        self.nbr = nbr
        self.course_name = course_name
        self.category = category
        self.prerequisite = prerequisite
        self.corequisite = corequisite
        self.chrs = chrs
        self.grade = grade
        self.note = note

    def __iter__(self):
        return iter([self.nbr, self.course_name,self.prerequisite,
        self.corequisite, self.chrs, self.grade, self.note])

    def toString(self):
        print('Degree Course Nbr: [' + self.nbr + '] Course_Name: [' + self.course_name
        + '] Category: [' + self.category + ']')
        if self.chrs:
            print('Chrs: [' + self.chrs+ '] ')
        if self.note:
            print('Note: [' + self.note+ '] ')

class CourseMapper:

    def __init__(self, department, code, codePlus, title,
    equivalency, remarks, category,credits, level):
        self.department = department
        self.code = code
        self.codePlus = codePlus
        self.title = title
        self.equivalency = equivalency
        self.remarks = remarks
        self.category = category
        self.credits = credits
        self.level = level

    def toString(self):
        print('Course: [' + self.title + '] Department: [' + self.department
         + '] Code: [' + self.code + '] Code Plus: [' + self.codePlus
         + '] Equivalency: [' + self.equivalency+ '] Category: [' + self.category
         + '] Credits: [' + self.credits + ']\n')

class Transcript:

    def __init__(self, code, title, score, credits, category):
        self.code = code
        self.title = title
        self.score = score
        self.credits = credits
        self.category = category

    def toString(self):
        print('Course Code [' + self.code + '] Title: [' + self.title + '] Score: [' + self.score + '] Cat: [' + self.category+ ']')
