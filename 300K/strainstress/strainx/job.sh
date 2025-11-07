#!/bin/bash
#SBATCH -A chem
#SBATCH -p burst
#SBATCH -N 1
#SBATCH --ntasks-per-node 36
#SBATCH -c 1
#SBATCH -J MoSe2_x
#SBATCH --mem=0
#SBATCH -t 48:00:00
#SBATCH -o ./output.txt
#SBATCH -e ./test-error.txt


cd $SLURM_SUBMIT_DIR

date

module load gcc
module load fftw

pwd

srun -n36 -c1 /home/gywjedi90/lammps_2023-12-15/build_2025-03-27/lmp_cades -in in.stress > out.txt &

wait
