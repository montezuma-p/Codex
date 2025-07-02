# scripts/test.sh

#!/bin/bash
set -e

pytest --cov=src/codex --cov-report=term-missing
