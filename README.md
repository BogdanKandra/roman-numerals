# roman-numerals
Roman numerals convertor, a small project illustrating advanced Python concepts

This project contains:
- User-defined class with constructors, static methods and many overriden [magic methods](https://docs.python.org/3/reference/datamodel.html)
  - Users are able to do type conversion, string representation, arithmetic and comparison operations, using Roman numerals and other numeric types
- Custom made [coroutines](https://docs.python.org/3/library/asyncio-task.html)
- Custom made [decorator](https://www.python.org/dev/peps/pep-0318/)
- Custom made [enum](https://docs.python.org/3/library/enum.html)
- Custom made [exceptions](https://docs.python.org/3/tutorial/errors.html)
- Custom made [generators](https://python-reference.readthedocs.io/en/latest/docs/generator/)
- Implementation of the [Iterator Protocol](https://wiki.python.org/moin/Iterator)
- [Unit tests](https://docs.pytest.org/en/7.0.x/) for all functionality in the project
- Requirements file, holding the runtime dependencies

Steps for using the project:
- Create a virtual environment for the project and activate it: `conda create -n env_name python=3.10`
- Install the dependencies: `pip install -r requirements.txt`
- Start Python interpreter, import the Roman class and play with Roman numbers!

Steps for testing the project:
- Run the [pytest](https://docs.pytest.org/en/8.1.x/) test suit from the project base directory: `python -m pytest tests`
- Run the [flake8](https://flake8.pycqa.org/en/latest/) linting tool from the project base directory: `flake8`
  - [Configure flake8](https://flake8.pycqa.org/en/latest/user/configuration.html) by editing the `.flake8` file
- Run the [mypy](https://mypy.readthedocs.io/en/stable/) static type checker from the project base directory: `mypy`
  - [Configure mypy](https://mypy.readthedocs.io/en/stable/config_file.html#config-file) by editing the `mypy.ini` file
