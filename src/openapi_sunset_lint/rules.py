from __future__ import annotations

from openapi_sunset_lint.models import Rule

PROJECT_NAME = 'openapi-sunset-lint'
SUMMARY = 'Lint API deprecation notes for sunset, replacement, and migration gaps.'
SAMPLE_RISK = 'deprecated /v1/search sunset missing replacement none'
SAMPLE_CLEAN = (
                   'deprecated /v1/search sunset 2026-12-31 replacement /v2/search migration'
                   ' guide linked'
               )
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='missing-sunset',
        severity='high',
        pattern='\\bsunset\\s*(missing|none|null)\\b',
        message='sunset date is missing',
        recommendation='Add a clear removal date.',
    ),
    Rule(
        code='missing-replacement',
        severity='medium',
        pattern='\\breplacement\\s*(none|missing|null)\\b',
        message='replacement endpoint is missing',
        recommendation='Document the supported migration target.',
    ),
    Rule(
        code='no-migration-guide',
        severity='low',
        pattern='\\bmigration guide\\s*(missing|none|null)\\b',
        message='migration guide is missing',
        recommendation='Link a migration guide or compatibility notes.',
    ),
)
