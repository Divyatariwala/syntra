def evaluate_result(result: dict) -> dict:
    """
    Evaluate the result of a Syntra task.

    This is intentionally deterministic for now.
    A more intelligent evaluator will be introduced later.
    """

    if result is None:
        return {
            "status": "failed",
            "success": False,
            "reason": "No result was produced",
        }

    if result.get("status") != "completed":
        return {
            "status": "failed",
            "success": False,
            "reason": "Execution did not complete successfully",
        }

    results = result.get("results", [])

    if not results:
        return {
            "status": "failed",
            "success": False,
            "reason": "Execution produced no step results",
        }

    for step in results:
        if step.get("status") != "completed":
            return {
                "status": "failed",
                "success": False,
                "reason": f"Step {step.get('step_id')} did not complete",
            }

    return {
        "status": "passed",
        "success": True,
        "reason": "All execution steps completed successfully",
    }