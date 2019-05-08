#!/bin/bash
#   crop all pdf with `_pad` note

filelist=`ls -1 | grep _pad`
filelist=(${filelist// /,})
num=${#filelist[*]}
for ((i=0; i<$num; i++)) do
{
    pdfcrop ${filelist[i]} ${filelist[i]//_pad/}
} done
