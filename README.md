# CI/CD with GitHub Actions

See: [python-package.yml](.github/workflows/python-package.yml)

# Links

[How to build a CI/CD pipeline with GitHub Actions in four simple steps](https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/)

# Static analysis

```shell
# pip install pylint
pylint $(git ls-files '*.py')
```

# Testing

```shell
# pip install pytest
pytest
```

# Create Binary

```shell
# pip install pyinstaller
pyinstaller --onefile src/main.py
```

# Run Binary

```shell
./dist/main
```