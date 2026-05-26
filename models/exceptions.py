class InvalidEmailError(Exception):
    """Exception raised for invalid email addresses."""
    def __init__(self, email):
        self.email = email
        self.message = f"Invalid email address: {email}"
        super().__init__(self.message)
        
class InvalidPhoneError(Exception):
    """Exception raised for invalid phone numbers."""
    def __init__(self, phone):
        self.phone = phone
        self.message = f"Invalid phone number: {phone}"
        super().__init__(self.message)