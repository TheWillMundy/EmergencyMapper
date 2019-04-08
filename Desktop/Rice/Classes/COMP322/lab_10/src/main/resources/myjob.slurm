#!/bin/bash

#SBATCH --job-name=comp322-lab10
#SBATCH --ntasks=8
#SBATCH --mem=16000m
#SBATCH --time=00:04:00
#SBATCH --mail-user=grs7@rice.edu # TODO: Input your netID
#SBATCH --mail-type=ALL
#SBATCH --export=ALL
#SBATCH --partition=commons
#SBATCH --exclusive

set -e

cd /home/$USER/labs/lab_10 # TODO: Path to your lab 10 folder

source /home/jmg3/comp322/322_setup.sh

mvn clean compile test-compile

CUSTOM_CP="target/classes"
CUSTOM_CP="$CUSTOM_CP:target/test-classes"
CUSTOM_CP="$CUSTOM_CP:$EBROOTOPENMPI/lib/mpi.jar"
CUSTOM_CP="$CUSTOM_CP:/home/$USER/.m2/repository/junit/junit/4.12/junit-4.12.jar"
CUSTOM_CP="$CUSTOM_CP:/home/$USER/.m2/repository/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar"

srun -n 1 java -cp $CUSTOM_CP org.junit.runner.JUnitCore edu.rice.comp322.Lab10PerformanceTest
srun -n 2 java -cp $CUSTOM_CP org.junit.runner.JUnitCore edu.rice.comp322.Lab10PerformanceTest
srun -n 4 java -cp $CUSTOM_CP org.junit.runner.JUnitCore edu.rice.comp322.Lab10PerformanceTest
srun -n 8 java -cp $CUSTOM_CP org.junit.runner.JUnitCore edu.rice.comp322.Lab10PerformanceTest
