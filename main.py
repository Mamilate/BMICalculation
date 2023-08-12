import tkinter

window = tkinter.Tk()
window.title("BMI Calculation")
window.minsize(width=300,height=300)

font = ("Arial",10,"normal")

my_label = tkinter.Label(text="Enter Your Weight (kg)",font=font)
my_label.pack()

def sa():
    weight = my_entry.get()
    height = my_entry1.get()

    if weight =="" or height =="":
        my_result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / ((float(height)/100) **2)
            result_string = write_result(bmi)
            my_result_label.config(text=result_string)
        except:
            my_result_label.place(x=90,y=150)
            my_result_label.config(text="Enter a valid number!")



my_entry = tkinter.Entry()
my_entry.pack()

my_label1 = tkinter.Label(text="Enter Your Height (cm)",font=font)
my_label1.place(x=80,y=50)

my_entry1 = tkinter.Entry()
my_entry1.place(x=87,y=75)

my_button = tkinter.Button(text="Calculate",command=sa)
my_button.place(x=120,y=110)

my_result_label = tkinter.Label()
my_result_label.place(x=75,y=150)

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string

window.mainloop()