# packagetest

#This is required for the package to be imported
#pip install -r requirements.txt

# explanation

1. ci.yaml: CI workflow ran by Github Actions when pushing or merging
   a. identifies virtual env
   b. sets up python
   c. install dependencies (for linting, testing, and src): can include all dependencies in requirement.txt
   d. run linting/tests with tox (refer to tox.ini)
2. python-publish.yml: CD workflow ran by Github Actions when releasing
   a. sets up env/python
   b. install dependencies
   c. build as package (refer to setup.py/setup.cfg/pyproject.toml)
   d. publish to pypi
