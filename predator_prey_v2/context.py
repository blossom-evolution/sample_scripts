"""Local import context for Blossom sample scripts."""

from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[2]
BLOSSOM_ROOT = REPO_ROOT / "blossom"
if str(BLOSSOM_ROOT) not in sys.path:
    sys.path.insert(0, str(BLOSSOM_ROOT))

import blossom  # noqa: E402
