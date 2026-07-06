<p align="center">
  <img src="assets/readme-cover.svg" alt="Openapi Sunset Lint cover" width="100%" />
</p>

# Openapi Sunset Lint

![stack](https://img.shields.io/badge/stack-Python-2563eb?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-16a34a?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-dc2626?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-7c3aed?style=flat-square)

Lint API deprecation notes for sunset, replacement, and migration gaps.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `openapi-sunset-lint` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
openapi-sunset-lint examples/sample.txt
openapi-sunset-lint examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-sunset` | high | sunset date is missing |
| `missing-replacement` | medium | replacement endpoint is missing |
| `no-migration-guide` | low | migration guide is missing |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
deprecated /v1/search sunset missing replacement none
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m openapi_sunset_lint --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Openapi Sunset Lint policy easy to review.
