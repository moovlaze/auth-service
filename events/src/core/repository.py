from typing import Protocol


class IEventRepository(Protocol):
    def send(self, operation: str, description: str) -> None:
        pass


class MyEventRepository:
    def send(self, operation: str, description: str) -> None:
        with open(
            r"C:\my\projects\auth-service\events\src\core\events_repository\events.txt",
            mode="a",
            encoding="UTF-8",
        ) as fl:
            fl.write(f"----------\nAction: {operation}\n{description}\n----------")


def get_event_repository() -> IEventRepository:
    return MyEventRepository()
