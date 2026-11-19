from collections.abc import Sequence

from core.domain.context import Context
from core.pipeline.exceptions import PipelineStepError
from core.pipeline.pipeline_step import PipelineStep
from core.pipeline.logging import logger


class Pipeline:
    def __init__(self, steps: Sequence[PipelineStep]):
        self._steps = steps

    def execute(self, context: Context) -> Context:
        current_context = context

        logger.info("Pipeline started")

        for step in self._steps:
            logger.info(
                "Executing PipelineStep: %s",
                step.__class__.__name__,
            )

            try:
                current_context = step.execute(current_context)
            except Exception as exc:
                logger.exception(
                    "PipelineStep failed: %s",
                    step.__class__.__name__,
                )
                raise PipelineStepError(
                    f"PipelineStep '{step.__class__.__name__}' failed"
                ) from exc

        logger.info("Pipeline completed")

        return current_context
