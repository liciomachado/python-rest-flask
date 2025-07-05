from abc import ABC, abstractmethod

class IEventBus(ABC):
    @abstractmethod
    def publish(self, queue_name: str, payload: dict): pass
