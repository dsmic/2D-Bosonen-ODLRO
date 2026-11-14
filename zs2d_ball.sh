#!/bin/bash
# Kurzlauf 2026-11-11: Abweg "ball" (Anfang aus dem bedingten Gesetz im Torus-Manhattan-Ball vom Radius R um Y_m)
# am System m = 1 des Nachtlaufs (6×4, N = 6, Zellen 2×2), R = 1, 2, 3, mit und ohne Pflicht-Querschritt, w = 1..4.
# Aufruf: bash zs2d_ball.sh <Parallelität> <Stunden je Lauf>
cd "$(dirname "$0")"
P=${1:-14}
STD=${2:-0.25}
OUT=ergebnisse/zs2d_nacht
jobs=()
for w in 1 2 3 4; do
  for R in 1 2 3; do
    jobs+=("m1 ballR$R $w --Lx 6 --Ly 4 --N 6 --cx 2 --cy 2 --abweg ball --radius $R --locker")
    jobs+=("m1 ballqR$R $w --Lx 6 --Ly 4 --N 6 --cx 2 --cy 2 --abweg ball --radius $R --querschritt --locker")
  done
done
printf '%s\n' "${jobs[@]}" | xargs -P "$P" -L 1 bash -c '
  sn=$0; vn=$1; w=$2; shift 2
  nice -n 0 python3 zeitschleife2d.py --modus mc --S 8 --beta 0 --zuege alle --w $w "$@" \
     --proben 1000000 --zeit '"$STD"' --zwischen 2000 --seed $((w*7+3)) \
     --fdatei '"$OUT"'/${sn}_${vn}_w${w}.npy > '"$OUT"'/${sn}_${vn}_w${w}.txt 2>&1'
echo "Kurzlauf ball fertig: $(date)" > $OUT/FERTIG_ball
