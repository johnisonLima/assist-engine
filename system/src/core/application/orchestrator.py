from core.domain.context import Context
from core.domain.message import Message
from core.domain.response import Response


class Orchestrator:

    def process(self, message: Message, context: Context,) -> Response:
        return Response(
            content=f"Mensagem recebida: {message.content}"
        )