from datetime import datetime

name = "Botti"
pvm = datetime.today()
now = datetime.now()

# dd/mm/yy H:M:S

dt_string = pvm.strftime("%d/%m/%y")
aika_string = now.strftime("%H:%M:%S")

print("Hello, the time is", dt_string, aika_string,",", name)

