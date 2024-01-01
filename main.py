import tkinter as tk
from admin.admin_gui import AdminGUI
from user.user_gui import UserGUI

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CBT Application")

        self.show_login_screen()

    def show_login_screen(self):
        login_frame = tk.Frame(self.master)
        tk.Label(login_frame, text="Login Screen").pack(pady=10)

        admin_button = tk.Button(login_frame, text="Administrator Section", command=self.show_admin_dashboard)
        admin_button.pack(pady=10)

        user_button = tk.Button(login_frame, text="User Section", command=self.show_user_section)
        user_button.pack(pady=10)

        login_frame.pack()

    def show_admin_dashboard(self):
        self.hide_current_frame()
        admin_frame = AdminGUI(self.master, self.show_login_screen)
        admin_frame.show_admin_dashboard()

    def show_user_section(self):
        self.hide_current_frame()
        user_frame = UserGUI(self.master, self.show_login_screen)
        user_frame.show_user_dashboard()

    def hide_current_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    main_app = MainApp(root)
    root.mainloop()
