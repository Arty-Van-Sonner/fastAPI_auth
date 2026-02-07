from fastapi import APIRouter

from src.auth.schemas import TestGet

router = APIRouter(
    prefix='/auth',
)

@router.get('/test')
async def get_test() -> TestGet:
    return TestGet.model_validate({'title': 'all is right', 'body': 'Let\'s go to new achievements'})
