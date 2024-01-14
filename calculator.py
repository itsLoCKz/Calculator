# Calculator by Adam Szcześniak

from tkinter import *

first_number = second_number = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text="")

def get_operator(oper):
    global first_number,operator

    first_number = int(result_label["text"])
    operator = oper
    result_label.config(text="")

def get_result():
    global first_number,second_number,operator

    second_number = int(result_label["text"])

    if operator == "+":
        result_label.config(text=str(first_number+second_number))
    elif operator == "-":
        result_label.config(text=str(first_number-second_number))
    elif operator == "*":
        result_label.config(text=str(first_number*second_number))
    else:
        if second_number == 0:
            result_label.config(text="Error")
        else:
            result_label.config(text=str(round(first_number/second_number,2)))



# GUI settings

window = Tk()
window.title(" Calculator by Adam Szcześniak")
window.iconbitmap("calculator.ico")
window.geometry('280x380')
window.resizable(0,0)
window.configure(bg="#252526")

result_label = Label(window,text="",bg="#252526",fg="white")
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25))
result_label.config(font=("verdana",30,"bold"))

# First row

button_7 = Button(window,text="7",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_digit(7))
button_7.grid(row=1,column=0)
button_7.config(font=("verdana",14))

button_8 = Button(window,text="8",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_digit(8))
button_8.grid(row=1,column=1)
button_8.config(font=("verdana",14))

button_9 = Button(window,text="9",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_digit(9))
button_9.grid(row=1,column=2)
button_9.config(font=("verdana",14))

button_add = Button(window,text="+",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_operator("+"))
button_add.grid(row=1,column=3)
button_add.config(font=("verdana",14))

# Second row

button_4 = Button(window,text="4",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_digit(4))
button_4.grid(row=2,column=0)
button_4.config(font=("verdana",14))

button_5 = Button(window,text="5",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_digit(5))
button_5.grid(row=2,column=1)
button_5.config(font=("verdana",14))

button_6 = Button(window,text="6",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_digit(6))
button_6.grid(row=2,column=2)
button_6.config(font=("verdana",14))

button_subtract = Button(window,text="-",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_operator("-"))
button_subtract.grid(row=2,column=3)
button_subtract.config(font=("verdana",14))

# Third row

button_1 = Button(window,text="1",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_digit(1))
button_1.grid(row=3,column=0)
button_1.config(font=("verdana",14))

button_2 = Button(window,text="2",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_digit(2))
button_2.grid(row=3,column=1)
button_2.config(font=("verdana",14))

button_3 = Button(window,text="3",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_digit(3))
button_3.grid(row=3,column=2)
button_3.config(font=("verdana",14))

button_multiplication = Button(window,text="*",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_operator("*"))
button_multiplication.grid(row=3,column=3)
button_multiplication.config(font=("verdana",14))

# Fourth row

button_clear = Button(window,text="C",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: clear())
button_clear.grid(row=4,column=0)
button_clear.config(font=("verdana",14))

button_0 = Button(window,text="0",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_digit(0))
button_0.grid(row=4,column=1)
button_0.config(font=("verdana",14))

button_equals = Button(window,text="=",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_result())
button_equals.grid(row=4,column=2)
button_equals.config(font=("verdana",14))

button_divide = Button(window,text="/",bg="#1e1e1e",fg="white",width=5,height=2,command=lambda: get_operator("/"))
button_divide.grid(row=4,column=3)
button_divide.config(font=("verdana",14))


window.mainloop()