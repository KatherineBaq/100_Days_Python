from tkinter import *
FONT = ("Arial", 24, "normal")
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)
#Label
my_label = Label(text="I am a label", font=FONT)
#my_label.pack()
#my_label["text"] = "New Text"
my_label.config(text="is equal to", font=FONT)
my_label.grid(column=0, row=1)

# Second label result
label_result = Label(text="0", font=FONT)
label_result.grid(column=1, row=1)

#Third label km
label_km = Label(text="Km", font=FONT)
label_km.grid(column=2, row=1)

#Fourth label Miles
label_miles = Label(text="Miles", font=FONT)
label_miles.grid(column=2, row=0)
# Button

def button_calculate():
    label_result.config(text=f"{float(inputw.get())*1.609}")

button = Button(text="Calculate", command=button_calculate, font=FONT)
#button.pack()
button.grid(column=1, row=2)

# Entry component (it is an input)

inputw = Entry(width=7, font=FONT)
#inputw.pack()
inputw.grid(column=1, row=0)



window.mainloop()