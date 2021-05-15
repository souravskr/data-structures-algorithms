

def gradingStudents(grades):
    pass_mark = 40
    no_round_up_mark = pass_mark - 3
    final_mark = []
    for grade in grades:
        if (grade % 5 == 0 or grade <= no_round_up_mark):
            final_mark.append(grade)
        
        else:
            divide_by_five = int(grade / 5) + 1
            upper_limit = divide_by_five * 5
            grade_review = upper_limit - grade
            if grade_review < 3:
                final_mark.append(upper_limit)
            else:
                final_mark.append(grade)
        
    return final_mark

        
arr = [73, 67, 38, 33]
print(gradingStudents(arr))