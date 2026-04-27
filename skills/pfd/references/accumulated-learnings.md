# PFD Accumulated Learnings — superseded by sharded architecture (v0.5+)

This file is retained as a pointer for backward compatibility with external links.

**Learnings now live as atom files under [`learnings/`](learnings/).** Query via:

- [`learnings/_index.md`](learnings/_index.md): human-readable, grouped by layer, sorted by date
- [`learnings/_search.json`](learnings/_search.json): machine-readable, flat array for programmatic filters

See `SKILL.md` § Accumulated Learnings for the query sequence (read the index first, drill into specific atom files on demand).

**Why the change:** lazy-load via lightweight index scales to 1000+ learnings without the per-activation cost blowup of the monolithic format.
