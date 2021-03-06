from tkinter import *  # Import all classes and constants
from tkinter import messagebox  # Import a module
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passw_letter = random.choices(letters, k=random.randint(8, 10))
    passw_symb = random.choices(symbols, k=random.randint(2, 4))
    passw_numb = random.choices(numbers, k=random.randint(2, 4))
    password_list = passw_letter + passw_numb + passw_symb
    random.shuffle(password_list)
    password = ''.join(password_list)
    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askyesno(title=website, message=f"These are the details entered: \n"
                                                           f"Email: {email}\n Password: {password}")
        if is_ok:
            new_data = {
                website: {
                    "email": email,
                    "password": password,
                }
            }
            try:
                with open("data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)  # Indent is for writing in a nice format in the json file
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)  # Indent is for writing in a nice format in the json file
            finally:
                input_website.delete(0, END)
                input_password.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_website.get()
    try:
        with open("data.json", "r") as file:
        # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning!", message="No data File Found!")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email is: {data[website]['email']},\n Password is: "
                                                       f"{data[website]['password']}")
            pyperclip.copy(data[website]['password'])
        else:
            messagebox.showinfo(title=website, message=f"No details for the website {website} exists")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)  # always needs the center of the image x,y
# canvas.pack()
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_email = Label(text="Email / Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entry
input_website = Entry(width=25)
input_website.grid(column=1, row=1)
input_website.focus()  # To indicate where the cursor should start

input_email = Entry(width=43)
input_email.grid(column=1, row=2, columnspan=2)  # Columnspan indicates that takes the space of two columns
input_email.insert(0, "kata@mail.com")

input_password = Entry(width=25)
input_password.grid(column=1, row=3)

# Buttons
button_search = Button(text="Search", command=find_password, width=14)
button_search.grid(column=2, row=1)
button_generate = Button(text="Generate Password", command=generate_password, width=14)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
