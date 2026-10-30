from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class HealthResponse(BaseModel):
    status: str
    service: str


class AnalysisCreate(BaseModel):
    input_text: str = Field(min_length=1)


class AnalysisResponse(AnalysisCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int | None = None
    findings: str | None = None
    recommendations: str | None = None
    created_at: datetime
