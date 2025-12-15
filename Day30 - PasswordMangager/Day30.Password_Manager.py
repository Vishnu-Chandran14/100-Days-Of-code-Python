import os
import random
from tkinter import *
from tkinter import messagebox
import json



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


#-----------CONSTANTS------------#
FONT = ("Courier", 10)
JSON_FILE_PATH = os.path.join("save_data.json")

#------------generate password----#
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    user_letters = random.randint(4, 6)
    user_numbers = random.randint(3, 4)
    user_symbols = random.randint(2, 3)

    password_letters = [random.choice(letters) for letter in range(user_letters)]
    password_numbers = [random.choice(numbers) for numeer in range(user_numbers)]
    password_symbols = [random.choice(symbols) for symbol in range(user_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    new_password = "".join(password_list)
    password_entry.insert(0, new_password)
    

#-----------------------------SAVE PASSWORD--------------------------------#
def save():

    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        web : {
            "email" : email,
            "password" : password
        }
    }



    if len(web) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Missing Error", message="Please don't any fiels are blanks!")
    else:
        is_ok = messagebox.askokcancel(title="User details", message= "Press 'OK' to save" )

        if is_ok:
            try:
                with open(JSON_FILE_PATH, "r") as data:
                    dt = json.load(data)
            except FileNotFoundError:
                with open(JSON_FILE_PATH, "w") as data:
                    json.dump(new_data, data, indent= 4)
            else:
                with open(JSON_FILE_PATH, "w") as data:
                    dt.update(new_data)
                    json.dump(dt, data, indent= 4)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')

            







#-----------------------------------UI setting-------------------------------#
#------------------logo image setting----------------------#
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file=os.path.join("image", "logo.png"))
canvas.create_image(100, 100, image = logo_image)
canvas.grid(column=1, row=0)

#--------label creations-------------#
website_label = Label(text="Website:", font= FONT)
website_label.grid(column=0, row=1)

email_label = Label(text="Email:", font= FONT)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font= FONT)
password_label.grid(column=0, row=3)

#--------entry creations-------------#

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, pady=10, sticky="w")

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, pady=10, columnspan=2, sticky="we")
email_entry.insert(0, "vishnu142000@gmail.com")

password_entry = Entry(width=38)
password_entry.grid(column=1, row=3, pady=10, sticky="w")


#--------button creations-------------#

search_button = Button(text="Search", width=13)
search_button.grid(column=2, row=1)

password_button = Button(text="Generate Password", width=15, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=12, command=save)
add_button.grid(column=1, row=4, sticky="we", columnspan=2)








window.mainloop()