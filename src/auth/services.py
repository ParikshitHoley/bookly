from sqlmodel.ext.asyncio.session import AsyncSession
from pydantic import EmailStr
from src.auth.model import User
from sqlmodel import select
from src.auth.schemas import UserCreate
from src.auth.utils import hash_password
class AuthService:
    async def check_user_by_email(self, email: EmailStr, session: AsyncSession) -> dict | None:
        # Email existence check logic here
        statement = select(User).where(User.email == email)
        result = await session.exec(statement)
        user = result.first()
        return user if user else None
    
    async def find_user_by_email(self, email: EmailStr, session: AsyncSession) -> bool:
        # Find user by email logic here
        userexit = await self.check_user_by_email(email, session)
        return True if userexit else False

    async def Create_user(self, user_data:UserCreate,session:AsyncSession) -> User:
        # Authorization logic here
        user_creation_data = user_data.model_dump()
        # extract and remove plaintext password from payload
        new_user = User(**user_creation_data)
        new_user.hashed_password = hash_password(user_creation_data["password"])
        session.add(new_user)
        await session.commit()
        # refresh to populate DB-generated fields
        await session.refresh(new_user)
        return new_user
        
    