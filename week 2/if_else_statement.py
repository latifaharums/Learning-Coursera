#Requirement
#Score 60 or more is Pass
#Score above 95 is Top Score
#Under 60 is Fail

#Create function if else elif and then return grade
def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade

#Print value
print(exam_grade(65)) # Should print Pass
print(exam_grade(55)) # Should print Fail
print(exam_grade(60)) # Should print Pass
print(exam_grade(95)) # Should print Pass
print(exam_grade(100)) # Should print Top Score
print(exam_grade(0)) # Should print Fail