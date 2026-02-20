#!/usr/bin/env python3
"""Run predator-prey v2 simulation from this project directory."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from context import blossom


def load_runtime_options(config_path: Path) -> dict[str, int | bool | None]:
    """Load runtime options from config.

    Args:
        config_path: Config YAML path.

    Returns:
        Runtime settings used by this convenience runner.
    """
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)
    return {
        "timesteps": int(cfg.get("timesteps", 1000)),
        "organism_limit": cfg.get("organism_limit"),
        "snapshot_interval": int(cfg.get("snapshot_interval", 1)),
        "log_interval": int(cfg.get("log_interval", 1)),
        "retain_last_checkpoints": cfg.get("retain_last_checkpoints"),
        "compact_json_output": bool(cfg.get("compact_json_output", False)),
        "validate_invariants": bool(cfg.get("validate_invariants", False)),
    }


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Run predator-prey v2 simulation")
    parser.add_argument(
        "--config",
        default="config.yml",
        help="Path to project config YAML",
    )
    parser.add_argument(
        "--timesteps",
        type=int,
        default=None,
        help="Optional timestep override",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional seed override",
    )
    parser.add_argument(
        "--verbosity",
        type=int,
        default=1,
        help="Progress verbosity for console output",
    )
    args = parser.parse_args()

    project_dir = Path(__file__).resolve().parent
    config_path = (project_dir / args.config).resolve()
    runtime_options = load_runtime_options(config_path)
    timesteps = (
        args.timesteps
        if args.timesteps is not None
        else int(runtime_options["timesteps"])
    )

    universe = blossom.Universe(
        config_fn=config_path,
        project_dir=project_dir,
        end_time=timesteps,
        seed=args.seed,
        organism_limit=runtime_options["organism_limit"],
        snapshot_interval=runtime_options["snapshot_interval"],
        log_interval=runtime_options["log_interval"],
        retain_last_checkpoints=runtime_options["retain_last_checkpoints"],
        compact_json_output=runtime_options["compact_json_output"],
        validate_invariants=runtime_options["validate_invariants"],
    )
    universe.run(verbosity=args.verbosity, expanded=False)

    print(f"Run complete: {universe.run_data_dir.name}")
    print(f"Data dir: {universe.run_data_dir}")
    print(f"Logs dir: {universe.run_logs_dir}")


if __name__ == "__main__":
    main()
