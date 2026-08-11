#!/bin/sh
# Double-click to open the console. macOS and Linux.
#
# The console's audience is the product manager, and a terminal is a wall for that reader, so the
# command they were told to type lives in a file they can open instead. It does exactly what the
# README documents, in the folder it sits in, with no arguments to remember.
#
# ASCII only, on purpose: this text is printed by whatever shell the machine happens to run, and a
# dash that arrives as a box is the same failure this project refuses everywhere else.
#
# Windows: use console.bat next to this file.

cd "$(dirname "$0")/../.." || exit 1

PY=""
for c in python3 python; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; raise SystemExit(0 if sys.version_info[0] == 3 else 1)' 2>/dev/null; then
    PY="$c"
    break
  fi
done

if [ -z "$PY" ]; then
  echo ""
  echo "  Python 3 is missing. It is all this needs, and it is the only thing missing."
  echo "  Install it from https://www.python.org/downloads/ and double-click this file again."
  echo ""
  printf "  Press Enter to close. "
  read -r _
  exit 1
fi

echo ""
echo "  Opening the console in your browser. It only reads the product folder, it changes nothing."
echo "  Close this window, or press Ctrl+C, to stop it."
echo ""

"$PY" tools/ui/serve.py "$@"
