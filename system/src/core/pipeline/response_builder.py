from core.domain.context import Context


class ResponseBuilder:
    def build(self, context: Context) -> Context:
        return context