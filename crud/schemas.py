from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime


# Person 相关 Schemas

class PersonBase(BaseModel):
    """Person 的基础字段"""
    name: str
    email: str
    phone: str

    class Config:
        from_attributes = True


class PersonCreate(PersonBase):
    """创建 Person 时的输入 schema"""
    pass


class PersonUpdate(BaseModel):
    """更新 Person 时的输入 schema，所有字段可选"""
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class Person(PersonBase):
    """Person 的输出 schema，包含所有字段"""
    id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True


# Blog 相关 Schemas

class BlogBase(BaseModel):
    """Blog 的基础字段"""
    title: str
    description: Optional[str] = None
    completed: bool = False
    person_name: str

    class Config:
        from_attributes = True


class BlogCreate(BlogBase):
    """创建 Blog 时的输入 schema"""
    pass


class BlogUpdate(BaseModel):
    """更新 Blog 时的输入 schema，所有字段可选"""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    person_name: Optional[str] = None


class Blog(BlogBase):
    """Blog 的输出 schema，包含所有字段"""
    id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True
