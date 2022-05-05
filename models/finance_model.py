from typing import Dict, List, Optional, Union
from pydantic import BaseModel


class FinanceResultsModel(BaseModel):
    revenue: Union[int, None]
    income: Union[int, None]
    revenue_growth_yoy: Union[str, None]
    profit_margin: Union[str, None]
    ebit_margin: Union[str, None]
    sales_margin: Union[str, None]
    gross_margin: Union[str, None]
    roe: Union[str, None]


class OrganizationModel(BaseModel):
    inn: int
    bfo_id: Union[int, None]
    results: Optional[List[Dict[str, FinanceResultsModel]]]
