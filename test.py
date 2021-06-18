from datetime import date
from datetime import datetime
today=date.today()
d2 = today.strftime("%B %d, %Y")
print(d2)

def xuly(you):
    if you=="":
        robot="I can't hear you, try again ."
    elif you=='hello':
        robot='Hello Phuc'
    elif "today" in you:
        today=date.today()
        robot=today.strftime("%B %d, %Y")
    elif "time" in you:
        now=datetime.now()
        robot=now.strftime("%H hours %M minutes %S seconds")
    elif "president" in you:
        robot="Joe Biden"
    else:
        robot="I'm fine thank you, and you ?"
    return robot
print(xuly("president"))