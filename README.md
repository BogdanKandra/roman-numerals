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
- Jupyter Notebook which illustrates usage of all Roman class functionality
- [Unit tests](https://docs.pytest.org/en/7.0.x/) for all functionality in the project
- Separate `requirements.txt` and `test-requirements.txt` files, holding the development and testing dependencies

Steps for using the project:
- Create a virtual environment for the project: `conda create -n <env_name> python=3.10`
- Activate the virtual environment: `conda activate <env_name>`
- Install the development dependencies: `pip install -r requirements.txt`
- Start Python interpreter, import the Roman class and play with Roman numbers!
  - Test by first importing the Roman class: `from scripts.roman import Roman`

Steps for testing the project:
- Create a virtual environment for the project (or activate the one created for the step above)
- Install the testing dependencies: `pip install -r test-requirements.txt`
- Run the [pytest](https://docs.pytest.org/en/8.1.x/) test suit from the project base directory: `python -m pytest tests`
  - Compute the test coverage: `coverage run --source=scripts -m pytest -v .\tests\`
  - Visualize the test coverage report (in the CLI): `coverage report -m`
  - Visualize the test coverage report (in the web browser): `coverage html` -> Then open the index.html file
- Run the [flake8](https://flake8.pycqa.org/en/latest/) linting tool from the project base directory: `flake8`
  - [Configure flake8](https://flake8.pycqa.org/en/latest/user/configuration.html) by editing the `.flake8` file
- Run the [mypy](https://mypy.readthedocs.io/en/stable/) static type checker from the project base directory: `mypy`
  - [Configure mypy](https://mypy.readthedocs.io/en/stable/config_file.html#config-file) by editing the `mypy.ini` file
