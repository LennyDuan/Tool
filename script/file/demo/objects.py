class Result:

    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    def toString(self):
        print('Course: ' + self.id + ' ' + self.name + ' - ' + self.score + '\n')
