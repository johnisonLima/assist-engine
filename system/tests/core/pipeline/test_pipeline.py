import pytest

from core.domain.context import Context
from core.pipeline.pipeline_step import PipelineStep
from core.pipeline.pipeline import Pipeline
from core.pipeline.exceptions import PipelineStepError

class FirstPipelineStep(PipelineStep):
    def __init__(self, received_contexts: list[Context]):
        self.received_contexts = received_contexts

    def execute(self, context: Context) -> Context:
        self.received_contexts.append(context)
        return context


class SecondPipelineStep(PipelineStep):
    def __init__(self, received_contexts: list[Context]):
        self.received_contexts = received_contexts

    def execute(self, context: Context) -> Context:
        self.received_contexts.append(context)
        return context


def test_pipeline_executes_steps_in_order():
    execution_order = []

    class First(PipelineStep):
        def execute(self, context: Context) -> Context:
            execution_order.append("first")
            return context

    class Second(PipelineStep):
        def execute(self, context: Context) -> Context:
            execution_order.append("second")
            return context

    pipeline = Pipeline([First(), Second()])
    context = Context()

    result = pipeline.execute(context)

    assert execution_order == ["first", "second"]
    assert result is context


def test_pipeline_propagates_context_between_steps():
    received_contexts = []

    pipeline = Pipeline(
        [
            FirstPipelineStep(received_contexts),
            SecondPipelineStep(received_contexts),
        ]
    )

    context = Context()

    result = pipeline.execute(context)

    assert received_contexts == [context, context]
    assert result is context

class FailingPipelineStep(PipelineStep):
    def execute(self, context: Context) -> Context:
        raise ValueError("Something went wrong")


class PipelineStepAfterFailure(PipelineStep):
    def __init__(self, executed: list[bool]):
        self.executed = executed

    def execute(self, context: Context) -> Context:
        self.executed.append(True)
        return context


def test_pipeline_raises_pipeline_step_error_when_step_fails():
    pipeline = Pipeline([FailingPipelineStep()])
    context = Context()

    with pytest.raises(PipelineStepError) as error:
        pipeline.execute(context)

    assert "FailingPipelineStep" in str(error.value)
    assert isinstance(error.value.__cause__, ValueError)


def test_pipeline_stops_execution_after_step_failure():
    executed = []

    pipeline = Pipeline(
        [
            FailingPipelineStep(),
            PipelineStepAfterFailure(executed),
        ]
    )

    context = Context()

    with pytest.raises(PipelineStepError):
        pipeline.execute(context)

    assert executed == []

# python -m pytest
