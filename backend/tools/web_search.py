from typing import Any, Dict

from tools.base import Tool


class WebSearchTool(Tool):

    @property
    def name(self) -> str:
        return "web_search"

    @property
    def description(self) -> str:
        return "Search the web for information relevant to a query."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query.",
                }
            },
            "required": ["query"],
        }

    def execute(self, query: str) -> dict:
        return {
            "query": query,
            "status": "completed",
            "results": [
                {
                    "title": f"Search result for: {query}",
                    "url": "https://example.com",
                    "snippet": f"Placeholder result for: {query}",
                }
            ],
        }