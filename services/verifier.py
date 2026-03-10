from agents.myth_agent import create_agent_executor

def verify_claim(claim):

    agent = create_agent_executor()

    prompt = f"""
    Fact-check the following claim.

    Claim: {claim}

    Respond in this format:

    Verdict: TRUE / FALSE / MISLEADING

    Explanation:
    (Short explanation)

    Confidence:
    LOW / MEDIUM / HIGH
    """

    response = agent.invoke({
        "messages": [
            {"role": "user", "content": prompt}
        ]
    })

    return response["messages"][-1].content