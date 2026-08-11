from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Response:
    content: str
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not self.content.strip():
            raise ValueError("Response content cannot be empty.")