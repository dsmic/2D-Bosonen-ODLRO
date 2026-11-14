#!/bin/bash
# Läufe 2026-11-13: Fortsetzung des Teilens am Schwanz gegen die Scheibendauer S (4×4, N = 4, Zellen 2×2, w = 2).
# Aufruf: bash kopfteilen2d_schwanz_S.sh <Parallelität> <Stunden je Lauf>
cd "$(dirname "$0")"
P=${1:-4}
STD=${2:-0.33}
OUT=ergebnisse/kopfteilen2d_schwanz
printf '%s\n' 4 12 16 24 | xargs -P "$P" -I{} bash -c '
  python3 pruef_kopfteilen2d.py --S {} --w 2 --Lx 4 --Ly 4 --N 4 --cx 2 --cy 2 --abweg ball --radius 3 --querschritt --locker \
     --zuege alle --proben 1000000 --zeit '"$STD"' --zwischen 1000 --seed 23 > '"$OUT"'/S{}_4x4_N4_w2.txt 2>&1'
echo "fertig: $(date)" > $OUT/FERTIG_S
