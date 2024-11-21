import math
import os
import random
import re
import sys

def gradingStudents(grades):
    final_grade = []
    
    for i in grades:
        if i < 38:
            final_grade.append(i)
        elif i % 5 > 2:
            i = (i//5 + 1) * 5
            final_grade.append(i)
        else:
            final_grade.append(i)
            
    return final_grade
          
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
