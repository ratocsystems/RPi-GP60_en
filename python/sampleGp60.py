#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   RPi-GP60 sample program
#   "sampleGp60.py"
#   2018/12/07 R1.0
#   2020/03/24 R1.1 Explicitly specify RTS = False as the initial value
#   2021/08/26 R1.2 English translation
#   RATOC Systems, Inc. Osaka, Japan
#

import sys
import os
import time
import argparse
import math
import RPi.GPIO as GPIO # for GPIO control
import serial
import serial.rs485

# Global variables
port0 = "/dev/ttySC0"   # Device name of Port0
baud0 = 9600            # default baud rate 9600
port1 = "/dev/ttySC1"   # Device name of Port1
baud1 = 9600

# RPi-GP60 initialization
def init_GP60():
    GPIO.setmode(GPIO.BCM)                                # Use Broadcom pin numbering
    GPIO.setup(27,   GPIO.OUT, initial=GPIO.HIGH )        # Turn on isolated power supply of RPi-GP60
    time.sleep(0.5)                                       # Waiting for power supply stabilization

# Change serial setting information
# See 'pyserial' for details on each parameter
# https://pythonhosted.org/pyserial/pyserial_api.html#serial.Serial
def input_param( ser ):
    print( "Input setting parameters. enter:No change >" )
    i=input(" baudrate(300,1200,2400,4800,9600,14400,19200,38400,57600,115200,230400,460800,921600) = ")
    if( len(i) ):
        ser.baudrate = int(i)         # Change baud rate [bps] setting
    i=input(" bytesize(5, 6, 7, 8) = ")
    if( len(i) ):
        ser.bytesize = int(i)         # Change byte length [bit] setting
    i=input(" parity('N','E','O','S','M') = ")
    if( len(i) ):
        ser.parity = i                # Change parity [None, Odd, Even, Space, Mark] setting
    i=input(" stopbits(1, 1.5, 2) = ")
    if( len(i) ):
        ser.stopbits = float(i)       # Change stop bit length [bit] setting
    i=input(" timeout = ")
    if( len(i) ):
        ser.timeout = float(i)        # Change time out [sec] setting
    i=input(" xonxoff(False, True) = ")
    if( len(i) ):
        ser.xonoff = i                # Change Xon/Xoff control setting
    i=input(" rtscts(False, True) = ")
    if( len(i) ):
        ser.rtscts = i                # Change RTS/CTS control setting
    i=input(" dsrdtr(False, True) = ")
    if( len(i) ):
        ser.dsrdtr = i                # Change DSR/DTR control setting


