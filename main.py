import tkinter as tk
from login import open_login_window 

def start_application():
    root = tk.Tk()
    root.title("EMS - Main Menu")
    root.geometry("400x300")
    root.configure(bg="#2c3e50")

    # Center window
    window_width, window_height = 400, 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{window_width}x{window_height}+{int((screen_width/2)-(window_width/2))}+{int((screen_height/2)-(window_height/2))}")

    tk.Label(root, text="EMPLOYEE SYSTEM", bg="#2c3e50", fg="white", 
             font=("Arial", 18, "bold")).pack(pady=40)

    def go_to_login():
        root.destroy()        
        open_login_window()   

    tk.Button(root, text="OPEN LOGIN PAGE", command=go_to_login, 
              bg="#3498db", fg="black", font=("Arial", 12, "bold"),
              padx=20, pady=10).pack()

    root.mainloop()

if __name__ == "__main__":
    start_application()