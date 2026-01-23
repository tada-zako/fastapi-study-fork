from fastapi.dependencies.utils import get_typed_return_annotation


def test_get_typed_return_annotation():
    def func1() -> int:
        return 1

    def func2() -> str:
        return "test"

    def func3():
        return None

    assert get_typed_return_annotation(func1) is int
    assert get_typed_return_annotation(func2) is str
    assert get_typed_return_annotation(func3) is None
