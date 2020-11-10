from tkinter import *
from PIL import ImageTk, Image

window = Tk()

img = ImageTk.PhotoImage(
    Image.open("E:/Git/TestGUI/TestGUI/desktop_app/img/AntLogo128px.png")
)
position = Canvas(window, bg="#140B35", height=500, highlightthickness=0)
position.pack()

position.create_image((200, 300), image=img)

add_btn = Button(window, text="Rehersal", width=15, bg="#E8641A", fg="white")
add_btn.place(x=220, y=400)

remove_btn = Button(window, text="Commencement", width=15, bg="#E8641A", fg="white")
remove_btn.place(x=380, y=400)


window.configure(bg="#140B35")
window.resizable(width=False, height=False)
window.title("NUB-SHOW BANDIT")
window.geometry("700x700+0+10")

window.mainloop()