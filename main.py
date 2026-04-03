def process_data(items: list[str]) -> dict:
    """Process a list of items and return statistics."""
    return {
        "count": len(items),
        "unique": len(set(items)),
        "first": items[0] if items else None,
    }

# BUG: This function doesn't handle empty lists properly
def calculate_average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)
