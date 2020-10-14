from datetime import date, datetime
print("date of birth")
dob = int(input())
print("month of birth")
mob = int(input())
print("year of birth")
yob = int(input())
print("how many years")
years = int(input())
Bday = datetime(month = mob, day = dob, year = yob)
index = Bday.weekday()
VIndex = {'dayweek': 0}
x = 0
yob2 = yob + years
for i in range(yob, yob2):
    Bday = datetime(month = mob, day = dob, year = yob)
    wd = Bday.weekday()
    if wd == index:
        VIndex["dayweek"] = x + 1
        x = x + 1
    yob = yob + 1
if index == 0:
    g = "monday"
elif index == 1:
    g = "tuesday"
elif index == 2:
    g = "wednesday"
elif index == 3:
    g = "thursday"
elif index == 4:
    g == "friday"
elif index == 5:
    g = "saturday"
elif index == 6:
    g = "sunday"
a = f"You were born on {g} and it is repeated {VIndex['dayweek']} times in {years} years"
print(a)
print("please restart the programme")