#!/usr/bin/env bash
set -euo pipefail

# generate-release-notes.sh
# Generate release notes from git history with template checksums
# Usage: generate-release-notes.sh <new_version> <last_tag>

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <new_version> <last_tag>" >&2
  exit 1
fi

NEW_VERSION="$1"
LAST_TAG="$2"

# Get commits since last tag
if [ "$LAST_TAG" = "v0.0.0" ]; then
  # Check how many commits we have and use that as the limit
  COMMIT_COUNT=$(git rev-list --count HEAD)
  if [ "$COMMIT_COUNT" -gt 10 ]; then
    COMMITS=$(git log --oneline --pretty=format:"- %s" HEAD~10..HEAD)
  else
    COMMITS=$(git log --oneline --pretty=format:"- %s" HEAD~$COMMIT_COUNT..HEAD 2>/dev/null || git log --oneline --pretty=format:"- %s")
  fi
else
  COMMITS=$(git log --oneline --pretty=format:"- %s" $LAST_TAG..HEAD)
fi

# Create release notes with PMF branding
cat > release_notes.md << EOF
This is the latest set of releases that you can use with your agent of choice. We recommend using the PMF CLI to scaffold your projects, however you can download these independently and manage them yourself.

## Changelog

$COMMITS

## Assets

36 template variants with SHA-256 checksums:

EOF

# Add checksums for all generated templates
for zip in .genreleases/*.zip; do
  [[ -f "$zip" ]] || continue
  filename=$(basename "$zip")
  size=$(ls -lh "$zip" | awk '{print $5}')
  sha256=$(shasum -a 256 "$zip" | cut -d' ' -f1)

  echo "$filename" >> release_notes.md
  echo "sha256:$sha256" >> release_notes.md
  echo "$size" >> release_notes.md
  echo "" >> release_notes.md
done

echo "Generated release notes:"
cat release_notes.md
