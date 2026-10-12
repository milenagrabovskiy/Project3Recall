from langchain_aws import ChatBedrockConverse #converse api

from config import BEDROCK_MODEL_ID, BEDROCK_MAX_TOKENS, AGENT_RUNTIME_ARN, AWS_REGION


def _load_model() -> ChatBedrockConverse:
    """Build Bedrock chat model from environment variables."""
    
    return ChatBedrockConverse(
        model_id=BEDROCK_MODEL_ID,
        max_tokens=int(BEDROCK_MAX_TOKENS) if BEDROCK_MAX_TOKENS else None,
        region_name=AWS_REGION,
        temperature=0.0
    )


# lazily load model so it is only ever instantiated when it is used
_MODEL: ChatBedrockConverse | None = None

def get_model() -> ChatBedrockConverse:
    global _MODEL
    if _MODEL is None:
        _MODEL = _load_model()
    return _MODEL