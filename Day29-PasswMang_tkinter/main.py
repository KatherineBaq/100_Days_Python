from tkinter import * #Import all classes and constants
from tkinter import messagebox #Import a module


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    if len(website) == 0 | len(email) == 0 | len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askyesno(title=website, message=f"These are the details entered: \n"
                                               f"Email: {email}\n Password: {password}")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            input_website.delete(0, END)
            input_password.delete(0, END)


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
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)  # Columnspan indicates that takes the space of two columns
input_website.focus()  # To indicate where the cursor should start

input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2)  # Columnspan indicates that takes the space of two columns
input_email.insert(0, "kata@mail.com")

input_password = Entry(width=21)
input_password.grid(column=1, row=3)

# Buttons
button_generate = Button(text="Generate Password", command="")
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
