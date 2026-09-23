"""Smoke test for the HR Policy Assistant agent.

Verifies that the agent can be built and answers a question.
"""

from hr_assistant.pipeline import ask, build_hr_assistant


def test_agent_smoke():
    agent = build_hr_assistant()
    answer = ask(agent, "How many paid annual leave days do I get?")
    assert answer is not None
    assert len(str(answer).strip()) > 0
