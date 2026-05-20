# python_repo

Small collection of Python examples and practice scripts covering core Python
syntax, interview-style coding problems, and pytest-based API tests.

## Project Structure

- `python_basics/` - beginner examples for variables, functions, control flow,
  classes, exceptions, imports, and simple tests.
- `python_practice/` - coding practice exercises, useful helper functions, and
  interview-style problems.
- `tests/api_petstore/` - pytest suite for the public Swagger Petstore API.
- `tests/api_petstore2/` - Petstore client utilities and related test code.

## Python Basics

- `python_basics/hello_world.py` - simple "hello, world!" example.
- `python_basics/variables.py` - numbers, strings, booleans, lists, dicts, and
  `type()`.
- `python_basics/functions.py` - function definitions, default arguments, and
  simple math examples.
- `python_basics/control_flow.py` - `if`/`elif`/`else` and `for` loop examples.
- `python_basics/classes.py` - `Vehicle`, `Motorcycle`, and `Car` classes with
  methods and `__repr__`.
- `python_basics/exceptions.py` - raising and handling errors.
- `python_basics/import.py` - importing project modules and using standard
  library modules like `time`.
- `python_basics/test.py` - `fuzzy_math` function and pytest-based tests.

## Requirements

- Python 3.8+; Python 3.10 or 3.11 is recommended.
- `pytest`, installed from `requirements-dev.txt`, to run the local and API test
  suites.

## Quick Start

Run an example script:

```bash
python3 python_basics/hello_world.py
python3 python_basics/variables.py
python3 python_basics/functions.py
```

Install test dependencies:

```bash
python3 -m pip install -r requirements-dev.txt
```

Run the local basics tests:

```bash
python3 -m pytest python_basics/test.py -q
```

Run the Petstore API tests:

```bash
python3 -m pytest tests/api_petstore -q
```

The Petstore suite uses the public Swagger Petstore service at
`https://petstore.swagger.io/v2`, so those tests require network access and can
reflect temporary state or availability issues in that shared demo API.

## Notes

- The tests in `python_basics/test.py` can be extended to cover all cases for
  `fuzzy_math`.
- Keep shared project instructions in this root README. Directory-level README
  files should link back here instead of duplicating the same setup steps.

## Contributing

Feel free to open issues or submit pull requests with improvements, additional
examples, or completed tests.
