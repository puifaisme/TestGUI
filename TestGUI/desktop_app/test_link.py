from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

import requests
import json
import time


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="#140B35")

        username_text = StringVar()
        username_label = Label(
            self, text="Username", fg="red", font=("bold", 10), padx=20
        )
        username_label.place(x=300, y=500)
        self.username_entry = Entry(self, textvariable=username_text)
        self.username_entry.place(x=350, y=500)

        password_text = StringVar()
        password_label = Label(
            self, text="Password", fg="red", font=("bold", 10), padx=20
        )
        password_label.place(x=300, y=600)
        self.password_entry = Entry(self, show="*", textvariable=password_text)
        self.password_entry.place(x=350, y=600)
        login_btn = Button(self, text="Login", fg="red", width=15, command=self.login)
        login_btn.place(x=600, y=600)

    def login(self):
        global token_out
        global username
        global password
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "":
            messagebox.showerror(
                "Required Fields", "Username/password should not be empty"
            )

        else:
            data = {"username": username, "password": password}
            try:
                response = requests.post(
                    "http://localhost:8000/api-token-auth/", data=data
                )
                response_dict = json.loads(response.text)
                token_out = response_dict["token"]
                # Link to Page 2
                p2 = Page2()
                container = Frame(self)
                container.pack(side="top", fill="both", expand=True)

                # if don't have this sentence it will create a new page
                p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

            except Exception as e:
                messagebox.showerror(
                    "Login Failure",
                    "Username/Credentials Invalid. Please try again !!!",
                )


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="#140B35")
        self.img = ImageTk.PhotoImage(
            Image.open("E:/Git/TestGUI/TestGUI/desktop_app/img/AntLogo128px.png")
        )

        position = Canvas(self, bg="#140B35", height=500, highlightthickness=0)
        position.pack()

        position.create_image((200, 300), image=self.img)

        semestry_text = StringVar()
        semestry_label = Label(self, text="Semestry", fg="orange", padx=10)
        semestry_label.place(x=250, y=385)
        self.semestry_entry = Entry(self, textvariable=semestry_text)
        self.semestry_entry.place(x=350, y=385)

        rehersal_button = Button(
            self,
            text="Rehersal",
            width=15,
            bg="#E8641A",
            fg="white",
            command=semestry,
        )
        rehersal_button.place(x=220, y=430)

        commencement_button = Button(
            self,
            text="Commencement",
            width=15,
            bg="#E8641A",
            fg="white",
            command=semestry,
        )
        commencement_button.place(x=380, y=430)

        # ----------- Loop TEST -------------
        # x = 0
        # while True:
        #     print(x)
        #     x = x + 1

        #     loop = Label(self, text="Test Loop")
        #     loop.pack()

        #     button_loop = Button(self, command=self.test_loop)
        #     button_loop.pack()

        # def test_loop(self):
        #     people_count = 0
        #     while True:

        #         # location given here
        #         people_count = people_count + 1
        #         time.sleep(10)

        #         people = Label(self)

        # username_text = StringVar()
        # username_label = Label(
        #     self, text="Username", fg="red", font=("bold", 10), padx=20
        # )
        # username_label.place(x=300, y=500)
        # self.username_entry = Entry(self, textvariable=username_text)
        # self.username_entry.place(x=350, y=500)

    def semestry():
        # save data to database
        pass


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)


class Page4(Page):
    pass


class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        # p3 = Page3(self)
        p4 = Page4(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = Button(buttonframe, text="Page 2", command=p2.lift)
        # b3 = Button(buttonframe, text="Page 3", command=p3.lift)

        # b1.pack(side="left")
        # b2.pack(side="left")
        # b3.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.resizable(width=False, height=False)
    root.title("NUB-SHOW BANDIT")
    root.geometry("700x700+0+10")

    root.mainloop()