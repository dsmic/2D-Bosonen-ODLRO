#!/bin/bash
# Lücken-Green-Funktion G(tau) bei k = 0 (2026-11-10), kanonischer Wurm, 6 Prozesse mit nice 0 auf dem i9.
# Startet erst, wenn Runde 1 fertig ist (ergebnisse/runde1.done), und übernimmt deren 6 Kerne; je 12 h.
cd /home/detlef/Nextcloud/SCHULE/gutzwille_chatGPT/paartransfer_analyse/bosonen_odlro
while [ ! -f ergebnisse/runde1.done ]; do sleep 60; done
sleep 30
export OMP_NUM_THREADS=1 NUMBA_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
PY=/home/detlef/anaconda3/envs/NetKet/bin/python
for spec in "16 32 0.0625 1" "16 32 0.125 1" "32 64 0.0625 1" "32 64 0.0625 2" "32 64 0.125 1" "32 64 0.125 2"; do
  set -- $spec
  $PY scan_gtau.py $1 $2 --rho $3 --mu-von ergebnisse/bos_L$1_b$2_r$3_s1.json --stunden 12 --seed $4 \
      > ergebnisse/gtau_L$1_b$2_r$3_s$4.log 2>&1 &
done
wait
date > ergebnisse/gtau.done
