# How to build locally ?

### Clone the project
```
git clone https://github.com/hellstein/codegen-statemachine.git
```

### Install dependencies
* `python3`
* `pip3`

### Create python package for testing
```
cd codegen-statemachine
make update
```
* We use the PyPI repo for development, you can check `Makefile` to see the build and test process.
* If you need knowledge how the python package works, please do read [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/).
* The python package has been built and uploaded into [pypi.org](https://pypi.org/project/smgen/).

### Generate state machine applcation
```
make test
```
The application `app` is generated according to `conf` directory.

### Test the application
```
cd app
python3 context.py
```
