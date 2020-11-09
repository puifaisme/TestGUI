import tkinter as tk
from PIL import ImageTk, Image

path = 'C:/Users/Chonticha Sae-jiw/Desktop/TestGUI/desktop_app/img/AntLogo128px.png'

window = tk.Tk()

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
window.mainloop()

add_btn = tk.Button(window, text='Rehersal', width=15)
add_btn.grid(row=3, column=9)

remove_btn = tk.Button(window, text='Commencement', width=15)
remove_btn.grid(row=3, column=10)

window.configure(bg='#140B35')
window.title('NUB-SHOW BANDIT')
window.geometry('750x350')

window.mainloop()