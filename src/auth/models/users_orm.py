from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, ProjectTypes

class UsersOrm(Base):
    """
    Docstring for UsersOrm
    """
    __tablename__ = 'users'

    id: Mapped[ProjectTypes.int_pk]
    nikename: Mapped[ProjectTypes.str_256]
    email: Mapped[ProjectTypes.str_256]
    hashed_password: Mapped[ProjectTypes.str_256]
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id', ondelete='SET NULL'))
    is_active: Mapped[bool]
    created_at: Mapped[ProjectTypes.created_at]
    updated_at: Mapped[ProjectTypes.updated_at]