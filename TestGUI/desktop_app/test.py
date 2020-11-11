from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


# def connected():
# เขียนว่าถ้าเปิดหน้าเว็บขึ้นมาแล้วจะขึ้นว่า connected complete ถ้าไม่ก็ไม่มีอะไรขึ้น
#     pass
# -------------------- ไม่แน่ใจอาจจะไม่ต้องมี -----------------------------


def login():
    # ดูที่ usr:pass ว่าเป็นของมหาวิทยาลัยอะไร // ไปแก้ที่ django ให้มีกรอก university
    # คนละหน้ากับหน้าแรก
    global token_out
    global username
    global password
    username = username_entry.get()
    password = password_entry.get()
    if username == "" or password == "":
        messagebox.showerror("Required Fields", "Username/password should not be empty")

    else:
        data = {"username": username, "password": password}
        try:
            response = requests.post("http://localhost:8000/api-token-auth/", data=data)
            response_dict = json.loads(response.text)
            token_out = response_dict["token"]

        except Exception as e:
            messagebox.showerror(
                "Login Failure", "Username/Credentials Invalid. Please try again !!!"
            )
        retrieve_list()
    pass


def Rehersal():
    text = Label(text="LOVE YOU")
    text.pack()
    pass


window = Tk()

img = ImageTk.PhotoImage(
    Image.open("E:/Git/TestGUI/TestGUI/desktop_app/img/AntLogo128px.png")
)
position = Canvas(window, bg="#140B35", height=500, highlightthickness=0)
position.pack()

position.create_image((200, 300), image=img)

add_btn = Button(
    window, text="Rehersal", width=15, bg="#E8641A", fg="white", command=Rehersal
)
add_btn.place(x=220, y=400)

remove_btn = Button(window, text="Commencement", width=15, bg="#E8641A", fg="white")
remove_btn.place(x=380, y=400)

# username_text = StringVar()
# username_label = Label(window, text="Username", fg="red", font=("bold", 10), padx=20)
# username_label.place(x=300, y=500)
# username_entry = Entry(window, textvariable=username_text)
# username_entry.place(x=350, y=500)


# password_text = StringVar()
# password_label = Label(window, text="Password", fg="red", font=("bold", 10), padx=20)
# password_label.place(x=300, y=600)
# password_entry = Entry(window, show="*", textvariable=password_text)
# password_entry.place(x=350, y=600)

# login_btn = Button(window, text="Login", fg="red", width=15, command=login)
# login_btn.place(x=600, y=600)


window.configure(bg="#140B35")
window.resizable(width=False, height=False)
window.title("NUB-SHOW BANDIT")
window.geometry("700x700+0+10")

window.mainloop()