from datetime import datetime
dt = datetime.now()
x = dt.strftime('%Y-%m-%d %H:%M:%S')
print (type(x))
y = dt.strptime(x,'%Y-%m-%d %H:%M:%S')
print (y.date().month)
print ()