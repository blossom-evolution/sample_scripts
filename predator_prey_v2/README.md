# Predator-Prey v2 (Native Intent API)

This folder is the active predator-prey workspace for Blossom's native
intent API. It is fully runnable on current Blossom and does not require a
sample-local bridge.

## What this sample gives you

- Runnable predator-prey config (`config.yml`).
- Intent-style custom callbacks in `custom_behaviors.py`.
- Reference intent payload printer (`print_intent_example.py`).
- Convenience runner (`run_sim.py`).

## Quickstart

From repo root:

```bash
cd sample_scripts/predator_prey_v2
conda run -n blossom python run_sim.py --verbosity 1
```

Optional seed/timestep override:

```bash
conda run -n blossom python run_sim.py --seed 7 --timesteps 400 --verbosity 1
```

Dashboard (from this directory):

```bash
conda run -n blossom blossom dashboard . -p 8888
```

Open: `http://localhost:8888`

## Intent API usage pattern

1. Import from core API:

```python
from blossom.simulation import (
    BehaviorContext,
    CompositeIntent,
    FieldChange,
    OrganismView,
    UpdateIntent,
)
```

2. Write callbacks with `(org, ctx)` parameters (this is now default):

```python
def eat_prey(org: OrganismView, ctx: BehaviorContext) -> CompositeIntent:
    ...
```

3. Query state from `ctx` (read-only):

- `ctx.at_location(location)`
- `ctx.by_species("prey", alive_only=True)`
- `ctx.nearest(source_id, k, species="prey")`

4. Return explicit proposed effects:

- `UpdateIntent` for existing organisms.
- `SpawnIntent` for new organisms.

5. Reference callback name in `config.yml` (`action`, `movement`, `eating`, etc).

Legacy note:

- Legacy callbacks are still available, but must be explicitly marked with
  `@legacy_behavior`.

## Why this is clearer for users

- Reads and writes are separated:
  - Read through `BehaviorContext`.
  - Write through explicit intent payloads.
- Intent payloads are auditable and easier to debug than hidden shared-state
  mutation.
- `parse_intent` remains the consistency boundary for conflicting outcomes.

## File map

- `config.yml`: runnable project config for current Blossom.
- `run_sim.py`: convenience runner for this folder.
- `custom_behaviors.py`: predator/prey behavior logic.
- `print_intent_example.py`: prints a sample intent JSON payload.
- `context.py`: local import helper for Blossom package.

## Notes

- Outputs (`data/`, `logs/`) are ignored by `.gitignore` in this folder.
- This folder is meant to be the iteration surface for the "new age" API
  direction while still remaining runnable today.
