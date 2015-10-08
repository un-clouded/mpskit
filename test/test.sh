#!/bin/sh
set -e
set -x 
echo 'RUNNING..'
cp EXO.HAG EX.HAG

mpskit hag unpack EX.HAG

mpskit mdat unpack EX.HAG.dir/MESSAGES.DAT
mpskit mdat pack EX.HAG.dir/MESSAGES.DAT
mpskit mdat unpack EX.HAG.dir/MESSAGES.DAT

mpskit ss unpack EX.HAG.dir/RM901C1.SS
mpskit ss pack EX.HAG.dir/RM901C1.SS
mpskit ss unpack EX.HAG.dir/RM901C1.SS

mpskit ss unpack EX.HAG.dir/RM505A8.SS
mpskit ss pack EX.HAG.dir/RM505A8.SS
mpskit ss unpack EX.HAG.dir/RM505A8.SS

mpskit ff unpack EX.HAG.dir/FONTCONV.FF
mpskit ff pack EX.HAG.dir/FONTCONV.FF
mpskit ff unpack EX.HAG.dir/FONTCONV.FF

mpskit aa unpack EX.HAG.dir/RM967A.AA
mpskit aa pack EX.HAG.dir/RM967A.AA
mpskit aa unpack EX.HAG.dir/RM967A.AA

mpskit aa unpack EX.HAG.dir/I0.AA
mpskit aa pack EX.HAG.dir/I0.AA
mpskit aa unpack EX.HAG.dir/I0.AA

mpskit cnv unpack EX.HAG.dir/CONV000.CNV
mpskit cnv pack EX.HAG.dir/CONV000.CNV
mpskit cnv unpack EX.HAG.dir/CONV000.CNV

mpskit rdat unpack EX.HAG.dir/VOCAB.DAT
mpskit rdat pack EX.HAG.dir/VOCAB.DAT
mpskit rdat unpack EX.HAG.dir/VOCAB.DAT

mpskit hag pack EX.HAG
mpskit hag unpack EX.HAG
echo 'CLEANING..'
rm EX.HAG.dir -r
rm EX.HAG.lst
rm EX.HAG
echo 'OK'



