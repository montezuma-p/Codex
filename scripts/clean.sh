# scripts/clean.sh

#!/bin/bash
set -e

find . -type d -name '__pycache__' -exec rm -rf {} +
find . -type f -name '*.pyc' -delete
rm -rf .pytest_cache .mypy_cache .coverage htmlcov
echo "Limpeza completa de arquivos temporários, caches e bytecode."
