
#from dataclasses import dataclass
from datetime import datetime
from datetime import timedelta
class Time:
    def __init__(self, lname, sname, diffhour, diffmin=0):
        self.lname = lname
        self.sname = sname
        self.diffhour = diffhour
        self.diffmin = diffmin

times = [
        Time("Baker Island Time", "BIT", -12),
        Time("Samoa Standard Time", "SST", -11),
        Time("Cook Island Time", "CKT", -10),
        Time("Hawaii-Aleutian Daylight Time", "HDT", -9),
        Time("Alaska Daylight Time","AKDT",-8),
        Time("US Pacific Time", "PDT", -7),
        Time("US Mountain Time", "MDT", -6),
        Time("Acre Time", "ACT", -5),
        Time("Central Time", "CDT", -5),
        Time("Eastern Time", "EDT", -4),
        Time("Rio de Janeiro, Brazil", "-03", -3),
        Time("Oscar Time", "O", -2),
        Time("Cape Verde", "CVT", -1),
        Time("Greenwich Mean Time", "GMT", 0),
        Time("London, UK", "BST", 1),
        Time("Berlin, Germany", "CEST", 2),
        Time("Moscow, Russian Federation", "MSK", 3),
        Time("Dubai, UAE", "+04", 4),
        Time("Uzbekistan","UZT",5),
        Time("Mumbai, India", "IST", 5, 30),
        Time("Omsk", "OMST", 6),
        Time("Christmas Island", "CXT", 7),
        Time("Davis Time", "DAVT", 7),
        Time("Singapore, Singapore", "+08", 8),
        Time("Beijing, China", "CST", 8),
        Time("China Time, China", "CST", 8),
        Time("AUstralian Central Western Standard Time)", "ACWST", 8, 45),
        Time("Tokyo, Japan", "JST", 9),
        Time("Australian Central Standard Time", "ACST", 9, 30),
        Time("Australian Eastern Standard Time", "AEST", 10),
        Time("Australian Central Daylight Savings Time", "ACDT", 10, 30),
        Time("Sydney Australia", "AEDT", 11),
        Time("Wake Island", "WAKT", 12),
        Time("Auckland, New Zealand", "NZDT", 13)]
UCT = datetime.utcnow()
found = False
for t in times:
    maybe5 = UCT + timedelta(hours=t.diffhour, minutes= t.diffmin)
    if maybe5.hour == 17:
        print (t.lname)
        found = True
if not found:
    print ("aww")
'''
Time("US Mountain Time", "MDT", -6)
Time("Central Time", "CDT", -5)
Time("Eastern Time", "EDT", -4)
Time("Rio de Janeiro, Brazil", "-03", -3)
Time("London, UK", "BST", 1)
Time("Berlin, Germany", "CEST", 2)
Time("Moscow, Russian Federation", "MSK", 3)
Time("Dubai, UAE", "+04" 4)
Time("Mumbai, India", "IST" 5, 30)
Time("Singapore, Singapore" "+08" 8)
Time("Beijing, China", "CST", 8)
Time("China Time, China", "CST", 8)
Time("Tokyo, Japan", "JST", 9)
Time("Sydney Australia", "AEDT", 11)
Time("Auckland, New Zealand", "NZDT", 13)
'''
