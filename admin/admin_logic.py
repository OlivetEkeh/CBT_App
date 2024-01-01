class AdminLogic:
    def __init__(self):
        # Placeholder for administrator credentials
        self.admin_credentials = {"admin": "admin123"}  # Replace with a secure method in a real application
        self.exam = []

    def check_credentials(self, username, password):
        return username in self.admin_credentials and self.admin_credentials[username] == password
    
    def add_exam(self, subject, num_questions):
        exam = {"subject": subject, "num_questions": num_questions, "questions": []}
        self.exams.append(exam)
