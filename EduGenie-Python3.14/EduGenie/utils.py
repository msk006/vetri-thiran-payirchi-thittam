import json
import re


def clean_json_block(value: str) -> str:
    """Remove Markdown fences and surrounding text around a JSON object/array."""
    value = value.strip()
    value = re.sub(r"^```(?:json)?\s*", "", value, flags=re.IGNORECASE)
    value = re.sub(r"\s*```$", "", value)

    start_candidates = [i for i in (value.find("["), value.find("{")) if i >= 0]
    if not start_candidates:
        return value
    start = min(start_candidates)

    end_array = value.rfind("]")
    end_object = value.rfind("}")
    end = max(end_array, end_object)
    return value[start : end + 1] if end >= start else value


def parse_json(value: str):
    return json.loads(clean_json_block(value))
