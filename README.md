# Happy Number Checker

A simple Python script to determine if a given number is a **happy number**. 

## What is a Happy Number?

A **happy number** is defined by the following process:
1. Start with any positive integer.
2. Replace the number with the sum of the squares of its digits.
3. Repeat the process until:
   - The number equals `1` (it is a happy number), or
   - A loop is detected that does not include `1` (it is not a happy number).

⭐For example:
- `7` is a happy number: \( 7 \to 49 \to 97 \to 130 \to 10 \to 1 \).
- `45` is not a happy number: \( 45 \to 41 \to 17 \to 50 \to 25 \to 29 \to 85 \to 89 \to ... \) (enters a loop).

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/happy-number-checker.git

   cd happy-number-checker
2. Run the script:

    ```bash
    python happy_number.py
    ```
## Example

Here is an example usage:

```python
>>> from happy_number import is_happy
>>> is_happy(7)
True
>>> is_happy(45)
False
>>> is_happy(44)
True
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.