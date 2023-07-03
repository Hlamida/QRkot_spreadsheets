from datetime import datetime
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharity(CRUDBase[CharityProject]):
    """Обрабатывает базу проектов."""

    @classmethod
    async def get_project_id_by_name(
        cls,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        """Возвращает проект по имени."""

        db_proj_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name,
            )
        )

        return db_proj_id.scalars().first()

    async def get(
        self,
        obj_id: int,
        session: AsyncSession,
    ) -> Optional[CharityProject]:
        """Возвращает проект."""

        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id,
            )
        )
        return db_obj.scalars().first()
#####
    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession,
    ) -> List[CharityProject]:
        """Возвращает все завершённые экземпляры."""

        db_objs = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            ).order_by(self.model.close_date - self.model.create_date)
        )

        return db_objs.scalars().all()

#    async def get_projects_by_completion_rate(
#            self,
#            from_reserve: datetime,
#            to_reserve: datetime,
#            session: AsyncSession,
#    ) -> list[dict[str, int]]:
#        reservations = await session.execute(
#            select(
#                [CharityProject.meetingroom_id,
#                 func.count(CharityProject.meetingroom_id)]).where(
#                    CharityProject.from_reserve >= from_reserve,
#                    CharityProject.to_reserve <= to_reserve,
#               ).group_by(CharityProject.meetingroom_id)
#        )
#        reservations = reservations.all()
#        return reservations


charity_crud = CRUDCharity(CharityProject)
