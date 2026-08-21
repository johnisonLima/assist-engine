from core.domain.context import Context
from core.pipeline.context_builder import ContextBuilder
from core.pipeline.middleware import Middleware
from core.pipeline.pipeline import Pipeline
from core.pipeline.response_builder import ResponseBuilder


class PipelineMiddleware(Middleware):
    def __init__(self, executed: list[str]):
        self.executed = executed

    def execute(self, context: Context) -> Context:
        self.executed.append("middleware")
        return context


def test_pipeline_full_flow():
    executed = []

    context_builder = ContextBuilder()
    pipeline = Pipeline(
        [
            PipelineMiddleware(executed),
        ]
    )
    response_builder = ResponseBuilder()

    context = context_builder.build()
    result = pipeline.execute(context)
    response = response_builder.build(result)

    assert isinstance(context, Context)
    assert executed == ["middleware"]
    assert result is context
    assert response is context