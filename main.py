import tkinter as tk
from win32api import GetSystemMetrics

window = tk.Tk()

x_size = 500
y_size = 500
width_icon = int((GetSystemMetrics(0) - x_size) / 2)
height_icon = int((GetSystemMetrics(1) - y_size) / 2)
# ОБЯЗАТЕЛЬНО НУЖНО ВСТАВИТЬ СВОЙ ПУТЬ К ФАЙЛУ
window.iconbitmap("C:/Users/Вадим/Downloads/Calculator_30001.ico")
entry = tk.Entry(window, background="black", foreground="white", font=('Arial Black', 40), justify="right")
label = tk.Label(window, background="black", foreground="white", font=('Arial Black', 40), anchor="ne")
entry.place(x=0, y=100, width=x_size, height=(y_size/2)-100)
label.place(x=0, y=0, width=x_size, height=(y_size/2)-150)


# GetSystemMetrics(0)-ширина(width)
# GetSystemMetrics(1)-высота(height)
def visual():
    window.title("Калькулятор")
    window.geometry(f"{x_size}x{y_size}+{width_icon}+{height_icon}")
    window.configure(background="black")

    btndelete = tk.Button(window, background="#778899", foreground="white", borderwidth=5, text="C", command=message_clear)
    btndelete.place(x=0, y=y_size/2, width=x_size/4, height=y_size/10)
    btnpercent = tk.Button(window, background="#778899", foreground="white", borderwidth=5, text="%", command=lambda : message_input("%"))
    btnpercent.place(x=x_size/4, y=y_size/2, width=x_size/4, height=y_size/10)
    btndeleteonesymbol = tk.Button(window, background="#778899", foreground="white", borderwidth=5, text="<<", command=message_clear_one_symbol)
    btndeleteonesymbol.place(x=x_size/2, y=y_size/2, width=x_size/4, height=y_size/10)
    btndivision = tk.Button(window, background="#778899", foreground="white", borderwidth=5, text="/", command=lambda : message_input("/"))
    btndivision.place(x=(x_size/4)*3, y=y_size/2, width=x_size/4, height=y_size/10)

    btn7 = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text="7", command=lambda : message_input("7"))
    btn7.place(x=0, y=y_size/2+y_size/10, width=x_size/4, height=y_size/10)
    btn8 = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text="8", command=lambda : message_input("8"))
    btn8.place(x=x_size/4, y=y_size/2+y_size/10, width=x_size/4, height=y_size/10)
    btn9 = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text="9", command=lambda : message_input("9"))
    btn9.place(x=x_size/2, y=y_size/2+y_size/10, width=x_size/4, height=y_size/10)
    btnmultiplication = tk.Button(window, background="#778899", foreground="white", borderwidth=5, text="*", command=lambda : message_input("*"))
    btnmultiplication.place(x=(x_size/4)*3, y=y_size/2+y_size/10, width=x_size/4, height=y_size/10)

    btn4 = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text="4", command=lambda : message_input("4"))
    btn4.place(x=0, y=y_size/2+y_size/10+y_size/10, width=x_size/4, height=y_size/10)
    btn5 = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text="5", command=lambda : message_input("5"))
    btn5.place(x=x_size/4, y=y_size/2+y_size/10+y_size/10, width=x_size/4, height=y_size/10)
    btn6 = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text="6", command=lambda : message_input("6"))
    btn6.place(x=x_size/2, y=y_size/2+y_size/10+y_size/10, width=x_size/4, height=y_size/10)
    btnminus = tk.Button(window, background="#778899", foreground="white", borderwidth=5, text="-", command=lambda : message_input("-"))
    btnminus.place(x=(x_size/4)*3, y=y_size/2+y_size/10+y_size/10, width=x_size/4, height=y_size/10)

    btn1 = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text="1", command=lambda : message_input("1"))
    btn1.place(x=0, y=y_size/2+y_size/10+y_size/10+y_size/10, width=x_size/4, height=y_size/10)
    btn2 = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text="2", command=lambda : message_input("2"))
    btn2.place(x=x_size/4, y=y_size/2+y_size/10+y_size/10+y_size/10, width=x_size/4, height=y_size/10)
    btn3 = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text="3", command=lambda : message_input("3"))
    btn3.place(x=x_size/2, y=y_size/2+y_size/10+y_size/10+y_size/10, width=x_size/4, height=y_size/10)
    btnplus = tk.Button(window, background="#778899", foreground="white", borderwidth=5, text="+", command=lambda : message_input("+"))
    btnplus.place(x=(x_size/4)*3, y=y_size/2+y_size/10+y_size/10+y_size/10, width=x_size/4, height=y_size/10)

    btn00 = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text="00", command=lambda : message_input("00"))
    btn00.place(x=0, y=y_size/2+y_size/10+y_size/10+y_size/10+y_size/10, width=x_size/4, height=y_size/10)
    btn0 = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text="0", command=lambda : message_input("0"))
    btn0.place(x=x_size/4, y=y_size/2+y_size/10+y_size/10+y_size/10+y_size/10, width=x_size/4, height=y_size/10)
    btncomma = tk.Button(window, background="#696969", foreground="white", borderwidth=5, text=".", command=lambda : message_input("."))
    btncomma.place(x=x_size/2, y=y_size/2+y_size/10+y_size/10+y_size/10+y_size/10, width=x_size/4, height=y_size/10)
    btnresult = tk.Button(window, background="#D2691E", foreground="white", borderwidth=5, text="=", command=print_result)
    btnresult.place(x=(x_size/4)*3, y=y_size/2+y_size/10+y_size/10+y_size/10+y_size/10, width=x_size/4, height=y_size/10)


