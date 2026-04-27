import tkinter as tk
import emp
from employee import EmployeeManagementSystem

def open_dashboard(login_window):
    dash = tk.Toplevel(login_window)
    # We let the EmployeeManagementSystem handle the title/geometry 
    # but we ensure the database is ready first.
    emp.create_table()

    # --- 1. BOTTOM LOGOUT BAR ---
    # We pack this FIRST with side="bottom" so it stays anchored at the base
    bottom_bar = tk.Frame(dash, bg="#2c3e50")
    bottom_bar.pack(fill="x", side="bottom")

    def logout():
        dash.destroy()
        login_window.deiconify()

    btn_logout = tk.Button(
        bottom_bar, 
        text="LOGOUT", 
        bg="#e74c3c", 
        fg="black", 
        font=("Arial", 10, "bold"),
        command=logout,
        width=12,
        height=1,
        relief="raised",
        cursor="hand2"
    )
    btn_logout.pack(side="right", padx=20, pady=15)

    # --- 2. LOAD EMPLOYEE SYSTEM ---
    # We pass 'dash' (the Toplevel window) so your class can 
    # successfully call self.root.title() without crashing.
    app = EmployeeManagementSystem(dash)

def open_login_window():
    root = tk.Tk()
    root.title("EMS - Secure Login")
    root.geometry("400x500")
    root.configure(bg="#2c3e50")

    # Center window logic
    window_width, window_height = 400, 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{window_width}x{window_height}+{int((screen_width/2)-(window_width/2))}+{int((screen_height/2)-(window_height/2))}")

    def login():
        username = entry_user.get()
        password = entry_pass.get()

        if username == "admin" and password == "1234":
            root.withdraw()
            open_dashboard(root)
        else:
            error_label.config(text="Invalid Username or Password")

    # --- UI LAYOUT ---
    main_frame = tk.Frame(root, bg="#ecf0f1", padx=30, pady=30)
    main_frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=420)

    tk.Label(main_frame, text="SYSTEM LOGIN", bg="#ecf0f1", fg="#2c3e50", 
             font=("Arial", 18, "bold")).pack(pady=(10, 30))

    tk.Label(main_frame, text="USERNAME", bg="#ecf0f1", fg="#7f8c8d", 
             font=("Arial", 9, "bold")).pack(anchor="w", padx=5)
    entry_user = tk.Entry(main_frame, font=("Arial", 12), bg="white", fg="black",
                          insertbackground="black", relief="solid", borderwidth=1)
    entry_user.pack(fill="x", pady=(5, 20), ipady=8)
    entry_user.insert(0, "admin")

    tk.Label(main_frame, text="PASSWORD", bg="#ecf0f1", fg="#7f8c8d", 
             font=("Arial", 9, "bold")).pack(anchor="w", padx=5)
    entry_pass = tk.Entry(main_frame, font=("Arial", 12), bg="white", fg="black",
                          insertbackground="black", relief="solid", borderwidth=1, show="●")
    entry_pass.pack(fill="x", pady=(5, 5), ipady=8)

    error_label = tk.Label(main_frame, text="", fg="#e74c3c", bg="#ecf0f1", font=("Arial", 9))
    error_label.pack(pady=5)

    btn_login = tk.Button(main_frame, text="SIGN IN", command=login, 
                          bg="#3498db", fg="black", 
                          font=("Arial", 12, "bold"), 
                          highlightbackground="#ecf0f1", 
                          padx=20, pady=10)
    btn_login.pack(fill="x", pady=20)

    tk.Label(main_frame, text="EMS v2.0", bg="#ecf0f1", fg="#bdc3c7", 
             font=("Arial", 8)).pack(side="bottom")

    root.mainloop()