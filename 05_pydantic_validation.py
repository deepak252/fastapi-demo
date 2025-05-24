from pydantic import BaseModel, field_validator, model_validator

class CreateUser(BaseModel):
    email: str
    password: str
    confirm_password: str

    @field_validator("email")
    def validate_email(cls, value):
        if (not "gmail" in value) or "admin" in value:
            raise ValueError("This email is not allowed")
        return value
    
    @model_validator(mode="after")
    def validate_password(self):
        if self.password!=self.confirm_password:
            raise ValueError("The two passwords should match")
        
        return self


user1 = CreateUser(email="temp@gmail.com", password="123", confirm_password="123")
# user2 = CreateUser(email="temp@gmail.com", password="asdf", confirm_password="123")   # ERROR
# user2 = CreateUser(email="admin@gmail.com", password="123", confirm_password="123") # ERROR
print(user1)
