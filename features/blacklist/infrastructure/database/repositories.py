from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from features.blacklist.domain.models import BlacklistUser
from features.blacklist.domain.ports import BlacklistRepository

Base = declarative_base()

class BlacklistUserDB(Base):
    __tablename__ = "blacklist_users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_numbers = Column(ARRAY(String), nullable=False)
    emails = Column(ARRAY(String), nullable=False)
    telegrams = Column(ARRAY(String), nullable=False)
    comment = Column(String, nullable=True)

class SQLAlchemyBlacklistRepository(BlacklistRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, user: BlacklistUser):
        db_user = BlacklistUserDB(
            first_name=user.first_name,
            last_name=user.last_name,
            phone_numbers=user.phone_numbers,
            emails=user.emails,
            telegrams=user.telegrams,
            comment=user.comment,
        )
        self.session.add(db_user)
        self.session.commit()

    def get_user(self, user_id: int) -> BlacklistUser:
        db_user = self.session.query(BlacklistUserDB).filter(BlacklistUserDB.id == user_id).first()
        if not db_user:
            raise ValueError("User not found")
        return BlacklistUser(
            first_name=db_user.first_name,
            last_name=db_user.last_name,
            phone_numbers=db_user.phone_numbers,
            emails=db_user.emails,
            telegrams=db_user.telegrams,
            comment=db_user.comment,
        )

    def get_all_users(self) -> List[BlacklistUser]:
        db_users = self.session.query(BlacklistUserDB).all()
        return [
            BlacklistUser(
                first_name=db_user.first_name,
                last_name=db_user.last_name,
                phone_numbers=db_user.phone_numbers,
                emails=db_user.emails,
                telegrams=db_user.telegrams,
                comment=db_user.comment,
            )
            for db_user in db_users
        ]

    def delete_user(self, user_id: int):
        self.session.query(BlacklistUserDB).filter(BlacklistUserDB.id == user_id).delete()
        self.session.commit()