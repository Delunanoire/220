"""
Name: Stephanie Pittman
weighted_average.py

Problem: Develop a Python program that uses numeric data from a text file.
         Create a new text file with the correct format.

Certificate of Authenticity:
I certify that this assignment is my work and was discussed with Tutor Brooke Duvall.

Input : text file grades.txt
Output: text file average.txt

"""
in_file_name = "grades.txt"
out_file_name = "avg.txt"

def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    grades = []
    student_name = []
    averages = []
    for line in infile.readlines():
        new_line = line.split(':')
        student_name.append(new_line[0])
        grades.append(new_line[1].split())
    for x in range(len(grades)):
        weights = []
        grade_value = []
        for i in range(len(grades[x])):
            if i % 2 == 0:
                weights.append(float(grades[x][i]))
            if i % 2 == 1:
                grade_value.append(float(grades[x][i]))
        total = 0
        if sum(weights) > 100:
            outfile.write(student_name[x] + "'s average: Error: The weights are more than 100.")
        elif sum(weights) < 100:
            outfile.write(student_name[x] + "'s average: Error: The weights are less than 100.")
        elif len(weights) > len(grade_value):
            outfile.write(student_name[x] + "'s average: Error: The number of weights exceeds the number of grades.")
        elif len(grade_value) > len(weights):
            outfile.write(student_name[x] + "'s average: Error: The number of grades exceeds the number of weights.")
        else:
            for i in range(len(weights)):
                total += (weights[i] * grade_value[i])
            average = total / 100
            averages.append(average)
            outfile.write(student_name[x] + "'s average: " + str(round(average, 2)) + "\n")
    outfile.write(str(round(sum(averages) / len(student_name), 2)))
    infile.close()
    outfile.close()
if __name__ == '__weighted_average__':
    weighted_average(in_file_name, out_file_name)