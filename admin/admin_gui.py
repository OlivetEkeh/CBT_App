import tkinter as tk

class AdminGUI:
    def __init__(self, master, show_login_screen_callback):
        self.master = master
        self.show_login_screen_callback = show_login_screen_callback

    def show_admin_dashboard(self):
        admin_dashboard_frame = tk.Frame(self.master)
        tk.Label(admin_dashboard_frame, text="Welcome to the Admin Dashboard!").pack()

        add_exam_button = tk.Button(admin_dashboard_frame, text="Add Exam", command=self.add_exam)
        add_exam_button.pack(pady=10)

        back_button = tk.Button(admin_dashboard_frame, text="Back", command=self.show_login_screen)
        back_button.pack(pady=10)

        admin_dashboard_frame.pack()

    def add_exam(self):
        tk.messagebox.showinfo("Info", "Add Exam functionality goes here.")

    def show_login_screen(self):
        if self.master.winfo_exists():
            self.master.destroy()  # Destroy the current frame
        self.show_login_screen_callback()  # Show the login screen


if __name__ == "__main__":
    root = tk.Tk()
    admin_gui = AdminGUI(root, None)
    admin_gui.show_admin_dashboard()
    root.mainloop()
