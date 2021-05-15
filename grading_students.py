

def gradingStudents(grade):
    pass_mark = 40
    no_round_up_mark = pass_mark - 3
    
    if (grade % 5 == 0 or grade <= no_round_up_mark):
        return grade
    
    else:
        divide_by_five = int(grade / 5) + 1
        upper_limit = divide_by_five * 5
        grade_review = upper_limit - grade
        if grade_review < 3:
            return upper_limit
        else:
            return grade

        

print(gradingStudents(67))