from main import calculate_score, compare


def test_case_1_calculate_score():
    assert calculate_score([11, 10]) == 0


def test_case_2_calculate_score():
    assert calculate_score([10, 11]) == 0


def test_case_3_calculate_score():
    assert calculate_score([11, 11]) == 12


def test_case_4_calculate_score():
    assert calculate_score([11, 8, 10]) == 19


def test_case_5_calculate_score():
    assert calculate_score([11, 8, 2]) == 21


def test_case_6_calculate_score():
    assert calculate_score([11, 11, 2]) == 14


def test_case_7_calculate_score():
    assert calculate_score([11, 11, 10]) == 12


def test_case_8_calculate_score():
    assert calculate_score([11, 11, 11, 10]) == 13


def test_case_9_calculate_score():
    assert calculate_score([2, 8, 10]) == 20


def test_case_10_calculate_score():
    assert calculate_score([2, 10, 10]) == 22


def test_case_11_calculate_score():
    assert calculate_score([10, 10]) == 20
