from datetime import date,timedelta



for i in range(1,8):
    print(i)

    today = date.today()+timedelta(i)                 #tommorrow date
    day = str(today.day)                              #int-stringconversion
    month = today.strftime("%b")                      #int-stringconversion
    year = str(today.year)                            #int-stringconversion

    startdate = month+" "+day+","+" "+year            #gmaildateformat
    enddate = month+" "+day+","+" "+year              #gmaildateformat
    title=""
    starttime=""
    endtime=""


    if i==1:
        title = "Single Event  7-8 am"
        starttime= "7.00am"
        endtime = "8.00am"


    elif i==2:
        title = "Single Event  8-9 am"
        starttime = "8.00am"
        endtime = "9.00am"

    elif i==3:
        title = "Single Event  9-10 am"
        starttime = "9.00am"
        endtime = "10.00am"

    elif i==4:
        title = "Single Event  10-11 am"
        starttime = "10.00am"
        endtime = "11.00am"

    print(title,starttime,endtime)




