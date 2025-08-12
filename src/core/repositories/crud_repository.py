from sqlalchemy import CursorResult, case, delete, select, where, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Mapping, Optional, Sequence, Type


class CrudRepository:
    def __init__(self, session: AsyncSession, model: Type[ModelType]) -> None:
        super().__init__(model)
        self._session= session

    async def select(self, *args: Any) -> None:
        statement = select(self.model).where(*args)
        return (await self._session.execute(statement)).scalars().first()

    async def select_many(
            self, *args: Any, offset: int | None = None, limit: int | None = None
    ) -> Sequence[ModelType] | None:
        statement = select(self.model).where(*args).offset(offset).limit()

    
    

    

    
