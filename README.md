# Example Usage Comparison of pyproject.toml vs setup.py

- Using setup.py:
  - Create python venv as usual and activate
  - pip install -r requirements.txt
  -  python setup.py bdist_wheel
    - You will get this message:
    - ```
        /Users/metecanakar/VisualStudioCodeProjects/comparison-pyproject-toml-vs-setup-py/setuppy-venv/lib/python3.10/site-packages/setuptools/_distutils/cmd.py:66: SetuptoolsDeprecationWarning: setup.py install is deprecated.

            ********************************************************************************
            Please avoid running ``setup.py`` directly.
            Instead, use pypa/build, pypa/installer or other
            standards-based tools.

            See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
            ********************************************************************************
        ```
- Using Pyproject.toml:
  - Create python venv as usual and activate it
  - pip install .
  - python -m build (make sure there is no setup.py in the same directory otherwise it might try to run the setup.py)
