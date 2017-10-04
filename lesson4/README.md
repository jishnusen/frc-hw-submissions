# Assignment #4
## Conditionals and Booleans
Input the user’s age. Then, tell them what they can and cannot do using the following criteria and if/elif/else statements:
  1. 14+ can join robotics team
  2. 16+ can drive and get a job
  3. 18+ can attend college
  4. 21+ is an adult
  5. 35+ can become President

# Assignment #4.5
## Lesson 4.5: The Software Engineering Process
We have an array of patients with values of their weight and height. This program is supposed to return the BMI (Body Mass Index) for with patient in a loop. However, something is not quite right. Time to debug!!
```python
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
def calculate_bmi(weight, height):
  return weight / (height ** 2)
for patient in patients:
  weight, height = patients[0]
bmi = calculate_bmi(height, weight)
print "Patient's BMI is:" + str(bmi)
```

