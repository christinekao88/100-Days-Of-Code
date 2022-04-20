from tkinter import *

def miles_to_km():
    miles = input.get()
    # 利用config來改變文本屬性(*也可以利用fstring再改成string)
    km_result.config(text=float(miles)*1.6093)

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

#Label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

#Entry
input = Entry(width=7)
input.grid(column=1, row=0)

window.mainloop()