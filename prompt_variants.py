def zero_shot(task):
    return f"{task}"

def few_shot(task):
    return f"""
Example 1:
Task: Explain gravity to a child.
Answer: Gravity is the force that pulls things down to Earth.

Now your turn:
Task: {task}
Answer:
"""

def chain_of_thought(task):
    return f"""
{task}

Let's think step by step.
"""

def role_based(task):
    return f"""
You are a world-class expert educator.

Task:
{task}
"""
