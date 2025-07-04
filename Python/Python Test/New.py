import unittest
import bank_app  # Your module with create_account()

class TestBankApp(unittest.TestCase):

    def test_module_imports(self):
        actual = 1
        expected = 1
        self.assertEqual(actual, expected)  # If import fails, this won't run

    def test_create_account_successfully(self):
        accounts = {}
        actual = bank_app.create_account(accounts, 1234567890, "Eriife")
        expected = "Account created successfully. Your account number is: 1234567890 and Your account name is: Eriife"
        self.assertEqual(actual, expected)
        self.assertIn("1234567890", accounts)

    def test_create_duplicate_account(self):
        accounts = {}
        bank_app.create_account(accounts, 1234567890, "Eriife")
        actual = bank_app.create_account(accounts, 1234567890, "Someone Else")
        expected = "Account number already exists."
        self.assertEqual(actual, expected)

    def test_account_number_too_short(self):
        accounts = {}
        actual = bank_app.create_account(accounts, 12345, "Shorty")
        expected = "Invalid account number. It must be exactly 10 digits."
        self.assertEqual(actual, expected)

    def test_account_number_too_long(self):
        accounts = {}
        actual = bank_app.create_account(accounts, 1234567890123, "Longy")
        expected = "Invalid account number. It must be exactly 10 digits."
        self.assertEqual(actual, expected)

    def test_account_number_not_integer(self):
        accounts = {}
        actual = bank_app.create_account(accounts, "1234567890", "NotInt")
        expected = "Account number must be an integer."
        self.assertEqual(actual, expected)

    def test_account_number_negative(self):
        accounts = {}
        actual = bank_app.create_account(accounts, -1234567890, "Negative")
        expected = "Invalid account number. It must be exactly 10 digits."
        self.assertEqual(actual, expected)

    def test_account_number_with_leading_zero_fails(self):
        accounts = {}
        actual = bank_app.create_account(accounts, 123456789, "TooShortEvenWithLeadingZero")
        expected = "Invalid account number. It must be exactly 10 digits."
        self.assertEqual(actual, expected)

    def test_account_name_empty(self):
        accounts = {}
        actual = bank_app.create_account(accounts, 1234567890, "")
        expected = "Account name cannot be empty."  # You need to add this check in your function
        self.assertEqual(actual, expected)

    def test_account_name_with_spaces(self):
        accounts = {}
        actual = bank_app.create_account(accounts, 1234567890, "   ")
        expected = "Account name cannot be empty."  # Treat whitespace as empty
        self.assertEqual(actual, expected)

    def test_account_name_valid_with_spaces(self):
        accounts = {}
        actual = bank_app.create_account(accounts, 1234567890, "  Eriife  ")
        expected = "Account created successfully. Your account number is: 1234567890 and Your account name is:   Eriife  "
        self.assertEqual(actual, expected)

    def test_create_account_with_default_balance(self):
        accounts = {}
        bank_app.create_account(accounts, 1234567890, "Eriife")
        self.assertEqual(accounts["1234567890"]["balance"], 0)

    def test_create_account_with_initial_balance(self):
        accounts = {}
        bank_app.create_account(accounts, 1234567890, "Eriife", 500)
        self.assertEqual(accounts["1234567890"]["balance"], 500)

    def test_multiple_accounts_creation(self):
        accounts = {}
        bank_app.create_account(accounts, 1234567890, "User1")
        bank_app.create_account(accounts, 2345678901, "User2")
        bank_app.create_account(accounts, 3456789012, "User3")
        self.assertEqual(len(accounts), 3)

    def test_account_number_data_type_enforced(self):
        accounts = {}
        actual = bank_app.create_account(accounts, [1234567890], "ListAccount")
        expected = "Account number must be an integer."
        self.assertEqual(actual, expected)

    def test_account_name_with_special_characters(self):
        accounts = {}
        actual = bank_app.create_account(accounts, 1234567890, "@Eriife$")
        expected = "Account created successfully. Your account number is: 1234567890 and Your account name is: @Eriife$"
        self.assertEqual(actual, expected)

    def test_account_name_case_sensitivity(self):
        accounts = {}
        bank_app.create_account(accounts, 1234567890, "Eriife")
        self.assertEqual(accounts["1234567890"]["name"], "Eriife")

    def test_account_name_numeric_only(self):
        accounts = {}
        actual = bank_app.create_account(accounts, 1234567890, "123456")
        expected = "Account created successfully. Your account number is: 1234567890 and Your account name is: 123456"
        self.assertEqual(actual, expected)

    def test_account_creation_edge_of_valid_number(self):
        accounts = {}
        actual = bank_app.create_account(accounts, 1000000000, "EdgeUser")
        expected = "Account created successfully. Your account number is: 1000000000 and Your account name is: EdgeUser"
        self.assertEqual(actual, expected)

    def test_account_creation_max_valid_number(self):
        accounts = {}
        actual = bank_app.create_account(accounts, 9999999999, "MaxUser")
        expected = "Account created successfully. Your account number is: 9999999999 and Your account name is: MaxUser"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
































def create_account(accounts, account_number, name, balance=0):
    # Validate account_number is an integer
    if type(account_number) is not int:
        return "Account number must be an integer."

    # Convert to string for digit count
    account_str = str(account_number)

    # Check account number is exactly 10 digits (no leading zeros allowed)
    if len(account_str) != 10:
        return "Invalid account number. It must be exactly 10 digits."

    # Validate name is not empty or only whitespace
    if type(name) is not str or name.strip() == "":
        return "Account name cannot be empty."

    # Prevent duplicates
    if account_str in accounts:
        return "Account number already exists."

    # Create account
    accounts[account_str] = {
        'name': name,
        'balance': balance
    }

    return f"Account created successfully. Your account number is: {account_str} and Your account name is: {name}"

