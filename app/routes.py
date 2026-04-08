from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
from services.explaination_service import get_explaination
from services.image_service import create_visual

class ExplainRequest(BaseModel):
    text: str

class VisualRequest(BaseModel):
    prompt: str

@router.post("/explain")
def explain(request: ExplainRequest):
    return get_explaination(request.text)

@router.post("/visual")
def visual(request: VisualRequest):
    return create_visual(request.prompt)

