from datetime import datetime

from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.services.google_api import (
    spreadsheets_create, spreadsheet_update_value, set_user_permissions
)
from app.core.user import current_superuser

from app.crud.charity_project import charity_crud


router = APIRouter()


@router.get(
    '/',
    response_model=list[dict[str, int]],
    dependencies=[Depends(current_superuser)],
)
async def get_report(
    session: AsyncSession = Depends(get_async_session),
    wrapper_services: Aiogoogle = Depends(get_service),
):
    """Только для суперюзеров."""
    closed_projects = await charity_crud.get_projects_by_completion_rate(
        session,
    )
    spreadsheetid = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheetid, wrapper_services)
    await spreadsheet_update_value(
        spreadsheetid,
        closed_projects,
        wrapper_services,
    )
    return closed_projects
