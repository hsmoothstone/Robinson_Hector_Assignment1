#!/bin/bash
echo "Enter word to find."
read findd
echo "Enter word to replace."
read replace
mkdir -p replace/

#use grep to find all .txt files that have 'find' in them
grep -l "$findd" ./*.txt | xargs cp -t replace/
#files then copied into new directory

#use sed to find 'find' and replace with 'replace' in all files that were copied into new directory
sed -i -e s/"$findd"/"$replace"/g ./replace/*.txt
