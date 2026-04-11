from typing import List, Optional


def process_numbers(
    values: List[float],
    scale: float = 1.0,
    allow_negative: bool = False
) -> List[float]:
    """
    Process a list of numeric values by applying a scaling factor.

    This function multiplies each value in the input list by the provided
    scaling factor. Optionally, it can reject negative numbers.

    Args:
        values (List[float]): A list of numeric values to process.
        scale (float, optional): Multiplier applied to each value.
            Defaults to 1.0.
        allow_negative (bool, optional): If False, raises an error when
            negative values are encountered. Defaults to False.

    Returns:
        List[float]: A new list containing the scaled values.

    Raises:
        ValueError: If `values` is empty.
        ValueError: If negative values are present and `allow_negative` is False.
        TypeError: If input types are invalid.

    Example:
        >>> process_numbers([1.0, 2.0, 3.0], scale=2.0)
        [2.0, 4.0, 6.0]
    """
    # --- Input Validation ---
    if not isinstance(values, list):
        raise TypeError("values must be a list of floats")

    if not values:
        raise ValueError("values list cannot be empty")

    if not isinstance(scale, (int, float)):
        raise TypeError("scale must be a numeric type")

    # --- Core Logic ---
    processed = []

    for value in values:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Invalid value detected: {value}")

        if not allow_negative and value < 0:
            raise ValueError(f"Negative value not allowed: {value}")

        processed.append(value * scale)

    # --- Return Result ---
    return processed
