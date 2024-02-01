#!/bin/bash

# Set the repository URL and token
REPO_URL="https://github.com/amineaith3/alx-higher_level_programming.git"
TOKEN="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"

# Set the commit message
COMMIT_MESSAGE="More commits"

# Make Python files executable
chmod u+x *.py

# Stage changes
git add .

# Commit changes
git commit -m "$COMMIT_MESSAGE"

# Push to the repository
git push "$REPO_URL" master

# Provide credentials using the token
git push "$REPO_URL" master --quiet -u "$TOKEN"

