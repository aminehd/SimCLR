#!/bin/bash
apt install pv
trap "exit" INT

scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")
destination=$(cd "$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")";cd ..; pwd)/$(basename "$1")/


python -c "print('*' * 30)"
echo "copying test.tar ..."
cp $scriptDir/test.tar  $destination/test.tar

python -c "print('*' * 30)"
echo "copying train.tar ..."
cp $scriptDir/train.tar  $destination/train.tar

python -c "print('*' * 30)"
echo "coping validation.tar ..."
cp $scriptDir/validation.tar  $destination/validation.tar

python -c "print('*' * 70)"
python -c "print('*' * 70)"
echo "done copying"


rm -rf $destination/test
rm -rf $destination/train
rm -rf $destination/validation

python $scriptDir/untar.py "$destination" test
python $scriptDir/untar.py "$destination" train
python $scriptDir/untar.py "$destination" validation

python -c "print('*' * 70)"
python -c "print('*' * 70)"
echo ""
echo "All Done."