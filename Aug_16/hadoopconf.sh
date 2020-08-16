#!/usr/bin/bash

ssh-keygen -b 4096

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

wget 
tar -xzf
mv * /usr/local/hadoop/ 

echo "PATH=/usr/local/hadoop/bin:/usr/local/hadoop/sbin:$PATH" >> /home/$user/.profile
