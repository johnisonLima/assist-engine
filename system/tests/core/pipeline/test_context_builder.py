from core.domain.context import Context
from core.pipeline.context_builder import ContextBuilder


def test_context_builder_creates_context():
    builder = ContextBuilder()

    context = builder.build()

    assert isinstance(context, Context)