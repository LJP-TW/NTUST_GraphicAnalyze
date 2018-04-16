#!/bin/bash

#for i in `seq 1 9`;
#do
#	if [ $i -eq 7 ]
#	then
#		continue
#	fi
#	python imgToPos.py img/complete/$i.png > position/$i.pos
#done

beTransPath="img/complete"
savePath="position"

for file in `ls ./$beTransPath | awk -F '.' '{ print $1 }'`;
do
	fileFullPath="$beTransPath/$file.png"
	saveFullPath="$savePath/$file.pos"
	python imgToPos.py $fileFullPath > $saveFullPath
done


