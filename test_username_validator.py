import unittest
from username_validator import validate_username

class TestUsernameValidator(unittest.TestCase):
    def test_valid_usernames(self):
        valid_usernames = [
            "abc",
            "_abc",
            "a123",
            "A_1_b",
            "_A1b2c3",
            "user_name",
            "a_b_c_d_e_f_g_h_i"
        ]
        for username in valid_usernames:
            with self.subTest(username=username):
                self.assertTrue(validate_username(username))

    def test_too_short(self):
        self.assertFalse(validate_username("ab"))

    def test_too_long(self):
        self.assertFalse(validate_username("a" * 17))

    def test_starts_with_number(self):
        self.assertFalse(validate_username("1abc"))

    def test_starts_with_multiple_underscores(self):
        self.assertFalse(validate_username("__abc"))

    def test_invalid_characters(self):
        self.assertFalse(validate_username("abc$%"))
        self.assertFalse(validate_username("user-name"))
        self.assertFalse(validate_username("user.name"))

    def test_empty_string(self):
        self.assertFalse(validate_username(""))

    def test_only_underscores(self):
        self.assertFalse(validate_username("___"))

    def test_valid_edge_lengths(self):
        self.assertTrue(validate_username("abc"))
        self.assertTrue(validate_username("a" * 16))

if __name__ == "__main__":
    unittest.main()
