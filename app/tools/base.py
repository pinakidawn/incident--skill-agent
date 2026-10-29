from abc import ABC, abstractmethod

class Tool(ABC):
    @property
    @abstractmethod
    def name(self):
        ...

    @property
    @abstractmethod
    def description(self):
        ...

    @abstractmethod
    def execute(self, **kwargs):
        ...
