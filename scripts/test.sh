# scripts/test.sh

#!/bin/bash
set -e

pytest --cov=. --cov-report=term-missing
