
import datetime

start = datetime.datetime.strptime('26 02', '%d %m')
end = datetime.datetime.strptime('03 03', '%d %m')
print((end - start).days)
