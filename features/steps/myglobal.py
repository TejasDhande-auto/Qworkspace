email= "opsqdev2021@outlook.com"
password= "Quantuvos@123"
URL= "https://platform-dev.quantuvos.com/login"
TEMPURL= "https://temp-mail.org/en/"

#Calendar Things gmail
from datetime import date,timedelta
today = date.today()+timedelta(1)                 #tommorrow date
day = str(today.day)                              #int-stringconversion
month = today.strftime("%b")                      #int-stringconversion
year = str(today.year)                            #int-stringconversion

startdate = month+" "+day+","+" "+year            #gmaildateformat
enddate = month+" "+day+","+" "+year              #gmaildateformat

########################################################

