#!/bin/bash

for i in {1..27}
do
    echo "Starting $i."
    sudo /home/juha/tor-research/tor_asn/tor/src/or/tor -f /usr/local/etc/torrc$i
    sleep 2
    echo "Started."
done
