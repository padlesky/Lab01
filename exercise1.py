class Student:
    courseMarks={}

    def __init__(self, name, family):
        self.name = name
        self.family = family

    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark

    def average(self):
        temp = 0
        count = 0
        for x in self.courseMarks:
            temp = temp + self.courseMarks[x]
            count = count + 1
        avg = temp/count
        return avg

student = Student("Bob", "McGee")
print "expect Bob, McGee"
print "got: %s, %s " %(student.name, student.family)
student.addCourseMark("CMPUT310", 80)
student.addCourseMark("STS351", 70)
student.addCourseMark("CMPUT350", 80)
print "Expected 76"
print "Got: %s" %student.average()
