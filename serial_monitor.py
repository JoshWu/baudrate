#!/usr/bin/env python

import serial
import sys

wait_msg = 'use "tail -f usb2.output | xxd" to read another output \r\n' + \
            '----------------------------------------------------\r\n'

port1 = serial.Serial("/dev/ttyUSB1", baudrate=9600, timeout=0.1)
port2 = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0.1)

fd1 = open("usb1.output", "w");
fd2 = open("usb2.output", "w");

sys.stdout.write(wait_msg)

try:
    while True:
        rcv1 = port1.read(8)
        if rcv1 != '':
            sys.stdout.write(rcv1)
            sys.stdout.flush()
            fd1.write(rcv1)
            fd1.flush()
            port2.write(rcv1)

        rcv2 = port2.read(8)
        if rcv2 != '':
            #sys.stdout.write(rcv2)
            #sys.stdout.flush()
            fd2.write(rcv2)
            fd2.flush()
            port1.write(rcv2)

except KeyboardInterrupt:
    pass

port1.close()
port2.close()
fd1.close()
fd2.close()
