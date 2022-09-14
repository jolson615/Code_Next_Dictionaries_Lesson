my_schedule = ["Math", "History", "Biology", "Art", "English", "Music"]
cancelled_courses = ["Art","Music","PE"]
replacements_needed = 0
## How many courses in your schedule were canceled? 
## In other words, how many replacements do you actually need?

for course in my_schedule:
  if course in cancelled_courses:
    replacements_needed += 1
## Will this for loop find the right number of classes to be replaced?

print("You must replace " + str(replacements_needed) + " classes in your schedule due to course cancellations")

if replacements_needed > 0:
  new_class = input("What class would you like to add to your schedule?:")
  if len(my_schedule) < 7 and new_class in my_schedule == False:
    print("Class Added")
  else:
    print("Could not add your selected class")
## Will this 'if' statement get you back up to 7 classes?
## Is there anything about this program you would change?