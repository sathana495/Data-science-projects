
#This code demonstrates the use of three Python modules:
#calendar, datetime, and os. It also includes an example of using the pywhatkit module to send a WhatsApp message.
#calendar module
import calendar as c
print(c.calendar(2024))#its printing the calendar of 2024
print(c.month(2024, 6))#its printing the calendar of june 2024
print(c.monthrange(2026, 5))#its printing the first day of the month and the number of days in june 2024
print(c.weekday(2024, 6, 1))#its printing the day of the week for june 1, 2024 (0: Monday, 1: Tuesday, 2: Wednesday, 3: Thursday, 4: Friday, 5: Saturday, 6: Sunday)
print(c.isleap(2026))#its checking if 2026 is a leap year or not (True: leap year, False: not a leap year)
print(c.month_name[1])#its printing the name of the month for the given month number (1: January, 2: February, ..., 12: December)
print(c.day_name[0])#its printing the name of the day for the given day number 
c.setfirstweekday(c.SUNDAY)#its setting the first day of the week to Sunday
print(c.firstweekday())
print(c.weekheader(3))#its printing the header for the week with 3 characters


#Datetime module
import datetime as dt
print(dt.datetime.now())#its printing the current date and time
print(dt.date.today())#its printing the current date
print(dt.datetime(2024, 6, 1))#its creating a datetime object for June 1, 2024
print(dt.date(2024, 6, 1))#its creating a date object for June 1, 2024
print(dt.datetime(2024, 6, 1, 12, 30, 0))#its creating a datetime object for June 1, 2024 at 12:30:00
print(dt.datetime.now().year)#its printing the current year 
print(dt.datetime.now().month)#its printing the current month
print(dt.datetime.now().day)#its printing the current day   
print(dt.datetime.now().hour)#its printing the current hour
print(dt.datetime.now().minute)#its printing the current minute
print(dt.datetime.now().second)#its printing the current second
print(dt.datetime.now().microsecond)#its printing the current microsecond


#os module
import os
print(os.getcwd())#its printing the current working directory
print(os.listdir())#its printing the list of files and directories in the current working directory
print(os.path.exists('LW_Lab_4.py'))#its checking if the file 'LW_Lab_4.py' exists in the current working directory (True: exists, False: does not exist)
print(os.path.isfile('LW_Lab_4.py'))#its checking if 'LW_Lab_4.py' is a file (True: is a file, False: is not a file)
print(os.path.isdir('LW_Lab_4.py'))#its checking if 'LW_Lab_4.py' is a directory (True: is a directory, False: is not a directory)

#pywhatkit module
import pywhatkit as pw
pw.sendwhatmsg('+918754787921', 'Hello, this is a test message!')#its sending a WhatsApp message to the specified phone number 
pw.sendwhatmsg('+918754787921', 'Hello, this is a test message!', 15, 30)#its sending a WhatsApp message to the specified phone number at the specified time (15:30 in this case) 
pw.sendwhatmsg('+918754787921', 'Hello, this is a test message!', 15, 30, 10)#its sending a WhatsApp message to the specified phone number at the specified time (15:30 in this case) with a wait time of 10 seconds before sending the message
pw.search('Python programming')#its searching for 'Python programming' on the web
pw.playonyt('Python programming tutorial')#its playing a YouTube video for 'Python programming tutorial'  