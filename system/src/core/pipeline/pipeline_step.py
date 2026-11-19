from abc import ABC, abstractmethod

from core.domain.context import Context


class PipelineStep(ABC):
    @abstractmethod
    def execute(self, context: Context) -> Context:
        ...
