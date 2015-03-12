Multiple Tor relays to one machine with many IP addresses
=========================================================

Install multiple Tor relays to one machine with many IP addresses.

---------------------------------------

- Install Tor
- Install Python 2.7

```sh
sudo mkdir -p /usr/local/var/lib/tor{1,2,3,4,5,6,7,8,9,10}
sudo mkdir -p /usr/local/var/lib/tor{11,12,13,14,15,16,17,18,19,20}
sudo mkdir -p /usr/local/var/lib/tor{21,22,23,24,25,26,27}
sudo ip addr flush dev em1
sudo ifup em1:0 em1:1 em1:2 em1:3 em1:4 em1:5 em1:6 em1:7 em1:8 em1:9 em1:10 em1:11 em1:12 em1:13 em1:14 em1:15 em1:16 em1:17 em1:18 em1:19 em1:20 em1:21 em1:22 em1:23 em1:24 em1:25 em1:26
cd /home/juha/tor-research
python generate_torrcs.py
sudo cp torrc* /usr/local/etc/
sudo bash firewall.sh
sudo bash start_tor.sh
sudo killall tor
```
