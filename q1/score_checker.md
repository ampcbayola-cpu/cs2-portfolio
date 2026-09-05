# Clean Decision Code Makeover: Student Score Checker
**Name:** Ada Mary Phoebe C. Bayola
**Section:** 8 - Dahlia
---
## Activity Overview

In this activity, I improved a Student Score Checker program by applying proper coding standards and
selection structures.
The program accepts a student score from 0 to 100 and determines the appropriate classification.

The classifications are:
| Score | Classification |
|---:|---|
| 90–100 | Outstanding |
| 0–74 | Needs Improvement |

Scores below 0 or above 100 are considered invalid.
---
# Part 1 - Analyze the Logic
## Input
What information does the program need?

> The program primarily needs the users score as an input but also,
> needs to know whether its a valid score then classify it accordingly

## Valid Range
**Minimum valid score:**

> 1
**Maximum valid score:**

> 100

## Possible Outputs
List all possible outputs of the program.
1. "Invalid score"
2. "Outstanding"
3. "Very Satisfactory"
4. "Satifactory"
5. "Needs improvement"

## Boundary Condition
What condition will you use to determine whether the score is valid?
> if score is less than 0 ore more than 100.

## Multiple Decision Paths
Explain how the program decides which classification should be displayed.
> with the elif chain<img width="2199" height="1681" alt="whycomsci - Main" src="https://github.com/user-attachments/assets/28eafe4d-67ba-43f9-9c05-3db507aa1c2c" />

---
# Part 2 - Flowchart
Create a flowchart showing the logic of your program.
Your flowchart should show:
- Start
- Input score
- Valid score check
- Decision paths
- Classification
- Invalid score
- End

## Flowchart
Insert your flowchart below.
<img width="1044" height="827" alt="image" src="https://github.com/user-attachments/assets/9b30043e-badd-47be-9fd8-36b997537fbb" />

---

# Part 3 - Pseudocode
Create a pseudocode showing the logic of your program.

START
INPUT score
IF score < 0 OR score > 100 THEN
DISPLAY "Invalid score."
ELIF score >= 90 THEN
DISPLAY "Outstanding"
ELIF score >= 80 THEN
DISPLAY "Very Satifactory"
ELIF score >= 75 THEN
DISPLAY "Satisfactory"
ELIF score < 75 THEN
DISPLAY "Needs Improvement"
....
END

---
# Part 4 - Clean Code Implementation
## Source code
Insert your source code.
[Score Checker Source Code](q1/score_checker.py)

---
# Part 5 - Testing
| Test | Input | Purpose | Expected Output | Actual Output | Result |
|---|---:|---|---|---|---|
| 1 | -1 | Below minimum | | | |
| 2 | 0 | Minimum boundary | | | |
| 3 | 74 | Below Satisfactory boundary | | | |
| 4 | 75 | Satisfactory boundary | | | |
| 5 | 80 | Very Satisfactory boundary | | | |
| 6 | 90 | Outstanding boundary | | | |
| 7 | 100 | Maximum boundary | | | |
| 8 | 101 | Above maximum | | | |

---

## Testing Reflection
### 1. Why is it important to test the values 0 and 100?
> To see if I had put the wrong value in the wrong output.
### 2. Why did you also test -1 and 101?
> Because it is sometimes unrealistic & it also sets a standard.
### 3. Which test helped you understand boundary conditions the most?
> the range limitation from 1-100
### 4. Did any of your tests initially fail? If yes, what did you change in your program?
> yes, indention in the elif parts because, I forgot how it worked so I had many syntax errors.

---

# Reflection
### 1. How did selection structures make the program more useful?
>Selection structures allow the program to make dynamic decisions by screening out invalid scores
> and assigning inputs to their correct performance tiers.
### 2. How did proper comments and readable formatting improve your program?
>Proper comments clarify code logic for future maintenance, while clean indentation prevents syntax
>errors and keeps execution blocks organized.
### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code?
>Planning with flowcharts and pseudocode lets you map out program logic and catch edge cases visually
>before writing syntax-heavy code.
