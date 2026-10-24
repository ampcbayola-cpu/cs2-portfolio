#problem description : 
#- create a program that computes a students' average score from 3 assessments 
# and determines the students performnace category and eligibility for a practice
# challenge.


def calculate_average(score1, score2, score3):
  return (score1 + score2 + score3) / 3

def get_performance(average):
  if average >= 85:
    return "Mastery"
  elif average >= 70:
    return "Developing"
  else:
    return "Needs Review"

def is_eligible(average, completed_tasks):
  if average >= 85 and completed_tasks >= 3:
    return True
  else:
    return False

score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))
completed_tasks = int(input("Completed Tasks: "))

average = calculate_average(score1, score2, score3)
performance = get_performance(average)
eligible = is_eligible(average, completed_tasks)

print(f"Average: {average:.2f}")
print(f"Performance: {performance}")
print(f"Eligible for Challenge: {eligible}")


# Documentation Questions  🡇
# 1.) the functions calculate_average, get_performace, and is_eligible do those respectively
# 2.)  calculate_average function computes the value and sends it back using "return" and that 
#- said returned value is saved into a variable in the main program then passed onto 
#- get_performance as the argument.
# 3.) the is_eligibe function will turn out false because of "and" which needs both to be true.
# 4.) "return" sends the data back to the main program so the values can be stored in variables,
#- reused across other functions. Using print() would instead just display text on the output
#- screen making it hard to pass the results around or use them in logic checks.


