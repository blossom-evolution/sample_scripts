#!/usr/bin/env python3
"""Print a concrete intent payload example for user reference."""

from __future__ import annotations

from dataclasses import asdict
import json

from context import blossom  # noqa: F401
from blossom.simulation import CompositeIntent, FieldChange, UpdateIntent


def main() -> None:
    """CLI entry point."""
    payload = CompositeIntent(
        actor_id="predator-001",
        updates=(
            UpdateIntent(
                organism_id="predator-001",
                changes=(FieldChange(field="food_current", op="add", value=40),),
            ),
            UpdateIntent(
                organism_id="prey-117",
                changes=(
                    FieldChange(field="alive", op="set", value=False),
                    FieldChange(field="cause_of_death", op="set", value="eaten"),
                ),
            ),
        ),
    )
    print(json.dumps(asdict(payload), indent=2))


if __name__ == "__main__":
    main()
