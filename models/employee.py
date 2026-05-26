from helper import validate_email, validate_phone, calculate_age
from models.exceptions import InvalidEmailError, InvalidPhoneError

class Employee:
    def __init__(self, id, name, email, phone, dob, department, salary, day_worked):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.dob = dob
        self.age = calculate_age(dob)
        self.department = department
        self.salary = salary
        self.day_worked = day_worked
        self.bonus = self.salary * 0.5 if self.day_worked > 20 else self.salary * 0.2

    def __str__(self):
        return f"{self.name} - {self.dob} - {self.department} - {self.salary} - {self.day_worked}"
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if validate_email(email):
            self._email = email
        else:
            raise InvalidEmailError(email) 
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        if validate_phone(phone):
            self._phone = phone
        else:
            raise InvalidPhoneError(phone)
    
    def to_dict(self):
        return {
            "ID": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "dob": self.dob.isoformat(),
            "age": self.age,
            "department": self.department,
            "salary": self.salary,
            "day_worked": self.day_worked,
            "bonus": self.bonus
        }