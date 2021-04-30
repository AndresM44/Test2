


"""
The program is trying to analyze student grades on a final exam.
First the program wants to find the number of scores found on the Finals.txt file.
Afterwards, the program will calculate the average score of the students.
Then the program will want to find the percentage of the scores that are above the average which was found on the second step.

First function will output number of grades.
Second function will loop through the scores and output the average grade.
Third function will also loop and find the percentage of grades above average.

"""

"""
# function 1
file = open(Txt file, rt)
data = file.read
numbers = data.split()
print('Number of grades: ', len(numbers))
#function 2
infile = open (Txt file, rt)
total = 0
number_of_lines = 0
line = float(infile.readline())
while line != "":
    number_of_lines += 1
    total += float(line)
    line = infile.readline()
    average = total / number_of_lines
print("Average grade: ", average)

    
"""

def main():
    file = open("Final.txt", "rt")
    data = file.read()
    numbers = data.split()
    print("Number of grades: ", len(numbers))
    infile = open("Final.txt", "rt")
    total = 0
    number_of_lines = 0
    line = float(infile.readline())
    for i in range(0, 24):
        number_of_lines += 1
        total += float(line)
        line = infile.readline()
        average = total / number_of_lines
    print("Average grade: ", average)

# def calculate_percent_above_average():
#     infile = open("Final.txt", "rt")
#     total = 0
#     number_of_lines = 0
#     line = float(infile.readline())
#     for i in range(0, 24):
#         number_of_lines += 1
#         total += float(line)
#         line = infile.readline()
#         average = total / number_of_lines
#     for average_grade in file:
#         above_average = 0
#         average_grade = 0
#         if average_grade > average:
#             above_average += 1
#     print("Percentage of grades above average: {0:.2f}%", above_average)
#     return above_average

# calculate_percent_above_average()
main()
    
