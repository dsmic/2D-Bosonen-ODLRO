#!/bin/bash
# Phase 1, Runde 1 (2026-11-09): harte Bosonen, Wurm, 6 Prozesse mit nice 0 auf dem i9 (neben den Stufe-A-Läufen
# mit nice 10), je 16 h, beta = 2 L. Dichten 1/16, 1/8 (L = 16, 32), 1/4, 1/2 (L = 32).
cd /home/detlef/Nextcloud/SCHULE/gutzwille_chatGPT/paartransfer_analyse/bosonen_odlro
export OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
PY=/home/detlef/anaconda3/envs/NetKet/bin/python
for spec in "16 32 0.0625" "32 64 0.0625" "16 32 0.125" "32 64 0.125" "32 64 0.25" "32 64 0.5"; do
  set -- $spec
  $PY scan_bos.py $1 $2 --rho $3 --stunden 16 --seed 1 > ergebnisse/runde1_L$1_b$2_r$3.log 2>&1 &
done
wait
date > ergebnisse/runde1.done
