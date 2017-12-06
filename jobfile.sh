
NPRODS=100
NCPUS=6
sys=wt_ssrna_atp_1
prod=1
for ((i=1;i<=10;i++))
do
	j=1
	while ((j <= $NCPUS)) && ((prod <= $NPRODS))
	do
		echo $j $i $prod
		((b=$prod+4))
		printf -v x "%03d" $prod
		printf -v y "%03d" $b
		mkdir $x.$y.COM_Distance
		cd $x.$y.COM_Distance
		sed -e s/AAA/$prod/g -e s/BBB/$b/g -e s/XXX/$x/g -e s/YYY/$y/g -e s/system_descriptor/$sys/g < ../sample.config > $x.$y.res_res_com_distance.config
		time ../res_res_com_distance.calc.py $x.$y.res_res_com_distance.config > res_res_com_distance.output &
		cd ../
		((j=$j+1))
		((prod=$prod+5))
	done
	wait
done

