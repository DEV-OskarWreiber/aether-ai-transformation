from pydantic import BaseModel

class TransformationInput(BaseModel):
    staff_size: int
    adoption_rate: float
    avg_fte_cost: int
    department: str
