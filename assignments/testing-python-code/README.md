# 📘 Assignment: Testing Python Code with pytest

## 🎯 Objective

Learn how to write unit tests with `pytest` to verify functions and simple classes. You will practice checking normal behavior, edge cases, and expected failures so your Python code is easier to trust and maintain.

## 📝 Tasks

### 🛠️ Test Utility Functions

#### Description
Write tests for the helper functions in the starter code. Focus on making sure each function returns the expected result for common inputs and tricky edge cases.

#### Requirements
Completed program should:

- Write tests for at least 3 functions from the starter code
- Include at least one test for an edge case such as empty text, zero values, or negative numbers
- Verify that invalid input raises the expected error when appropriate
- Use clear test names that explain what each test checks


### 🛠️ Test a Simple Class

#### Description
Write tests for the `BankAccount` class in the starter code. Your tests should confirm that the class updates its state correctly when money is deposited or withdrawn.

#### Requirements
Completed program should:

- Test that a new account starts with the correct initial balance
- Test that deposits increase the balance correctly
- Test that withdrawals decrease the balance correctly
- Test that withdrawing too much raises a `ValueError`
- Keep each test focused on one behavior
