#!/bin/bash
# Läufe 2026-11-13 zu Restsatz M14: Zerlegung von ∫f² nach der Länge K der gemeinsamen Kopfkette
# (pruef_kopfteilen2d.py), Variante c (Ball R = 3) mit Pflicht-Querschritt, Grundzustand, S = 8.
# Aufruf: bash kopfteilen2d_start.sh <Parallelität> <Stunden je Lauf>
cd "$(dirname "$0")"
P=${1:-12}
STD=${2:-0.4}
OUT=ergebnisse/kopfteilen2d
jobs=()
for w in 2 3 4; do
  jobs+=("m1_6x4 $w --Lx 6 --Ly 4 --N 6 --cx 2 --cy 2")
  jobs+=("m1.5_6x4 $w --Lx 6 --Ly 4 --N 6 --cx 3 --cy 2")
  jobs+=("m3_6x4 $w --Lx 6 --Ly 4 --N 6 --cx 6 --cy 2")
done
for N in 4 6 8; do
  jobs+=("4x4_N$N 3 --Lx 4 --Ly 4 --N $N --cx 2 --cy 2")
done
printf '%s\n' "${jobs[@]}" | xargs -P "$P" -L 1 bash -c '
  sn=$0; w=$1; shift 1
  python3 pruef_kopfteilen2d.py --S 8 --w $w "$@" --abweg ball --radius 3 --querschritt --locker --zuege alle \
     --proben 1000000 --zeit '"$STD"' --zwischen 1000 --seed $((w*11+5)) > '"$OUT"'/${sn}_w${w}.txt 2>&1'
echo "fertig: $(date)" > $OUT/FERTIG
