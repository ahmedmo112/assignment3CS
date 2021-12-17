year=int(input("year: "))
month=int(input("month: "))
day=int(input("day: "))
extraDays=int(input("days you want to add: "))
totalDays = day

def checker(daysOfMonth):
    
    if 1> month >12:
        print("Please Enter a Valid Month Number!")
    elif day > daysOfMonth :
        print("Please Enter Days According To the Month Given")
    elif 1900> year > 2022 :
        print("Please Enter  Years No Earlier Than 1900 and No Later Than 2022")
    elif extraDays > 1000:
        print("Only Day Increments Of 1000 Days Maximum Allowed!")
    elif extraDays <0:
        print("Please Enter Positive Days")    
    else :
        calc_date(month,totalDays,year)        


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
    # while totalDays<0:
    #     if daysOfMonth(2)==28:
    #         totalDays=totalDays+365
    #     else:
    #         totalDays=totalDays+366
    #     year-=1

    x = daysOfMonth(month)

    while totalDays > x:
        totalDays-=x
        month +=1
        x = daysOfMonth(month)
        if month==12:
            month=1
            year+=1
          
    print(year,"/",month,"/",totalDays)


checker(daysOfMonth(month))   