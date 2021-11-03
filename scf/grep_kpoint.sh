#!/bin/sh
for dir in */; do
  cd $dir
  echo $dir

  K=$(grep TOTEN OUTCAR|tail -1)

  #E1=`echo ${E##* }`
  #remove everything except the value
  K1=`echo $K|cut -d ' ' -f5`

  cd ../
  echo ${dir/\//} $K1 | awk '{ print substr( $0, 5) }' >> cutoff.dat
done
