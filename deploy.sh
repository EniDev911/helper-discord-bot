#!/usr/bin/env sh

git checkout -b main
git add -A
git commit -m 'new deploy'
git push -f origin main
