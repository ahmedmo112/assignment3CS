year=int(input("year: "))
month=int(input("month: "))
day=int(input("day: "))
extraDays=int(input("days you want to add: "))
totalDays = day


def daysOfMonth(month):
    mYear = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year %4==0:
        if year % 400 ==0 or year%100!=0:
            mYear[1] = 29          
    return mYear[month-1]
    
def calc_date(month,totalDays,year):
    for i in range(1,month):
        totalDays += daysOfMonth(i)

    totalDays +=extraDays

    month=1
    x = daysOfMonth(month)

    while totalDays > x:
        totalDays-=x
        month +=1
        x = daysOfMonth(month)
        if month==12:
            month=1
            year+=1
          
    print(year,"/",month,"/",totalDays)


calc_date(month,totalDays,year)    