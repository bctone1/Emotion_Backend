# app/models/common.py
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, func

def gen_uuid():
    return str(uuid.uuid4())
