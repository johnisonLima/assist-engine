from abc import ABC, abstractmethod

from core.domain.context import Context


class Middleware(ABC):
    @abstractmethod
    def execute(self, context: Context) -> Context:
        ...