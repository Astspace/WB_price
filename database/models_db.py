from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import BigInteger, ForeignKey
from datetime import datetime

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[BigInteger]
    tg_name: Mapped[str]
    phone_number: Mapped[str]

class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    wb_id: Mapped[int]
    brand_name: Mapped[str]
    rating: Mapped[float]
    feedback: Mapped[int]
    volume: Mapped[int]
    price: Mapped[int]
    date_add: Mapped[datetime]

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)