# openapi-sunset-lint

**Release Gate.** Lint API deprecation notes for sunset, replacement, and migration gaps.

## Risk It Reduces

Deprecated endpoints stay risky when clients do not get a date or replacement path. This CLI audits API lifecycle notes.

## Run Locally

`openapi-sunset-lint` accepts OpenAPI deprecation notes or changelog text in text, JSON, JSONL, or CSV form.

## Automate

```bash
python -m pip install -e ".[dev]"
openapi-sunset-lint examples/sample.txt
openapi-sunset-lint examples/sample.txt --json --fail-on medium
```

## Rule Table

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-sunset` | high | sunset date is missing |
| `missing-replacement` | medium | replacement endpoint is missing |
| `no-migration-guide` | low | migration guide is missing |

## Testing

```bash
ruff check .
pytest
python -m openapi_sunset_lint --help
```

License: MIT

### Example Input

```text
deprecated /v1/search sunset missing replacement none
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the openapi-sunset-lint policy surface explicit.
