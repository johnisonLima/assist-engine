from core.domain.context import Context
from core.pipeline.response_builder import ResponseBuilder


def test_response_builder_returns_context():
    builder = ResponseBuilder()
    context = Context()

    response = builder.build(context)

    assert response is context