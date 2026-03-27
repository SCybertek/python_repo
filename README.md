# python_repo

Small collection of example Python scripts that demonstrate core Python concepts: variables, control flow, functions, classes, exceptions, modules, and simple tests.

## Contents

- `hello_world.py` — simple "hello, world!" example
- `variables.py` — examples of numbers, strings, booleans, lists, dicts, and `type()`
- `functions.py` — function definitions, default arguments, and simple math examples
- `control_flow.py` — `if`/`elif`/`else` and `for` loop examples
- `classes.py` — `Vehicle`, `Motorcycle`, and `Car` classes with methods and `__repr__`
- `exceptions.py` — raising and handling errors (example `TypeError`)
- `import.py` — demonstrates importing project modules and using the standard library
- `test.py` — `fuzzy_math` function and pytest-based tests (partially implemented)

## Requirements

- Python 3.8+ (3.10/3.11 recommended)
- `pytest` (only needed to run `test.py`)

## Quick start

Run an example script:

```bash
python3 hello_world.py
python3 variables.py
python3 functions.py
```

Run tests (install `pytest` first):

```bash
python3 -m pip install --user pytest
python3 -m pytest test.py -q
```

## Notes

- The tests in `test.py` are partially implemented; you can extend them to cover all cases for `fuzzy_math`.
- `import.py` shows how to import and use classes from `classes.py` and other standard-library modules like `time`.

## Contributing

Feel free to open issues or submit pull requests with improvements, additional examples, or completed tests.

---

Generated on March 13, 2026.

