#import 
import requests
from tkinter import *
import smtplib
from getpass import getpass
from datetime import datetime,timedelta

#input the link,so you can change the easily
daily_link = input ("API Link :")
main_link = input("Main Link : ")
#request_api:
response = requests.get(daily_link)
response.raise_for_status()

a = response.json()
types = [typ for typ in a] 

#Tkinter Window 

window = Tk()
window.title("Today Book Review At Openlibrary")
window.config(padx=50, pady=50)


# show book info
choice = StringVar()
choice.set('title')
selects = OptionMenu(window,choice,*types)
selects.config(width=7,anchor=S,pady=10)
selects.grid(row=1, column=1)
#built click fiction 
def click():
    review = choice.get()
    response = requests.get(daily_link)
    response.raise_for_status()
 
    a = response.json()
 
    print(a)
    #print(review)
 
    """ MADE CHANGES BELOW """
    if review in types:
        reviews = a[review]
        result = "\n".join(reviews)
        
        book_lable.config(text=result,font=("Arial", 20,"bold"))
        return True
    else:
        return False


#Tk Lable(Wirte Output Text)

book_lable = Label(text="Today Book Review At Openlibrary",font=("Arial", 20,"bold"))
book_lable.grid(row=0, column=0, columnspan=2, sticky="w", pady=10)


# #book button
book_button = Button(text="check it today review",command=click)
book_button.grid(row=1, column=0, columnspan=1, sticky="w",pady=0,padx=80 )
#Information Location
def information_Location():
    book_info = Label(text=f"All Information Are From Openlibrary\n{main_link }",font=("Arial", 10,"bold"))
    book_info.grid(row=2,column=0,  columnspan=1, sticky="w", pady=0,padx=0)
information_Location()

window.mainloop()

#change the daily review

def send_mail():
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(sender, password)
    connection.sendmail(sender,receiver,f"Subject:Time To Chang Today review")
today = datetime.today()
yesterday = today - timedelta(days = 1)
if   today != yesterday :
        sender = input("Email : ")
        password = getpass()
        receiver = input("Email : ")
        send_mail() 
        print("ok")
else:
    print("You don't need to change it now")



