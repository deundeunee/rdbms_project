from tkinter import messagebox, ttk
import tkinter as tk
from map import Map
from connection import connectDB, executeCommand


class Login(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        middle_frame = parent.get_frame("main").middle_frame

        # 사용자 id와 password를 저장하는 변수 생성
        user_id, password = tk.StringVar(), tk.StringVar()

        def check_login():
            db, cursor = connectDB("project")
            result = executeCommand(
                db, cursor, "SELECT password FROM user WHERE (id = '" + user_id.get() + "')"
            )
            try:
                if result[0][0] == password.get():
                    messagebox.showinfo("Success", "Login Success!")
                    parent.navigate_frame.create_index(parent)
            except:
                messagebox.showinfo("Fail", "Invalid id or password.")

        def check_signup():
            try:
                db, cursor = connectDB("project")
                cursor.execute(
                    "CREATE TABLE if not exists user(id VARCHAR(255) PRIMARY KEY, password VARCHAR(255))"
                )
                query = "insert into user (id, password) values (%s,%s)"
                cursor.execute(query, (user_id.get(), password.get()))
                db.commit()
                messagebox.showinfo("Success", "You are now signed up!")
            except:
                messagebox.showinfo("Fail", "Input is invalid or the id is already taken.")

        ttk.Label(middle_frame, text="Username : ").grid(row=1, column=1, padx=10, pady=10)
        ttk.Label(middle_frame, text="Password : ").grid(row=2, column=1, padx=10, pady=10)
        ttk.Entry(middle_frame, textvariable=user_id).grid(
            row=1, column=2, columnspan=2, padx=10, pady=10
        )
        ttk.Entry(middle_frame, textvariable=password).grid(
            row=2, column=2, columnspan=2, padx=10, pady=10
        )
        ttk.Button(middle_frame, text="Login", command=check_login).grid(
            row=3, column=2, columnspan=1, padx=10, pady=10
        )
        ttk.Button(middle_frame, text="Sign-up", command=check_signup).grid(
            row=3, column=3, columnspan=1, padx=10, pady=10
        )
        middle_frame.rowconfigure(0, weight=1)
        middle_frame.rowconfigure(4, weight=1)
        middle_frame.columnconfigure(0, weight=1)
        middle_frame.columnconfigure(4, weight=1)
