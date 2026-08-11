from core.domain.message import Message, MessageRole
from core.domain.context import Context
from core.application.orchestrator import Orchestrator

message = Message(
    content="Olá, Assist!",
    role=MessageRole.USER,
)

context = Context()

orchestrator = Orchestrator()

response = orchestrator.process(
    message,
    context,
)

print(response.content)

def test_orchestrator_processes_message():
    message = Message(
        content="Olá, Assist!",
        role=MessageRole.USER,
    )

    context = Context()
    orchestrator = Orchestrator()

    response = orchestrator.process(message, context)

    assert response.content == "Mensagem recebida: Olá, Assist!"

try:
    test_orchestrator_processes_message()
    print("Test passed!")
except AssertionError:
    print("Test failed!")