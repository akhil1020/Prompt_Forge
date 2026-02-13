"""
LLM Service Layer for PromptForge
Handles all OpenAI API communication safely and cleanly.
"""

import streamlit as st
from openai import OpenAI
from openai import APIError, RateLimitError, APITimeoutError
import logging
from typing import Optional, Dict, Any

# --------------------------------------------------
# Logging Configuration
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# --------------------------------------------------
# Initialize OpenAI Client Safely
# --------------------------------------------------

def get_openai_client() -> OpenAI:
    """
    Create OpenAI client using Streamlit secrets.
    Raises clear error if key is missing.
    """
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
        if not api_key:
            raise ValueError("OPENAI_API_KEY is empty.")
        
        return OpenAI(api_key=api_key)

    except KeyError:
        logger.error("OPENAI_API_KEY not found in Streamlit secrets.")
        raise RuntimeError(
            "OpenAI API key not found. Please set it in .streamlit/secrets.toml"
        )

# Create reusable client instance
client = get_openai_client()


# --------------------------------------------------
# LLM Generation Function
# --------------------------------------------------

def generate_response(
    prompt: str,
    temperature: float = 0.7,
    max_tokens: int = 500,
    model: str = "gpt-4o-mini"
) -> Dict[str, Any]:
    """
    Generate response from OpenAI model.

    Returns:
        {
            "success": bool,
            "content": str,
            "usage": dict | None,
            "error": str | None
        }
    """

    if not prompt or not prompt.strip():
        return {
            "success": False,
            "content": "",
            "usage": None,
            "error": "Prompt is empty."
        }

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )

        return {
            "success": True,
            "content": response.choices[0].message.content.strip(),
            "usage": response.usage.model_dump() if response.usage else None,
            "error": None
        }

    except RateLimitError:
        logger.warning("Rate limit exceeded.")
        return {
            "success": False,
            "content": "",
            "usage": None,
            "error": "Rate limit exceeded. Please wait and try again."
        }

    except APITimeoutError:
        logger.error("Request timed out.")
        return {
            "success": False,
            "content": "",
            "usage": None,
            "error": "Request timed out. Try again."
        }

    except APIError as e:
        logger.error(f"OpenAI API Error: {str(e)}")
        return {
            "success": False,
            "content": "",
            "usage": None,
            "error": f"API Error: {str(e)}"
        }

    except Exception as e:
        logger.exception("Unexpected error occurred.")
        return {
            "success": False,
            "content": "",
            "usage": None,
            "error": "Unexpected error occurred. Check logs."
        }
