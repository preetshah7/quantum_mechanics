#!/bin/sh
for dir in */; do
cd $dir
echo $dir

K=$(grep TOTEN OUTCAR|tail -1)

#E1=`echo ${E##* }`
#remove everything except the value
K1=`echo $K|cut -d ' ' -f5`

#ZPE="grep zero_point_energy: thermal properties.yanllawk '{print $2]** 9
#ZPE = grep 'zero_point_energy: thermal properties.yanl

cd ../
echo ${dir/\//} $K1 | awk '{ print substr( $0, 5) }' >> K.dat
done
