from sqlalchemy.ext.asyncio import AsyncSession
from src.common



class BaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._crud = CrudRepository(self._session, self.model)

        
