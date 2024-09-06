from tkinter import *
window=Tk()
window.title("Miles to Kilometer convertor")
window.minsize(width=300, height=200)
window.config(padx=60,pady=50)

def calculate():
    miles=float(input.get())
    km=round(miles * 1.689)
    result.config(text=f"{km}")

label1=Label(text="Miles",font=("Gibson",18))
label1.grid(column=3,row=1)

label2=Label(text="is equal to ", font=("Gibson",18))
label2.grid(column=1,row=2)

label3=Label(text="Km",font=("Gibson",18))
label3.grid(column=3,row=2)

result=Label(text="0",font=("Gibson",18))
result.grid(column=2,row=2)

input=Entry(width=20)
print(input.get())
input.grid(column=2,row=1)

calculate_button=Button(text="Calculate",command=calculate)
calculate_button.grid(column=2,row=3)

window.mainloop()