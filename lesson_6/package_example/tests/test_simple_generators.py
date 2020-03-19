from package_example.helpers.simple_generators import get_random_char, get_random_name


def test_get_random_char_value_is_string():
    result = get_random_char()
    assert isinstance(result, str), "Value is not a char"
