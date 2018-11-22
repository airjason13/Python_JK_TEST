
from scapy.all import *
import sys, getopt

def show_pkt_payload(pkt):
    #print "show_pkt_payload"
    try:
        if pkt[Raw]:
            #print "get packet"
            hexdump(pkt[Raw])
    except:
        #print "No Raw Load"

def start_sniff_runtime(dev):
    ###dpkt = sniff(iface = dev, prn=lambda x:x.show())
    dpkt = sniff(iface = dev, prn=show_pkt_payload, filter='tcp')

def start_sniff_to_file(dev, c):
    print "c =" , c
    dpkt = sniff(iface = dev, count = c)
    wrpcap("demo.pcap", dpkt)
    #dpkt.show()


def main(argv):
    sniff_dev = ''
    sniff_count = 0
    try:
        opts, args = getopt.getopt(argv,"hi:c:",["device=", "count="])
    except getopt.GetoptError:
        print "scapt-listener.py -i device -c count"
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print "scapt-listener.py -i device -c count"
            sys.exit(0)
        elif opt in ("-i", "--device"):
            sniff_dev = arg
        elif opt in("-c", "--count"):
            sniff_count = arg


    print "sniff device :", sniff_dev
    print "sniff_count :", sniff_count
    if 0 == int(sniff_count):
        start_sniff_runtime(sniff_dev)
    else:
        start_sniff_to_file(sniff_dev, int(sniff_count))


if __name__ == "__main__":
    main(sys.argv[1:])