# aoc23
https://adventofcode.com/2023


## Design decisions

### Initial setup before coding
Using [poetry](https://python-poetry.org/) for dependency management.
Using [Black](https://github.com/psf/black) for formatting.
Using [pytest](https://docs.pytest.org) for testing.

## Run locally
Install if you haven't already. This will create the virtual env and install teh dependencies.
```
poetry install
```

Start poetry shell to get into the virtual environment
poetry shell
```

```
python src/part1.py
```


### Run formatter:
In the poetry shell run:
```
black .
```

### Run tests
In the poetry shell run:
```
pytest tests/
```

### Add a new package
```
poetry add fastapi
```

## Troubleshooting
### Poetry install issues
Update dependencies in the poetry.lock file with:
```
poetry update
```

or run a check with:
```
poetry check
```

### GitPod setup
If you get this error:
```
bash: __vsc_prompt_cmd_original: command not found
```
run:
```
unset PROMPT_COMMAND
```

### Pytest
Test files should start with test or it will not be automatically picked up