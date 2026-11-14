#!/bin/bash
# Nachtlauf zeitschleife2d.py (2026-11-10/11): fester Gitter-Zustand (6×4, N = 6, ρ = 1/4), wachsende Teilchenzahl je Zelle
# m = 1 (Zellen 2×2), 1,5 (3×2), 3 (6×2); Varianten: a (festzelle+Querschritt, locker), festzelle locker ohne
# Pflicht-Querschritt, freier Spiegel, alter Zell-Abweg; Fensterlängen w = 1..4. Messgröße: ∫f²dµ = |ν|·E[f | angenommen].
# Aufruf: bash zs2d_nacht.sh <Parallelität> <Stunden je Lauf>
cd "$(dirname "$0")"
P=${1:-13}
STD=${2:-1.75}
OUT=ergebnisse/zs2d_nacht
mkdir -p $OUT
jobs=()
systeme=(
  "m1|--Lx 6 --Ly 4 --N 6 --cx 2 --cy 2"
  "m1.5|--Lx 6 --Ly 4 --N 6 --cx 3 --cy 2"
  "m3|--Lx 6 --Ly 4 --N 6 --cx 6 --cy 2"
)
varianten=(
  "a|--abweg festzelle --querschritt --locker"
  "festl|--abweg festzelle --locker"
  "frei|--abweg frei --locker"
  "zelle|--abweg zelle"
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
echo "Nachtlauf fertig: $(date)" > $OUT/FERTIG
