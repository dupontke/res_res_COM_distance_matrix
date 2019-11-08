#!/bin/bash
#SBATCH --job-name=dist_cal.wt_ssrna_atp_1
#SBATCH --output=dist_cal.wt_ssrna_atp_1.output
#SBATCH --time=96:00:00 
#SBATCH --nodes=1
#SBATCH --exclusive

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/gcc-4.9.2/lib64"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/hpcx-v1.2.0-292-gcc-MLNX_OFED_LINUX-2.4-1.0.0-redhat6.6/ompi-mellanox-v1.8/lib"

export PYTHON_EGG_CACHE="./"

NPRODS=100
NCPUS=20
sys=wt_ssrna_atp_1
prod=1
for ((i=1;i<=2;i++))
do
    j=1
    while ((j <= $NCPUS)) && ((prod <= $NPRODS))
    do
	echo $j $i $prod
	((a=$prod+4))
	printf -v x "%03d" $prod
	printf -v y "%03d" $a
	mkdir $x.$y.COM_distance
	cd $x.$y.COM_distance
	sed -e s/AAA/$prod/g -e s/BBB/$a/g -e s/XXX/$x/g -e s/YYY/$y/g -e s/system_descriptor/$sys/g < ../sample.config > $x.$y.res_res_com_distance.config
	time /mnt/lustre_fs/users/mjmcc/apps/python2.7/bin/python ../res_res_com_distance.calc.py $x.$y.res_res_com_distance.config > res_res_com_dist_calc.output & 
	cd ../
	((j=$j+1))
	((prod=$prod+5))
	done
    wait
done