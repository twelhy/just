import tkinter as tk
from tkinter import messagebox

# 1. Функцияны анықтау (Батырма басылғанда іске асатын әрекет)
def show_message():
    answer = ans.get()
    if answer == "Hello":
        messagebox.showinfo("Хабарлама", "Good job")
    else:
        messagebox.showinfo("Error", "Please Enter 'Hello'")
    greeting.destroy()

# 2. Негізгі терезені (root) жасау
root = tk.Tk()
root.title("Менің Бірінші Қолданбам") # Терезе тақырыбы
root.geometry("400x200")              # Терезе өлшемі (енxбиік)

# 3. Label (Белгі) жасау
greeting = tk.Label(root, text="Сәлем!")
greeting.pack(pady=20) # 'pack' виджетті терезеге орналастырады

ans =tk.Entry(root)
ans.pack()

# 4. Button (Батырма) жасау
my_button = tk.Button(root, 
                      text="Мені Басыңыз", 
                      command=show_message) # 'command' функцияны көрсетеді
my_button.pack()

# 5. Қолданбаның оқиға циклін іске қосу
# Бұл терезені экранда ұстап тұрады және оқиғаларды (тышқанды басу) тыңдайды.
root.mainloop()