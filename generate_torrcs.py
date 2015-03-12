"""Generate multiple torrc files."""
# -*- coding: utf-8 -*-
import codecs  # UTF-8 support for the text files

def text2file(txt, filename):
    """Write the txt to the file."""
    outputfile = codecs.open(filename, "w", "utf-8")
    outputfile.write(txt)
    outputfile.close()

f = open('relay_names.txt')
lines = f.readlines()
f.close()
lines = [line.replace('\n', '') for line in lines]
family = ",".join(lines)

if len(lines) > 30:
    print "ERROR: this script is not designed to open more than 30 ports."

ports = []
for index, relay in enumerate(lines):
    i = index + 1
    SocksPort = 9070 + i
    if SocksPort in ports:
        print "ERROR: %d in ports" % SocksPort
    ports.append(SocksPort)
    txt = "Address 193.166.167." + str(67+i) + "\n"
    txt = txt + "SocksPort " + str(SocksPort) + "\n"
    txt = txt + "Log notice file /usr/local/var/log/tor/notices" + str(i) + ".log\n"
    txt = txt + "RunAsDaemon 1\n"
    txt = txt + "DataDirectory /usr/local/var/lib/tor" + str(i) + "\n"
    ORPort = 9000+i
    if ORPort in ports:
        print "ERROR: %d in ports" % ORPort
    ports.append(ORPort)
    txt = txt + "ORPort 193.166.167." + str(67+i) + ":" + str(ORPort) + "\n"
    txt = txt + "Nickname " + relay + "\n"
    txt = txt + "ContactInfo juha.nurmi(att)tut.fi\n"
    DirPort = 9030 + i
    if DirPort in ports:
        print "ERROR: %d in ports" % DirPort
    ports.append(DirPort)
    txt = txt + "DirPort 193.166.167." + str(67+i)  + ":" + str(DirPort) + "\n"
    txt = txt + "ExitPolicy reject *:*\n"
    txt = txt + "AvoidDiskWrites 1\n"
    txt = txt + "MaxMemInQueues " + str(512) + " MB\n"
    txt = txt + "RelayBandwidthRate 300 KBytes\n"
    txt = txt + "HiddenServiceStatistics 1\n"
    txt = txt + "MyFamily " + family + "\n" 
    text2file(txt, "torrc"+str(i))

ports = sorted(ports)
print "Required ports: %s" % ", ".join(str(x) for x in ports) 
