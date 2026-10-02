from typing import Dict, List

from tools.base import Tool
from tools.web_search import WebSearchTool

class ToolRegistry:
    """
    Central registry of tools available to Syntra.
    """

    def __init__(self) -> None:
        self._tools: Dict[str, Tool] = {}
        self.register(WebSearchTool())

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(
                f"Tool '{tool.name}' is already registered."
            )

        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        tool = self._tools.get(name)

        if tool is None:
            raise ValueError(
                f"Tool '{name}' is not registered."
            )

        return tool

    def list_tools(self) -> List[Tool]:
        return list(self._tools.values())

    def list_tool_names(self) -> List[str]:
        return list(self._tools.keys())