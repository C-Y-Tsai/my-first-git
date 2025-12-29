# test_calculator.py
from calculator import add, divide
import pytest

# 測試正常加法 (Happy Path)
def test_add_simple():
    # Arrange (安排)
    a, b = 2, 3
    # Act (執行)
    result = add(a, b)
    # Assert (斷言)
    assert result == 5

# 測試邊界條件 (Edge Case)
def test_add_negative():
    assert add(-1, 1) == 0

# 測試異常處理 (Error Handling)
def test_divide_by_zero():
    with pytest.raises(ValueError, match="除數不能為零"):
        divide(10, 0)
