import tkinter as tk

def add_numbers():
    
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
    
        result = num1 + num2
        
        result_win = tk.Toplevel(win)
        icon = tk.PhotoImage(file='calculator.png')
        result_win.iconphoto(False, icon)
        result_win.title("Ответ")
        result_win.geometry("250x250+600+300")
        result_win.resizable(True,False)
        result_label = tk.Label(result_win, text=f"Сумма чисел {num1} и {num2} равна {result}")
        result_label.pack()
    except ValueError:
        
        error_label = tk.Label(win, text="Введите целые числа")
        error_label.pack()


win = tk.Tk()
icon = tk.PhotoImage(file='calculator.png')
win.iconphoto(False, icon)
win.config(bg='#DBDFEA')
win.geometry("200x200+550+200")
win.resizable(False,False)
win.title("Калькулятор")

entry1 = tk.Entry(win)
entry1.pack()
entry2 = tk.Entry(win)
entry2.pack()

button = tk.Button(win, text="Посчитать", command=add_numbers)
button.pack()

win.mainloop()