from package_name.example import reverse

def test_reverse():
    assert reverse("Hexlet") == "telxeH"

def test_reverse_for_empty_string():
    assert reverse(" ") == " "



test_reverse()
test_reverse_for_empty_string()


