from sqlalchemy.orm import Mapped
from datetime import datetime

from .. import Base


class Purchase(Base):
    __tablename__ = "purchases"

    name: Mapped[str]
    # purchasing_time: Mapped[datetime]
    number: Mapped[int]
    amount: Mapped[int]
    cost: Mapped[str]