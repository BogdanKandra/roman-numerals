# roman-numerals-class
Roman numerals convertor, a little project illustrating advanced Python concepts

This project contains:
- User-defined class with constructors, static methods and many overriden [magic methods](https://docs.python.org/3/reference/datamodel.html)
  - Users are able to do type conversion, string representation, arithmetic and comparison operations, using Roman numerals and other numeric types
- Custom made [decorator](https://www.python.org/dev/peps/pep-0318/)
- Custom made [enum](https://docs.python.org/3/library/enum.html)
- Custom made [exceptions](https://docs.python.org/3/tutorial/errors.html)
- Custom made [generator](https://python-reference.readthedocs.io/en/latest/docs/generator/)
- Implementation of the [Iterator Protocol](https://wiki.python.org/moin/Iterator)
- [Unit tests](https://docs.pytest.org/en/7.0.x/) for all functionality in the project
- Requirements file, holding the dependencies

Steps for using the project:
- Create a virtual environment for the project and activate it: `conda create -n env_name python=3.10`
- Install the dependencies: `pip install -r requirements.txt`
- Run the test suit from the project base directory: `python -m pytest tests`
- Start Python interpretor, import the Roman class and play with Roman numbers!
