# * only imports classes and attributes
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for item in range(randint(8, 10))]
    password_numbers = [choice(numbers) for item in range(randint(2,4))]
    password_symbols = [choice(symbols) for item in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    gen_password="".join(password_list)
    password_ent.insert(0, gen_password)
    pyperclip.copy(gen_password)


# ---------------------------- SAVE AND SEARCH PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_ent.get()
    new_data = {website: {
        "email": email,
        "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as f:

                #Reading old data
                data = json.load(f)
                #Updating old data with new data
                data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
                website_entry.delete(0, END)
                password_ent.delete(0, END)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
                website_entry.delete(0, END)
                password_ent.delete(0, END)

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as f:
            # Reading old data
            data = json.load(f)
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']} \n Password:{data[website]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Password file does not exist")
    except KeyError:
        messagebox.showinfo(title="Oops", message="Password for that website does not exist..Please create one")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)
# image
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,  100, image=logo_img)
canvas.grid(column=1, row=0)

# Text widgets

# website text
website_text = Label(text="Website")
website_text.grid(column=0, row=1)
# email/user text
email_user_text = Label(text="Email/Username:")
email_user_text.grid(column=0, row=2)
# password text
password = Label(text='Password')
password.grid(column=0, row=3)

# Button widgets

# generate password button
pass_button = Button(text="Generate Password", command=gen_pass)
pass_button.grid(column=2,row=3)
# add button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
# search button
search_button = Button(text="Search", width=13, command=search)
search_button.grid(column=2, row=1)

# Entry Widgets

# website
website_entry = Entry()
website_entry.grid(column=1, row=1)
website_entry.focus()
# email and user
email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "jaganlidder@gmail.com")
# pass
password_ent = Entry()
password_ent.grid(column=1, row=3)









window.mainloop()

