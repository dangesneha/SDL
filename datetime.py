# datetime operations


import datetime

t =datetime.time(1,45,56);
print t
print "hour"
print t.hour
print "minute"
print t.minute
print "second"
print t.second
print "todays date: "
print datetime.date.today()
print "tim"
print datetime.date.max
print datetime.date.min

d=datetime.date(2018,7,5)
print d.weekday()
print " "
print datetime.timedelta(0,99999)
print"replace ()"
print d.replace(month=9)
print "current time"+d.ctime()
print" "
now=datetime.datetime.now()
print "local date"+ now.strftime("%x")

print "local time:- "+ now.strftime("%X")

print "local date and time:  "+ now.strftime("%c")

