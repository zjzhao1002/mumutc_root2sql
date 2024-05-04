#!/bin/bash

process=$1

ROOTFILE=${process}.root

mkdir -p ${process}
cp main.py treeReader.py table.sql ${ROOTFILE} ${process}
cd ${process}

sed -i'' -e "s/PROCESS/${process}/g" main.py
sed -i'' -e "s/PROCESS/${process}/g" table.sql

python3 main.py
