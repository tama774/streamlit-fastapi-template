from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    username: str = Field(..., title="Username", max_length=50)
    password: str = Field(..., title="Password", min_length=6, max_length=128)

class LoginResponse(BaseModel):
    message: str
    username: str
