import os
import sys
import tkinter as tk

from datahandler import *
price = 0.60
power = 10


def gui():
    def handle_click(event):
        os.remove("tmp.txt")
        sys.exit()

    def run(event):
        power = float(e1.get())
        price = float(e2.get())
        greeting.destroy()
        greeting2.destroy()
        greeting3.destroy()
        button.destroy()
        e1.destroy()
        e2.destroy()
        running = tk.Label(text="Porszę czekać...", width=60, height=10)
        running.pack()
        window.update()
        try:
            init()
            populate_data()
            save_data(power, price)
            visualize_data()
        except Exception as e:
            running.destroy()
            error = tk.Label(text="ERROR " + str(e), width=60, height=10)
            button3 = tk.Button(text="Zamknij!")
            button3.bind("<Button-1>", handle_click)
            error.pack()
            button3.pack()
        else:
            running.destroy()
            done = tk.Label(text="GOTOWE", width=60, height=10)
            button4 = tk.Button(text="Zamknij!")
            button4.bind("<Button-1>", handle_click)
            done.pack()
            button4.pack()

    window = tk.Tk()
    window.wm_title("Raport domowy")
    window.geometry("460x320")

    greeting = tk.Label(text="Wprowadź moc żarówki (Watt)", width=60, height=5)
    e1 = tk.Entry()
    e2 = tk.Entry()
    greeting2 = tk.Label(text="Wprowadź cenę 1kWh energii (zł)", width=60, height=5)
    greeting3 = tk.Label(text="", width=60, height=1)
    button = tk.Button(text="START")
    button.bind("<Button-1>", run)

    greeting.pack()
    e1.pack()
    e1.insert(0, power)
    greeting2.pack()
    e2.pack()
    e2.insert(0, price)
    greeting3.pack()
    button.pack()
    e1.focus_set()
    window.mainloop()


if __name__ == "__main__":
    if not os.path.exists(path):
        os.makedirs(path)
    gui()