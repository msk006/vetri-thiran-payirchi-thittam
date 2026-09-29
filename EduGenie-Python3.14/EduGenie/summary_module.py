from gemini_client import get_gemini_service


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the educational passage below for quick revision.
Preserve the key facts, definitions, relationships, and important examples.
Use a clear heading followed by concise bullet points.
Do not add facts that are not supported by the passage.

Passage:
{text}
"""
    return get_gemini_service().generate(prompt, temperature=0.25, max_output_tokens=1000)
