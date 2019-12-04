import datetime
x = datetime.date.today()
print("Current date = ",x)
w = int(input("Enter before days number : "))
y = x - datetime.timedelta(days = w)
print("Date of before ",w ,"days is",y)
r = int(input("Enter after any days : "))
t = x + datetime.timedelta(days = r)
print("Date of ",r," after is :",t)

