import tkinter as tk
from tkinter import ttk, messagebox
import emp 

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("EMS - Management Dashboard")
        self.root.geometry("1200x800")
        self.root.configure(bg="#2c3e50") # Dark background for the whole window

        emp.create_table()

        # ─── TOP HEADER ────────────────────────
        header = tk.Frame(self.root, bg="#1a252f", height=60)
        header.pack(side="top", fill="x")
        
        tk.Label(header, text="EMPLOYEE MANAGEMENT SYSTEM", bg="#1a252f", 
                 fg="white", font=("Arial", 16, "bold")).pack(pady=15, padx=20, side="left")

        # ─── SIDEBAR (FORM) ────────────────────
        sidebar = tk.Frame(self.root, bg="#ecf0f1", width=350) # Light gray sidebar
        sidebar.pack(side="left", fill="y", padx=10, pady=10)
        sidebar.pack_propagate(False)

        tk.Label(sidebar, text="Register Employee", bg="#ecf0f1", fg="#2c3e50", 
                 font=("Arial", 13, "bold")).pack(pady=20)

        # Form Helper Function - FORCING COLORS HERE
        def create_label_entry(parent, label_text):
            tk.Label(parent, text=label_text, bg="#ecf0f1", fg="#2c3e50", font=("Arial", 9, "bold")).pack(anchor="w", padx=25)
            # Forced bg="white" and fg="black"
            entry = tk.Entry(parent, font=("Arial", 11), bg="white", fg="black", 
                            insertbackground="black", relief="solid", borderwidth=1)
            entry.pack(fill="x", padx=25, pady=(5, 15), ipady=5)
            return entry

        self.fname = create_label_entry(sidebar, "FIRST NAME")
        self.lname = create_label_entry(sidebar, "LAST NAME")
        self.age = create_label_entry(sidebar, "AGE")
        self.dept = create_label_entry(sidebar, "DEPARTMENT")
        self.salary = create_label_entry(sidebar, "SALARY")
        self.email = create_label_entry(sidebar, "EMAIL")

        # Action Button
        self.add_btn = tk.Button(sidebar, text="ADD RECORD", command=self.add_employee, bg="#27ae60", 
                                 fg="black", font=("Arial", 10, "bold"), highlightbackground="#f8f9fa",padx=10, pady=8)
        self.add_btn.pack(fill="x", padx=25, pady=10)

        # ─── MAIN AREA (TABLE) ────────
        main_area = tk.Frame(self.root, bg="#2c3e50")
        main_area.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Search & Table Controls
        search_frame = tk.Frame(main_area, bg="#2c3e50")
        search_frame.pack(fill="x", pady=(0, 10))

        tk.Label(search_frame, text="Search Staff:", bg="#2c3e50", fg="white", font=("Arial", 10)).pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.search_employee)
        
        # Search entry forced to white/black
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, font=("Arial", 11), 
                                bg="white", fg="black", insertbackground="black", width=30)
        search_entry.pack(side="left", padx=10)

        tk.Button(search_frame, text="DELETE", command=self.delete_employee, bg="#e74c3c", 
                  fg="black", font=("Arial", 9, "bold"), highlightbackground="#2c3e50", padx=15).pack(side="right", padx=5)
        tk.Button(search_frame, text="EDIT INFO", command=self.edit_employee, bg="#3498db", 
                  fg="black", font=("Arial", 9, "bold"), highlightbackground="#2c3e50", padx=15).pack(side="right", padx=5)

        # Table (Treeview)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="white", foreground="black", fieldbackground="white", rowheight=30)
        style.map("Treeview", background=[('selected', '#3498db')], foreground=[('selected', 'white')])

        self.cols = ("ID", "First Name", "Last Name", "Age", "Gender", "Dept", "Salary", "City", "Date", "Email")
        self.tree = ttk.Treeview(main_area, columns=self.cols, show="headings")

        for c in self.cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=100, anchor="center")

        self.tree.pack(fill="both", expand=True)
        self.load_data()

    # --- Methods ---
    def load_data(self, rows=None):
        for i in self.tree.get_children(): self.tree.delete(i)
        if rows is None: rows = emp.fetch_employees()
        for r in rows: self.tree.insert("", "end", values=r)

    def add_employee(self):
        try:
            age = int(self.age.get())
            sal = int(self.salary.get())
            emp.add_employee(self.fname.get(), self.lname.get(), age, "Male", self.dept.get(), sal, "City", "2026-04-24", self.email.get())
            self.load_data(); self.clear_form()
            messagebox.showinfo("Success", "Employee added")
        except ValueError:
            messagebox.showerror("Error", "Check Age and Salary numbers")

    def delete_employee(self):
        selected = self.tree.selection()
        if not selected: return
        emp_id = self.tree.item(selected[0])['values'][0]
        emp.delete_employee(emp_id)
        self.load_data()

    def edit_employee(self):
        selected = self.tree.selection()
        if not selected: return
        data = self.tree.item(selected[0])['values']
        
        edit_win = tk.Toplevel(self.root)
        edit_win.title("Update Record")
        edit_win.geometry("350x550")
        edit_win.configure(bg="#ecf0f1")

        def create_edit_field(label_text, default_val):
            tk.Label(edit_win, text=label_text, bg="#ecf0f1", fg="black").pack(pady=(10, 0))
            ent = tk.Entry(edit_win, font=("Arial", 11), bg="white", fg="black", insertbackground="black")
            ent.insert(0, default_val)
            ent.pack(padx=30, fill="x", ipady=5)
            return ent

        e_fname = create_edit_field("First Name", data[1])
        e_lname = create_edit_field("Last Name", data[2])
        e_age = create_edit_field("Age", data[3])
        e_dept = create_edit_field("Department", data[5])
        e_salary = create_edit_field("Salary", data[6])
        e_email = create_edit_field("Email", data[9])

        def update():
            try:
                emp.update_employee(data[0], e_fname.get(), e_lname.get(), int(e_age.get()), data[4], e_dept.get(), int(e_salary.get()), data[7], data[8], e_email.get())
                edit_win.destroy(); self.load_data()
            except: messagebox.showerror("Error", "Invalid data")

        tk.Button(edit_win, text="SAVE", command=update, bg="#3498db", fg="white", font=("Arial", 10, "bold")).pack(pady=30, padx=30, fill="x", ipady=10)

    def search_employee(self, *args):
        val = self.search_var.get().lower()
        all_data = emp.fetch_employees()
        filtered = [r for r in all_data if val in str(r[1]).lower() or val in str(r[5]).lower()]
        self.load_data(filtered)

    def clear_form(self):
        for ent in [self.fname, self.lname, self.age, self.dept, self.salary, self.email]:
            ent.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()