# Main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                prog='sampleGp60.py',          # Program file name
                usage='Sample program for RPi-GP60', # Usage
                description='No arguments',
                epilog=     '--------------------------------------------------------------------------',
                add_help=True,
                )

    try:
        # RPi-GP60 initialization
        init_GP60()

        print( "Sample program for RPi-GP60" )
        key = 1

        s0 = serial.Serial() # Port0
        s0.port = port0
        s0.timeout = 0.5
        s1 = serial.Serial() # Port1
        s1.port = port1
        s1.timeout = 0.5

        s0.rtscts=False
        s0.dsrdtr=False
        s0.rts=False
        s0.dtr=False
        s1.rtscts=False
        s1.dsrdtr=False
        s1.rts=False
        s1.dtr=False

        while( key != 0 ):
            i = input( "1: Send / Receive test (RS232 / RS422 full duplex) \n2: Send / receive test (RS485 half duplex) \n3: Setting \n0: Quit\n > " )
            if( len(i) == 0 ):      # If it is only Enter,
                continue            # redisplay menu.
            key = int(i,10)
            if( key == 0 ):         # If it is '0',
                break               # finish program.

            # Send / Receive test
            if( (key == 1)or(key == 2) ):         # If it is '1' or  '2', Send / Receive test
                # [Setting for RS232 or RS422 full duplex mode]
                # Set the jumper on the board to [RS232] or 
                # [RS-422 full duplex with terminating resistors on both ends of reception ON].

                # [Setting for RS485 mode]
                # Set the jumper on the board to [RS-485 half-duplex with terminating resistors on both ends turned on].

                stx = input( "Port number for sending(0, 1) enter: Back to menu > " ) # Port number for sending
                if( len(stx)==0 ):                                  # if it is only Enter, back to menu
                    continue
                srx = input( "Port number for receiving(0, 1) enter: Back to menu > " ) # Port number for receiving
                if( len(srx)==0 ):                                  # if it is only Enter, back to menu
                    continue
                s0.open() # Open Port0
                s1.open() # Open Port1

                if( key == 1 ):   # If it is '1', Full duplex setting
                    # RS422 mode of RPi-GP60 uses RTS signal for TXDEN. Full duplex, it always set RTS to False state.
                    if(s0.rtscts==False):
                        s0.rts=False
                    if(s1.rtscts==False):
                        s1.rts=False

                if( key == 2 ):   # If it is '2', RS485 mode setting
                    # For RPi-GP60, the RTS setting is (rts_level_for_tx = False, rts_level_for_rx = True).
                    # Even if the loopback is (loopback = False), the sendd data will be echoed back when it is half-duplex mode.
                    # Since the RS485 driver of RPi-GP60 is controlled natively by hardware, set (delay_before_tx = None, delay_before_rx = None).
                    s0.rs485_mode = serial.rs485.RS485Settings(rts_level_for_tx=False, rts_level_for_rx=True, loopback=False,
                                                               delay_before_tx=None, delay_before_rx=None)
                    s1.rs485_mode = serial.rs485.RS485Settings(rts_level_for_tx=False, rts_level_for_rx=True, loopback=False,
                                                               delay_before_tx=None, delay_before_rx=None)

                while( 1 ):     # Repeats sending the keyed character string and displaying the character string in the receive buffer
                    txd = input( "Input data for sending. enter: Back to menu > " )   # Enter the send string
                    if( len(txd)==0 ):                              # If it is only Enter, back to menu
                        if( key == 2 ):   # If is is '2', unset RS485 mode
                            s0.rs485_mode = None    # Unset RS485 mode for Port0
                            s1.rs485_mode = None    # Unset RS485 mode for Port1
                        s0.close()        # Close Port0
                        s1.close()        # Close Port1
                        break
                    if( stx=='0' ):       # Send
                        s0.write( txd.encode('utf-8')+b'\n' )       # For Port0 - Send serial data that converted byte string from 1-line character string
                    else:
                        s1.write( txd.encode('utf-8')+b'\n' )       # For Port1 - Send serial data that converted byte string from 1-line character string
                    while( 1 ):           # Receive
                        if( srx=='0' ):
                            line = s0.readline()    # For Port0 - Receive serial data of 1-line character string
                        else:
                            line = s1.readline()    # For Port1 - Receive serial data of 1-line character string
                        if( len(line)==0 ):         # Until the data is empty, repeat receiving data.
                            break
                        print( "Received data: "+line.decode('utf-8') )    # Convert to the character string from received data, and display the string.

            # Setting
            if( key == 3 ):         # If it is '3', change serial setting
                print( "[Current settings for Port0]" )
                print( s0 )         # Display current settings for Port0
                input_param( s0 )   # Inpu new settings for Port0

                print( "[Current settings for Port1]" )
                print( s1 )         # Display current settings for Port1
                input_param( s1 )   # Input new settings for Port1

        print( "Quit sample program" )

    except KeyboardInterrupt:       # If press the CTRL-C,
         print( "Stopped" )    # Stop
#    except Exception:               # If it occurs othe exceptions,
         print( "Error" )          # Error
    GPIO.output(27, False)          # Turn off isolated power supply of RPi-GP60
    GPIO.cleanup()
    sys.exit()
