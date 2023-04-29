import tkinter as tk
import time

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)

root = tk.Tk()
root.title('专注时钟')

clock = tk.Label(root, font=('times', 100, 'bold'), bg='white')
clock.pack(fill=tk.BOTH, expand=1)

tick()

root.mainloop()
