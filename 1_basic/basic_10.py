def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


def test_get_formatted_name():
    formatted_name = get_formatted_name("john", "doe")
    assert formatted_name == "John Doe"