#!/bin/sh

l_0=4.20448400
echo $l_0
for dir in */; do
cd $dir
echo $dir

l=`echo ${dir/\//} | awk '{ print substr( $0, 5) }'`
echo $l
K=$(grep TOTEN OUTCAR|tail -1)
sum=`echo "scale=2;$l-$l_0" | bc`
strain=`echo "scale=2;$sum/$l_0" | bc`

echo $strain
#E1=`echo ${E##* }`
#remove everything except the value
K1=`echo $K|cut -d ' ' -f5`

#ZPE="grep zero_point_energy: thermal properties.yanllawk '{print $2]** 9
#ZPE = grep 'zero_point_energy: thermal properties.yanl

cd ../
echo $strain $K1 >> strain.dat
done
