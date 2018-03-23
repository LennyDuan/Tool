class Result:

    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    def toString(self):
        print('Course: ' + self.id + ' ' + self.name + ' - ' + self.score + '\n')

class CourseMapper:

    def __init__(self, id, eName, cName, min, point):
        self.id = id
        self.eName = eName
        self.cName = cName
        self.min = min
        self.point = point

    def toString(self):
        print('Course: ' + self.id + ' ' + self.eName
         + '\n课程: ' + self.cName + '  最低转分要求: '
         + '\n可转学分: ' + self.point + '\n')

class Course:

    def __init__(self, cName):
        self.cName = cName
        self.results = []
        self.sum = 0

    def add(self, result, point):
        self.results.append(result)
        self.sum += int(point)

    def toString(self):
        print('课程: ' + self.cName)
        print('转分来自: ')
        for ele in self.results:
            ele.toString()
        print('总转学分: ' + str(self.sum))
