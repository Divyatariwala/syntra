def execute_plan(plan: dict) -> dict:
    """
    Execute a Syntra plan.

    This is intentionally deterministic for now.
    The LLM and real tools will be introduced later.
    """

    results = []

    for step in plan["steps"]:
        result = {
            "step_id": step["id"],
            "description": step["description"],
            "status": "completed",
            "output": f"Executed step: {step['description']}",
        }

        results.append(result)

    return {
        "status": "completed",
        "results": results,
    }