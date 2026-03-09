from jose import jwt
from datetime import datetime,timedelta

SECRET_KEY="secretkey"
ALGORITHM="HS256"

def create_token(data:dict):

    expire=datetime.utcnow()+timedelta(hours=10)

    data.update({"exp":expire})

    token=jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)

    return token