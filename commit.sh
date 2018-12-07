#!/bin/bash
if [ $# -ne 1 ]
then
  echo "Usage: commit.sh [commit desc]"
  exit 1
fi
git add .
git commit -m "$1"
git pull && git push
