from fastapi import APIRouter

from app.api.endpoints import (
    google_api_router,
    user_router,
    charity_router,
    donation_router,
)

main_router = APIRouter()

main_router.include_router(
    charity_router, prefix='/charity_project', tags=['Charities'],
)
main_router.include_router(
    donation_router, prefix='/donation', tags=['Donations'],
)
main_router.include_router(user_router)
main_router.include_router(
    google_api_router,
    prefix='/google',
    tags=['Google']
)