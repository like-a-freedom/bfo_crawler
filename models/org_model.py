from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

# from enum import Enum


# class BusinessType(str, Enum):
#     VENDOR = "vendor"
#     MSSP = "mssp"
#     INTEGRATOR = "integrator"
#     OTHER = "other"


class Financials(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    inn: int
    revenue: int | None
    income: int | None
    revenue_growth_yoy: float | None
    profit_margin: float | None
    ebit_margin: float | None
    sales_margin: float | None
    gross_margin: float | None
    roe: float | None
    created_at: str | None
    updated_at: str | None
    year: int
    organization_id: str | None = Field(foreign_key="organization.id", default=None)
    organization: Optional["Organization"] = Relationship(back_populates="results")


class OrgTagLink(SQLModel, table=True):
    organization_id: Optional[str] = Field(
        default=None, foreign_key="organization.id", primary_key=True
    )
    tag_id: Optional[int] | None = Field(
        default=None, foreign_key="tag.id", primary_key=True
    )


class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    organizations: Optional[List["Organization"]] = Relationship(
        back_populates="tags", link_model=OrgTagLink
    )


class Organization(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    inn: int
    name: str | None = Field(index=True)
    legal_name: str | None = Field(index=True)
    tags: List[Tag] | None = Relationship(
        back_populates="organizations", link_model=OrgTagLink
    )
    business_type: str | None
    bfo_id: int | None
    results: List[Financials] | None = Relationship(back_populates="organization")


Financials.model_rebuild()
Organization.model_rebuild()
Tag.model_rebuild()
OrgTagLink.model_rebuild()
