class PipelineError(Exception):
    """Base exception for pipeline execution errors."""


class MiddlewareError(PipelineError):
    """Raised when a middleware fails during execution."""