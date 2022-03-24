# roman-numerals
Roman numerals convertor, a little project illustrating advanced Python project development practices and OOP concepts

This project contains:
- User-defined class with constructors, static methods and many overriden [magic methods](https://docs.python.org/3/reference/datamodel.html)
  - Users are able to do type conversion, string representation, arithmetic and comparison operations, using Roman numerals and other numeric types
- Custom made [decorator](https://www.python.org/dev/peps/pep-0318/)
- Custom made [enum](https://docs.python.org/3/library/enum.html)
- Custom made [exceptions](https://docs.python.org/3/tutorial/errors.html)
- Custom made [generator](https://python-reference.readthedocs.io/en/latest/docs/generator/)
- Implementation of the [Iterator Protocol](https://wiki.python.org/moin/Iterator)
- [Pytest](https://docs.pytest.org/en/7.0.x/) integration for unit testing all functionality in the project
- [Flake8](https://flake8.pycqa.org/en/latest/) integration, a linter (including the PEP8 coding style)
- [Mypy](https://flake8.pycqa.org/en/latest/) integration, a static type checker
- [requirements.txt](https://note.nkmk.me/en/python-pip-install-requirements/) file, holding the project's _production dependencies_ - dependencies which are needed to run the application; this project doesn't have any such dependencies, however for illustration purposes, NumPy was mentioned
- [requirements_dev.txt](https://realpython.com/lessons/production-vs-development-dependencies/) file, holding the project's _development dependencies_ - dependencies which are only needed during the development of the application

Steps for using the project:
- Create a virtual environment for the project and activate it: `conda create -n env_name python=3.10`
- Install the dependencies: `pip install -r requirements.txt`
- Run the test suit from the project base directory: `python -m pytest tests`
- Start Python interpretor, import the Roman class and play with Roman numbers!
