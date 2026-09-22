"""Step 6: connect to the LLM (the "brain" of the assistant)."""

from langchain_groq import ChatGroq

from hr_assistant import config
from hr_assistant.gateway import get_gateway_llm
from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def get_llm():
    """Return an LLM model: routes via Portkey if PORTKEY_API_KEY is present, else directly via ChatGroq."""
    if config.PORTKEY_API_KEY:
        logger.info("Initializing LLM via Portkey gateway")
        return get_gateway_llm()
    
    logger.info("Initializing LLM directly via ChatGroq")
    return ChatGroq(
        model=config.LLM_MODEL_NAME,
        api_key=config.GROQ_API_KEY,
        temperature=0,
    )