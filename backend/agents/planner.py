def create_plan(objective: str) -> dict:
    """
    Create an execution plan for a Syntra task.

    This is intentionally deterministic for now.
    The LLM will replace this logic later.
    """

    return {
        "goal": objective,
        "steps": [
            {
                "id": 1,
                "description": "Understand the objective and required outcome",
                "type": "analysis",
            },
            {
                "id": 2,
                "description": "Gather the information required to complete the objective",
                "type": "research",
            },
            {
                "id": 3,
                "description": "Analyse the gathered information",
                "type": "analysis",
            },
            {
                "id": 4,
                "description": "Produce the final result",
                "type": "synthesis",
            },
        ],
    }