#!/bin/bash

#SBATCH --job-name="buried_wats"
#SBATCH --partition=mf_m-c1.9
#SBATCH --output="z_slurmOut.txt"
#SBATCH --error="z_slurmErr.txt"
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2000mb
#SBATCH --time=90:00:00
#SBATCH --distribution=block:cyclic
#--------------

# Informational output
echo "=================================== SLURM JOB ==================================="
echo
echo "The job will be started on the following node(s):"
echo $SLURM_JOB_NODELIST
echo
echo "Slurm User:         $SLURM_JOB_USER"
echo "Run Directory:      $(pwd)"
echo "Job ID:             $SLURM_JOB_ID"
echo "Job Name:           $SLURM_JOB_NAME"
echo "Partition:          $SLURM_JOB_PARTITION"
echo "Number of nodes:    $SLURM_JOB_NUM_NODES"
echo "Number of tasks:    $SLURM_NTASKS"
echo "Submitted From:     $SLURM_SUBMIT_HOST"
echo "Submit directory:   $SLURM_SUBMIT_DIR"
echo "=================================== SLURM JOB ==================================="
echo

export OE_LICENSE="$HOME/oe_license.txt"

cd $SLURM_SUBMIT_DIR
echo 'Working Directory:'
pwd

date

python Buried_Water_Run_Example_scipt.py > buried_wat_logfile.log

date
