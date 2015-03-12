#!/bin/bash

for port in {9000..9100}
do
    sudo iptables -I INPUT -p tcp --dport $port -m state --state NEW -s 0.0.0.0/0 -j ACCEPT
done
