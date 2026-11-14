#!/bin/bash
# Kurzlauf 2026-11-11: Abweg ohne Route (nur Zug d = 0, --nie_quer): Ball R = 1, 2, 3 und freier Anfang, m = 1 und 3, w = 1..4.
# Aufruf: bash zs2d_nie_quer.sh <Parallelität> <Stunden je Lauf>
cd "$(dirname "$0")"
P=${1:-14}
STD=${2:-0.25}
OUT=ergebnisse/zs2d_nacht
M1="--Lx 6 --Ly 4 --N 6 --cx 2 --cy 2"
M3="--Lx 6 --Ly 4 --N 6 --cx 6 --cy 2"
jobs=()
for w in 1 2 3 4; do
  for R in 1 2 3; do
    jobs+=("m1 bnR$R $w $M1 --abweg ball --radius $R --locker --nie_quer")
  done
  jobs+=("m1 freinq $w $M1 --abweg frei --locker --nie_quer")
  jobs+=("m3 bnR3 $w $M3 --abweg ball --radius 3 --locker --nie_quer")
  jobs+=("m3 freinq $w $M3 --abweg frei --locker --nie_quer")
done
printf '%s\n' "${jobs[@]}" | xargs -P "$P" -L 1 bash -c '
  sn=$0; vn=$1; w=$2; shift 2
  nice -n 0 python3 zeitschleife2d.py --modus mc --S 8 --beta 0 --zuege alle --w $w "$@" \
     --proben 1000000 --zeit '"$STD"' --zwischen 2000 --seed $((w*7+3)) \
     --fdatei '"$OUT"'/${sn}_${vn}_w${w}.npy > '"$OUT"'/${sn}_${vn}_w${w}.txt 2>&1'
echo "Kurzlauf nie_quer fertig: $(date)" > $OUT/FERTIG_nie_quer
