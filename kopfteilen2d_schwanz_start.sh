#!/bin/bash
# Läufe 2026-11-13 zu Restsatz M14: Fortsetzung des Teilens am Schwanz (Lochkette) gegen die Zellgröße s².
# pruef_kopfteilen2d.py mit Zerlegung nach K (Kopf) und K_T (Schwanz), Variante c (Ball R = 3), Pflicht-Querschritt.
# Aufruf: bash kopfteilen2d_schwanz_start.sh <Parallelität> <Stunden je Lauf>
cd "$(dirname "$0")"
P=${1:-8}
STD=${2:-0.33}
OUT=ergebnisse/kopfteilen2d_schwanz
jobs=()
jobs+=("s4_m1_6x4 --Lx 6 --Ly 4 --N 6 --cx 2 --cy 2")
jobs+=("s6_m1.5_6x4 --Lx 6 --Ly 4 --N 6 --cx 3 --cy 2")
jobs+=("s12_m3_6x4 --Lx 6 --Ly 4 --N 6 --cx 6 --cy 2")
for N in 4 6 8; do jobs+=("s4_4x4_N$N --Lx 4 --Ly 4 --N $N --cx 2 --cy 2"); done
jobs+=("s8_4x4_N4 --Lx 4 --Ly 4 --N 4 --cx 4 --cy 2")

printf '%s\n' "${jobs[@]}" | xargs -P "$P" -L 1 bash -c '
  sn=$0
  python3 pruef_kopfteilen2d.py --S 8 --w 2 "$@" --abweg ball --radius 3 --querschritt --locker --zuege alle \
     --proben 1000000 --zeit '"$STD"' --zwischen 1000 --seed 17 > '"$OUT"'/${sn}_w2.txt 2>&1'
echo "fertig: $(date)" > $OUT/FERTIG

# Zweiter Satz (Scheibendauer S): kopfteilen2d_schwanz_S.sh
