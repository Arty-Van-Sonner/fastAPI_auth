from sqlalchemy.orm import Mapped

from src.database import Base, ProjectTypes

class RolesOrm(Base):
    """
    Docstring for RolesOrm
    """
    __tablename__ = 'roles'

    id: Mapped[ProjectTypes.int_pk]
    name: Mapped[ProjectTypes.str_256]
    slug: Mapped[ProjectTypes.str_64]
    created_at: Mapped[ProjectTypes.created_at]
    updated_at: Mapped[ProjectTypes.updated_at]