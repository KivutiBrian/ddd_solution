from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str  
    SQLALCHEMY_DATABASE_URI:str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    CLIENT_ID: str
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: int
    CLOUDINARY_API_SECRET:str   

    class Config:
        env_file = ".env"

settings = Settings()