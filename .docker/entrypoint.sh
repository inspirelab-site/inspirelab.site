#!/bin/bash

# Refresh the container's citation data before serving.
python3 _cite/cite.py

# Recompile citations when source metadata is synchronized into the container.
watchmedo shell-command \
    --debug-force-polling \
    --recursive \
    --wait \
    --command="python3 _cite/cite.py" \
    --patterns="_data/sources*;_data/orcid*;_data/pubmed*;_data/google-scholar*" &

# Compose Watch restarts the container for configuration/plugin changes.
# Keep Jekyll in the foreground so build errors are visible and stop the preview.
# Generated files stay inside Docker, away from macOS file-sharing locks.
exec bundle exec jekyll serve \
    --force_polling --livereload --trace --host=0.0.0.0 \
    --destination /tmp/jekyll-site --disable-disk-cache
