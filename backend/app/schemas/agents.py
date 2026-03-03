from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID

# 응답용 스키마 정의 (클라이언트에게 돌려줄 JSON 형태)
class AgentResponse(BaseModel):
    id: UUID  # 백엔드에서는 UUID 객체 또는 문자열 모두 처리할 수 있도록 UUID 사용
    path: str
    name: str
    description: Optional[str] = None
    is_active: bool

    # Pydantic v2에서는 from_attributes를 사용합니다.
    model_config = ConfigDict(from_attributes=True)
