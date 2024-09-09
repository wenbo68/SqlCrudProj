# packagetest

#This is required for the package to be imported
#pip install -r requirements.txt

# explanation

1. ci.yaml: CI workflow ran by Github Actions when pushing or merging
   a. identifies virtual env
   b. sets up python
   c. install dependencies used for CI (linting, testing)
   d. run linting/tests with tox
2. python-publish.yml: CD workflow ran by Github Actions when releasing
   a. sets up env/python
   b. 