def message_input(symbol):
    entry.insert(tk.END, symbol)


def message_clear():
    entry.delete(0, tk.END)


def message_clear_one_symbol():
    entry.delete(len(entry.get())-1, tk.END)


def print_result():
    text = entry.get()
    result = 0
    check = True
    if "%" in text:
        if "+" in text:
            text_split = text.split("+")
            percent = float(text_split[1].replace("%", ""))
            result = float(text_split[0]) + (float(text_split[0]) * percent / 100)
        elif "-" in text:
            text_split = text.split("-")
            percent = float(text_split[1].replace("%", ""))
            result = float(text_split[0]) - (float(text_split[0]) * percent / 100)
        elif "*" in text:
            text_split = text.split("*")
            percent = float(text_split[1].replace("%", ""))
            result = float(text_split[0]) * (float(text_split[0]) * percent / 100)
        elif "/" in text:
            text_split = text.split("/")
            percent = float(text_split[1].replace("%", ""))
            if percent == 0:
                check = False
            result = float(text_split[0]) / (percent / 100)
        else:
            percent = 100 / float(text.split("%")[1])
            result = float(text.split("%")[0]) / percent
    else:
        checking_error = 0
        if "+" in text:
            checking_error = checking_error + 1
            if checking_error > 1:
                check = False
            else:
                result = float(text.split("+")[0]) + float(text.split("+")[1])
        elif "-" in text:
            checking_error = checking_error + 1
            if checking_error > 1:
                check = False
            else:
                result = float(text.split("-")[0]) - float(text.split("-")[1])
        elif "*" in text:
            checking_error = checking_error + 1
            if checking_error > 1:
                check = False
            else:
                result = float(text.split("*")[0]) * float(text.split("*")[1])
        elif "/" in text:
            checking_error = checking_error + 1
            if checking_error > 1:
                check = False
            else:
                if float(text.split("/")[1]) != 0:
                    result = float(text.split("/")[0]) / float(text.split("/")[1])
                else:
                    check = False

    if result % 1 == 0:
        result = int(result)

    message_clear()
    if check:
        message_input(result)
        label["text"] = entry.get()
    else:
        message_input("ERROR")


def main():
    visual()
    window.mainloop()


if __name__ == "__main__":
    main()
