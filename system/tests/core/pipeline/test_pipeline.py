import pytest

from core.domain.context import Context
from core.pipeline.middleware import Middleware
from core.pipeline.pipeline import Pipeline
from core.pipeline.exceptions import MiddlewareError

class FirstMiddleware(Middleware):
    def __init__(self, received_contexts: list[Context]):
        self.received_contexts = received_contexts

    def execute(self, context: Context) -> Context:
        self.received_contexts.append(context)
        return context


class SecondMiddleware(Middleware):
    def __init__(self, received_contexts: list[Context]):
        self.received_contexts = received_contexts

    def execute(self, context: Context) -> Context:
        self.received_contexts.append(context)
        return context


def test_pipeline_executes_middlewares_in_order():
    execution_order = []

    class First(Middleware):
        def execute(self, context: Context) -> Context:
            execution_order.append("first")
            return context

    class Second(Middleware):
        def execute(self, context: Context) -> Context:
            execution_order.append("second")
            return context

    pipeline = Pipeline([First(), Second()])
    context = Context()

    result = pipeline.execute(context)

    assert execution_order == ["first", "second"]
    assert result is context


def test_pipeline_propagates_context_between_middlewares():
    received_contexts = []

    pipeline = Pipeline(
        [
            FirstMiddleware(received_contexts),
            SecondMiddleware(received_contexts),
        ]
    )

    context = Context()

    result = pipeline.execute(context)

    assert received_contexts == [context, context]
    assert result is context

class FailingMiddleware(Middleware):
    def execute(self, context: Context) -> Context:
        raise ValueError("Something went wrong")


class MiddlewareAfterFailure(Middleware):
    def __init__(self, executed: list[bool]):
        self.executed = executed

    def execute(self, context: Context) -> Context:
        self.executed.append(True)
        return context


def test_pipeline_raises_middleware_error_when_middleware_fails():
    pipeline = Pipeline([FailingMiddleware()])
    context = Context()

    with pytest.raises(MiddlewareError) as error:
        pipeline.execute(context)

    assert "FailingMiddleware" in str(error.value)
    assert isinstance(error.value.__cause__, ValueError)


def test_pipeline_stops_execution_after_middleware_failure():
    executed = []

    pipeline = Pipeline(
        [
            FailingMiddleware(),
            MiddlewareAfterFailure(executed),
        ]
    )

    context = Context()

    with pytest.raises(MiddlewareError):
        pipeline.execute(context)

    assert executed == []

# python -m pytest