#FAKE TOOLS FROM WEEK 7 LECTURE

from langchain.tools import tool

from model.load import get_model


@tool
def get_expense_policy() -> str:
    """Get the company's travel expense policy."""
    model = get_model()
    prompt = "What is the company's travel expense policy?"
    response = model.converse(prompt)
    return response


TOOLS = [get_expense_policy]