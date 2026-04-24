from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class RolePermissionsOrm(Base):
    """
    Docstring for RolePermissionsOrm
    """
    __tablename__ = 'role_permissions'

    role_id: Mapped[int] = mapped_column(
        ForeignKey('roles.id', ondelete='CASCADE'),
        primary_key=True,
    )
    permission_id: Mapped[int] = mapped_column(
        ForeignKey('permissions.id', ondelete='CASCADE'),
        primary_key=True,
    )