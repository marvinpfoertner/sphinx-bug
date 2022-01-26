def test_one_return_type_in_docstring():
    """Test function with one return value and return type documentation in the
    docstring.

    Returns
    -------
    return1 : int
        Description of ``return1``.
    """
    return 42


def test_two_returns_type_in_docstring():
    """Test function with two return values.

    Returns
    -------
    return1 : int
        Description of ``return1``.

    return2 : float
        Description of ``return2``.
    """
    return 42, 42.0


def test_one_return() -> int:
    """Test function with one return value.

    Returns
    -------
    return1 :
        Description of ``return1``.
    """
    return 42


def test_two_returns() -> tuple[int, float]:
    """Test function with two return values.

    Returns
    -------
    return1 :
        Description of ``return1``.

    return2 :
        Description of ``return2``.
    """
    return 42, 42.0
