from dataclasses import dataclass, field
from enum import Enum
from uuid import UUID, uuid4


class MessageRole(Enum):
    USER = "user"
    ASSISTANT = "assistant"


@dataclass(frozen=True)
class Message:
    content: str
    role: MessageRole
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not self.content.strip():
            raise ValueError("Message content cannot be empty.")