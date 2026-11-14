#!/bin/bash
# Lochkosten im Wurm (2026-11-10): 8 Prozesse mit nice 0 auf dem i9 (neben den 6 G(tau)-Läufen), je 8 h.
cd /home/detlef/Nextcloud/SCHULE/gutzwille_chatGPT/paartransfer_analyse/bosonen_odlro
export OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
PY=/home/detlef/anaconda3/envs/NetKet/bin/python
for seed in 1 2 3 4; do
  $PY scan_leer.py 32 64 --rho 0.0625 --mu-von ergebnisse/bos_L32_b64_r0.0625_s1.json --h 4 6 8 --stunden 8 --seed $seed \
      > ergebnisse/leer_L32_r0.0625_s$seed.log 2>&1 &
  $PY scan_leer.py 32 64 --rho 0.125 --mu-von ergebnisse/bos_L32_b64_r0.125_s1.json --h 3 4 6 --stunden 8 --seed $seed \
      > ergebnisse/leer_L32_r0.125_s$seed.log 2>&1 &
done
wait
date > ergebnisse/leer.done
