# Local preview

Start Docker Desktop, then run `bash .docker/run.sh` from the repository root.
Open http://localhost:4000. Press Ctrl+C to stop the preview.

Docker Compose Watch copies source files into the container and synchronizes
saved edits. Jekyll builds into `/tmp/jekyll-site`. No project bind mount is used:
Docker Desktop previously returned EIO when reading source files and EDEADLK
when writing generated CSS through that mount.

Requires a recent Docker Compose with Watch and sync+restart support.
Configuration and plugin changes restart the preview; dependency changes rebuild
the image. Ordinary page and style changes use Jekyll live reload.

Citation refreshes at startup update the container's copy of `citations.yaml`.
To save regenerated citations back to the repository while preview is running:

```bash
docker compose -f .docker/compose.yaml exec preview python3 _cite/cite.py
docker compose -f .docker/compose.yaml cp preview:/usr/src/app/_data/citations.yaml _data/citations.yaml
```

Review and commit that file as usual. Source synchronization is one way, from the
host into Docker; other container-generated files do not modify the repository.

To remove the stopped preview container:

```bash
docker compose -f .docker/compose.yaml down
```
