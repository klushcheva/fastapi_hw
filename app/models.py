from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field


class DogType(Enum):
    terrier = 'terrier'
    bulldog = 'bulldog'
    dalmatian = 'dalmatian'


class Timestamp(BaseModel):
    id: int = Field(..., title='Id')
    timestamp: int = Field(..., title='Timestamp')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class Dog(BaseModel):
    name: str = Field(..., title='Name')
    pk: Optional[int] = Field(None, title='Pk')
    kind: DogType


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')
