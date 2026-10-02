from abc import ABC, abstractmethod
from typing import Any, Dict


class Tool(ABC):
    """
    Base abstraction for every capability available to Syntra.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def input_schema(self) -> Dict[str, Any]:
        """
        Schema describing the arguments accepted by the tool.
        """
        pass

    @abstractmethod
    def execute(self, **kwargs: Any) -> Any:
        pass

    def definition(self) -> Dict[str, Any]:
        """
        Return a model-friendly representation of the tool.
        """

        return {
            "name": self.name,
            "description": self.description,
            "input_schema": self.input_schema,
        }