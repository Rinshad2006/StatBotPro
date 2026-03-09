import builtins

# List of blocked keywords
BLOCKED_KEYWORDS = [
    "import os",
    "import sys",
    "subprocess",
    "open(",
    "exec(",
    "eval(",
    "__import__",
]

def is_code_safe(code):
    """Check if the code contains blocked keywords"""
    for word in BLOCKED_KEYWORDS:
        if word in code:
            return False
    return True


def run_code_safely(code, df):
    """Execute AI-generated code in a restricted environment"""

    if not is_code_safe(code):
        return "⚠️ Unsafe code detected. Execution blocked."

    safe_globals = {
        "__builtins__": {
            "print": builtins.print,
            "len": builtins.len,
            "range": builtins.range,
            "sum": builtins.sum
        },
        "df": df
    }

    try:
        exec(code, safe_globals)
        return "Code executed successfully."
    except Exception as e:
        return f"Error: {e}"