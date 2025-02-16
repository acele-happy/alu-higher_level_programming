#!/bin/bash

createfiles(){
echo "how many files do you want to create?"
read fileNum
echo "Enter the base name"
read baseName

for((i=1;i<=fileNum;i++))
do
	touch "${baseName}_${i}.txt"
done

echo "files created successfully!"
}

createfiles
