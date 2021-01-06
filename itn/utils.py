from datetime import datetime, timedelta
from calendar import HTMLCalendar

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
    
    def formatday(self, day):
        if day != 0:
            return day
        return None
    
    def formatweek(self, theweek):
        week = []
        for d, weekday in theweek:
            week.append(self.formatday(d))
        return week
    
    def formatmonth(self, withyear=True):
        cal = []
        # cal.append(self.formatweekheader())
        # for week in self.monthdays2calendar(self.year, self.month):
        #     weeks = {}
        #     days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        #     for day, date in zip(days,self.formatweek(week)):
        #         weeks[day] = date
        #     cal.append(weeks)        
        for week in self.monthdays2calendar(self.year, self.month):
            cal.append(self.formatweek(week))
        return cal