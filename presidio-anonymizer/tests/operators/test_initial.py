import pytest
from presidio_anonymizer.operators import Initial


def test_correct_name():
    initial = Initial()
    assert initial.operator_name() == "initial"


@pytest.mark.parametrize(
    "input_text, initials",
    [
        ("John Smith", "J. S."),
        ("john smith", "J. S."),
    ],
)
def test_given_value_for_initial(input_text, initials):
    output = Initial().operate(input_text)
    assert output == initials

def test_initials_trim_extra_whitespace():
    input_text = "     Eastern    Michigan   University   "
    expected = "E. M. U."
    output = Initial().operate(input_text)
    assert output == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("@abc", "@A."),
        ("@843A", "@8."),
        ("--**abc", "--**A."),
    ],
)
def test_initials_handle_leading_non_alphanumeric(input_text, expected):
    output = Initial().operate(input_text)
    assert output == expected
