#!/bin/bash
# Kurzlauf 2026-11-11: Abweg "zellgewicht" (Anfang aus dem bedingten Gesetz auf freien Plätzen der Zielzelle)
# am System des Nachtlaufs (6×4, N = 6), m = 1 und 3, mit und ohne Pflicht-Querschritt, w = 1..4.
# Aufruf: bash zs2d_zellgewicht.sh <Parallelität> <Stunden je Lauf>
cd "$(dirname "$0")"
P=${1:-14}
STD=${2:-0.3}
OUT=ergebnisse/zs2d_nacht
jobs=()
systeme=(
  "m1|--Lx 6 --Ly 4 --N 6 --cx 2 --cy 2"
  "m3|--Lx 6 --Ly 4 --N 6 --cx 6 --cy 2"
)
varianten=(
  "zgq|--abweg zellgewicht --querschritt --locker"
  "zg|--abweg zellgewicht --locker"
)
for w in 1 2 3 4; do
  for s in "${systeme[@]}"; do
    sn=${s%%|*}; sa=${s#*|}
    for v in "${varianten[@]}"; do
      vn=${v%%|*}; va=${v#*|}
      jobs+=("$sn $vn $w $sa $va")
    done
  done
done
printf '%s\n' "${jobs[@]}" | xargs -P "$P" -L 1 bash -c '
  sn=$0; vn=$1; w=$2; shift 2
  nice -n 0 python3 zeitschleife2d.py --modus mc --S 8 --beta 0 --zuege alle --w $w "$@" \
     --proben 1000000 --zeit '"$STD"' --zwischen 2000 --seed $((w*7+3)) \
     --fdatei '"$OUT"'/${sn}_${vn}_w${w}.npy > '"$OUT"'/${sn}_${vn}_w${w}.txt 2>&1'
echo "Kurzlauf zellgewicht fertig: $(date)" > $OUT/FERTIG_zellgewicht
