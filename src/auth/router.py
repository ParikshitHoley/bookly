from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.auth.schemas import UserCreate, UserRead
from src.auth.services import AuthService
from src.db.main import get_session


auth_Routher = APIRouter()
auth_service = AuthService()

@auth_Routher.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserCreate, session: AsyncSession = Depends(get_session)):
    user_exist = await auth_service.find_user_by_email(user_data.email, session)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with this email already exists")
    new_user = await auth_service.Create_user(user_data, session)
    return new_user