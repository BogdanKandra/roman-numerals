# roman-numerals-class
Roman numerals convertor, a little project illustrating OOP concepts in Python

This project contains:
- User-defined class, with constructors, static methods and many overriden [magic methods](https://docs.python.org/3/reference/datamodel.html) (_scripts/roman.py_)
- Custom made [decorator](https://www.python.org/dev/peps/pep-0318/) (_scripts/roman.py_)
- Custom made [enum](https://docs.python.org/3/library/enum.html) (_scripts/enums.py_)
- Custom made [exceptions](https://docs.python.org/3/tutorial/errors.html) (_scripts/exceptions.py_)
- [Unit tests](https://docs.pytest.org/en/7.0.x/) for all functionality in the project (_tests\test_roman.py_)
- Requirements file, holding the dependencies (_requirements.txt_)

Steps for using the project:
- Create a virtual environment for the project and activate it: `conda create -n env_name python=3.10`
- Install the dependencies: `pip install -r requirements.txt`
- Run the test suit from the project base directory: `python -m pytest tests`
- Start Python interpretor, import the Roman class and play with Roman numbers!
