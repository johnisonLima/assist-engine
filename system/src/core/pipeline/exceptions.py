class PipelineError(Exception):
    """Base exception for pipeline execution errors."""


class PipelineStepError(PipelineError):
    """Raised when a pipeline step fails during execution."""
