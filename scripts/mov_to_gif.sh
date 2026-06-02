#!/bin/zsh
# Convert .mov files to .gif using ffmpeg
# Usage:
#   ./mov_to_gif.sh                        # convert all .mov in current dir
#   ./mov_to_gif.sh file.mov               # convert a single file
#   ./mov_to_gif.sh -w 480 file.mov        # custom width (default: 640)
#   ./mov_to_gif.sh -f 10 file.mov         # custom fps (default: 15)
#   ./mov_to_gif.sh -w 480 -f 10 *.mov     # custom width + fps, multiple files

set -e

WIDTH=640
FPS=15
FILES=()

usage() {
  echo "Usage: $(basename $0) [-w width] [-f fps] [file.mov ...]"
  echo "  -w  Output width in pixels (default: 640, height auto-scaled)"
  echo "  -f  Frames per second (default: 15)"
  echo "  If no files given, converts all .mov in the current directory."
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -w) WIDTH="$2"; shift 2 ;;
    -f) FPS="$2";   shift 2 ;;
    -h|--help) usage ;;
    -*) echo "Unknown option: $1"; usage ;;
    *) FILES+=("$1"); shift ;;
  esac
done

if ! command -v ffmpeg &>/dev/null; then
  echo "Error: ffmpeg not found. Install with: brew install ffmpeg"
  exit 1
fi

if [[ ${#FILES[@]} -eq 0 ]]; then
  FILES=(*.mov(N))
  if [[ ${#FILES[@]} -eq 0 ]]; then
    echo "No .mov files found in current directory."
    exit 1
  fi
fi

echo "Settings: ${WIDTH}px wide, ${FPS}fps"
echo "Converting ${#FILES[@]} file(s)...\n"

SUCCESS=0
FAIL=0

for INPUT in "${FILES[@]}"; do
  if [[ ! -f "$INPUT" ]]; then
    echo "  Skipping (not found): $INPUT"
    ((FAIL++))
    continue
  fi

  OUTPUT="${INPUT:r}.gif"
  printf "  %-40s -> %s\n" "$INPUT" "$OUTPUT"

  if ffmpeg -i "$INPUT" \
    -vf "fps=${FPS},scale=${WIDTH}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
    -loop 0 "$OUTPUT" -y 2>/dev/null; then
    SIZE=$(du -sh "$OUTPUT" | cut -f1)
    echo "     Done ($SIZE)"
    ((SUCCESS++))
  else
    echo "     Failed."
    ((FAIL++))
  fi
done

echo "\n$SUCCESS converted, $FAIL failed."
