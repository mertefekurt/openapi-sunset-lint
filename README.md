# Openapi Sunset Lint

![Openapi Sunset Lint cover](assets/readme-cover.svg)

Lint API deprecation notes for sunset, replacement, and migration gaps. I keep it small because this kind of check is most useful when it can run beside the work, not after the work has already shipped.

## Openapi Sunset Lint catches

- `missing-sunset` (high): sunset date is missing. Fix: Add a clear removal date..
- `missing-replacement` (medium): replacement endpoint is missing. Fix: Document the supported migration target..
- `no-migration-guide` (low): migration guide is missing. Fix: Link a migration guide or compatibility notes..

## A normal pass

```bash
git clone https://github.com/mertefekurt/openapi-sunset-lint.git
cd openapi-sunset-lint
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
openapi-sunset-lint examples/sample.txt
openapi-sunset-lint examples/sample.txt --json
```

The input can be text, JSON, JSONL, or CSV. Use `--json` when another script needs the result instead of a Markdown report.

## A deliberately bad line

```text
deprecated /v1/search sunset missing replacement none
```

## Maintainer loop

```bash
ruff check .
pytest
python -m openapi_sunset_lint --help
```
