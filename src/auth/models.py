import datetime

from typing import Annotated, Optional
import enum

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

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
    created_at: Mapped[ProjectTypes.created_at]
    updated_at: Mapped[ProjectTypes.updated_at]

class PermissionsOrm(Base):
    """
    Docstring for Permissions
    """
    __tablename__ = 'permissions'

    id: Mapped[ProjectTypes.int_pk]
    name: Mapped[ProjectTypes.str_256]
    slug: Mapped[ProjectTypes.str_64]


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