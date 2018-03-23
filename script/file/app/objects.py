class Result:

    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    def toString(self):
        print('Course: ' + self.id + ' ' + self.name + ' - ' + self.score + '\n')

class CourseMapper:

    def __init__(self, id, eName, cName, min, score):
        self.id = id
        self.eName = eName
        self.cName = cName
        self.min = min
        self.score = score

    def toString(self):
        print('Course: ' + self.id + ' ' + self.eName
         + '\n课程: ' + self.cName + '  最低转分要求: '
         + '\n可转学分: ' + self.score + '\n')
