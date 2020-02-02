#!/bin/sh

echo Installing EasySSH
rm -rf ~/.easyssh
mkdir ~/.easyssh
cp ./client.py ~/.easyssh/client.py
cp ./addressList.csv ~/.easyssh/addressList.csv
alias easyssh="python3 ~/.easyssh/client.py"
source /etc/bashrc
#rm ../easyssh
echo Install complete!
