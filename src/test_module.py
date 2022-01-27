from collections.abc import Iterator


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


def test_one_yield_type_in_docstring():
    """Test function yielding one value.

    Yields
    ------
    yield1 : int
        Description of ``yield1``.
    """
    yield 1


def test_two_yields_type_in_docstring():
    """Test function yielding a tuple of two values.

    Yields
    ------
    yield1 : int
        Description of ``yield1``.

    yield2 : float
        Description of ``yield2``.
    """
    yield 1, 2.0


def test_one_yield() -> Iterator[int]:
    """Test function yielding one value.

    Yields
    ------
    yield1 :
        Description of ``yield1``.
    """
    yield 1


def test_two_yields() -> Iterator[tuple[int, float]]:
    """Test function yielding a tuple of two values.

    Yields
    ------
    yield1 :
        Description of ``yield1``.

    yield2 :
        Description of ``yield2``.
    """
    yield 1, 2.0
