#!/bin/sh

echo Installing EasySSH
mkdir ~/.easyssh
cp ./client.py ~/.easyssh/client.py
cp ./addressList.csv ~/.easyssh/addressList.csv
alias easyssh=python3 ~/.easyssh/client.py
#rm ../easyssh
