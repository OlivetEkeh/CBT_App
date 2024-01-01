import tkinter as tk

class UserGUI:
    def __init__(self, master, show_login_screen_callback):
        self.master = master
        self.show_login_screen_callback = show_login_screen_callback

    def show_user_dashboard(self):
        user_dashboard_frame = tk.Frame(self.master)
        tk.Label(user_dashboard_frame, text="Welcome to the User Dashboard!").pack()

        take_exam_button = tk.Button(user_dashboard_frame, text="Take Exam", command=self.take_exam)
        take_exam_button.pack(pady=10)

        back_button = tk.Button(user_dashboard_frame, text="Back", command=self.show_login_screen)
        back_button.pack(pady=10)

        user_dashboard_frame.pack()

    def take_exam(self):
        tk.messagebox.showinfo("Info", "Take Exam functionality goes here.")

    def show_login_screen(self):
        if self.master.winfo_exists():
            self.master.destroy()  # Destroy the current frame
        self.show_login_screen_callback()  # Show the login screen


if __name__ == "__main__":
    root = tk.Tk()
    user_gui = UserGUI(root, None)
    user_gui.show_user_dashboard()
    root.mainloop()
