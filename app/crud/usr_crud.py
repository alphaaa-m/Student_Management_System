from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models import usr as usr_mod
from app.schemas import usr_schema as usr_sch

hash_pass = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """password scrambler"""
    return hash_pass.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """verification with scrambled one, without unscrambling it"""
    return hash_pass.verify(plain_password, hashed_password)


def get_user(db: Session, user_id: int):
    """search user by their unique ID number"""
    return db.query(usr_mod.User).filter(usr_mod.User.usr_id == user_id).first()

def get_user_by_username(db: Session, username: str):
    """search user by their unique username"""
    return db.query(usr_mod.User).filter(usr_mod.User.usr_name == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Gets a list of users"""
    return db.query(usr_mod.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: usr_sch.UserCreate):
    """Makes a brand new user account in the database."""
    hashed_password = get_password_hash(user.usr_password)

    db_user = usr_mod.User(
        usr_name=user.usr_name,
        usr_password=hashed_password,
        usr_is_admin=user.usr_is_admin,
        usr_is_active=user.usr_is_active
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: usr_sch.UserUpdate):
    """update user."""
    db_user = get_user(db, user_id)
    if not db_user:
        return None

    if user_update.usr_name is not None:
        db_user.usr_name = user_update.usr_name
    if user_update.usr_password is not None:
        db_user.usr_password = get_password_hash(user_update.usr_password)
    if user_update.usr_is_admin is not None:
        db_user.usr_is_admin = user_update.usr_is_admin
    if user_update.usr_is_active is not None:
        db_user.usr_is_active = user_update.usr_is_active

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    """remove user"""
    db_user = get_user(db, user_id)
    if db_user: 
        db.delete(db_user)
        db.commit()
        return True 
    return False