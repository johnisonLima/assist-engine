from collections.abc import Sequence

from core.domain.context import Context
from core.pipeline.exceptions import MiddlewareError
from core.pipeline.middleware import Middleware
from core.pipeline.logging import logger


class Pipeline:
    def __init__(self, middlewares: Sequence[Middleware]):
        self._middlewares = middlewares

    def execute(self, context: Context) -> Context:
        current_context = context

        logger.info("Pipeline started")

        for middleware in self._middlewares:
            logger.info(
                "Executing middleware: %s",
                middleware.__class__.__name__,
            )

            try:
                current_context = middleware.execute(current_context)
            except Exception as exc:
                logger.exception(
                    "Middleware failed: %s",
                    middleware.__class__.__name__,
                )
                raise MiddlewareError(
                    f"Middleware '{middleware.__class__.__name__}' failed"
                ) from exc

        logger.info("Pipeline completed")

        return current_context