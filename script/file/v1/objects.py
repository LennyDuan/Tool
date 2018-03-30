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

    def toString(self):
        print('Degree Course Nbr: [' self.nbr+ + '] Course_Name: [' + self. course_name '] ' +
        'Category: [' + self.category + '] ' + 'C/Hrs: [ ' + self.chrs + '] ' +
        'Grade: [' + self.grade + ']')

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

    def __init__(self, code, title, score):
        self.code = code
        self.title = title
        self.score = score

    def toString(self):
        print('Course Code [' + self.code + '] Title: [' + self.title + '] Score: [' + self.score + ']')
