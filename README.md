# CI/CD with GitHub Actions

> Why spend 5 minutes doing something ...
> when you could spend 5 hours failing to automate it?


See: [python-package.yml](.github/workflows/python-package.yml)

# Guide

[How to build a CI/CD pipeline with GitHub Actions in four simple steps](https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/)

# Pipeline

Install dependencies
```shell
pip install --upgrade pip
pip install pylint pytest pyinstaller
pip install -r requirements.txt
```

Static analysis
```shell
pylint $(git ls-files '*.py')
```

Testing

```shell
pytest
```

# How to use

Run Python 
```shell
python src/main.py --number_x 40 --number_y 2 
```

Create Binary (Linux)

```shell
pyinstaller --onefile src/main.py
```

Run Binary

```shell
# ./dist/main --help
 ./dist/main --number_x 40 --number_y 2  # -> x=40.0 + y=2.0 == 42.0
```
