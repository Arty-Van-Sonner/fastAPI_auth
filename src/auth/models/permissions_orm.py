from sqlalchemy.orm import Mapped

from src.database import Base, ProjectTypes

class PermissionsOrm(Base):
    """
    Docstring for Permissions
    """
    __tablename__ = 'permissions'

    id: Mapped[ProjectTypes.int_pk]
    name: Mapped[ProjectTypes.str_256]
    slug: Mapped[ProjectTypes.str_64]