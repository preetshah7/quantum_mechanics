#!/bin/sh
for dir in */; do
  cd $dir
  echo $dir

  E=$(grep TOTEN OUTCAR|tail -1)

  #E1=`echo ${E##* }`
  #remove everything except the value
  E1=`echo $E|cut -d ' ' -f5`

  cd ../
  echo ${dir/\//} $E1 | awk '{ print substr( $0, 5) }' >> cutoff.dat
done
