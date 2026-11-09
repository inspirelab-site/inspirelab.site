#!/bin/bash
set -euo pipefail

# Resolve paths from this script, so it also works outside the repository root.
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
COMPOSE_FILE="${SCRIPT_DIR}/compose.yaml"

# Compose Watch synchronizes edits without a Docker Desktop project bind mount.
if (( $# )); then
    docker compose --file "$COMPOSE_FILE" build preview
    exec docker compose --file "$COMPOSE_FILE" run --rm --service-ports preview "$@"
else
    exec docker compose --file "$COMPOSE_FILE" up --build --watch
fi
