# Internal Repository Content

This directory contains internal project management content that should NOT be
included in the public repository.

## Contents

- `project/` - Project management, planning, learnings
- `docs/` - Internal documentation (ADRs, investigations, setup)
- `reports/` - Status reports and analytics
- `scripts/` - Internal automation scripts
- `.github/` - Internal GitHub configurations
- `AGENTS.md` - AI agent quick reference

## Important

When publishing to the public repo, everything in `_internal/` is excluded
via the allowlist strategy. See `../private_to_public_clean_mirror_workflow.md`.
