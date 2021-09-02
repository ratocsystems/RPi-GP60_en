# Python sample file for RPi-GP60

This section describes how to use the Python sample file for RPi-GP60.
Raspberry Pi is explained in'Raspberry Pi3 ModelB', and OS is explained in'Raspberry Pi OS Version 2021-03-04'.
The sample file is `sampleGp60.py`.


***
## Preparation  
### Connect RPi-GP60 to Raspberry Pi
Please make the following preparations.
- [Raspberry Pi OS installation](../install/README.md#Raspberry_Pi_OS_installation)  
- [GPIO40pin I2C settings](../install/README.md#i2cEnableSetting)  
- [Connect'RPi-GP60' to 'Raspberry Pi'](../setup/README.md#settingAndInstalletionRPi0GP60)  
- [Serial driver settings](../setup/README.md#serialDriverSettings)  

### Create a directory to run the Python sample files
1. Use the'mkdir' command to create a directory named'RPi-GP60'. (The directory name and creation location are free)
    ```
    $ mkdir RPi-GP60  
    ```

1. Execute the'ls' command and confirm that the'RPi-GP60' directory has been created.
    ```
    $ ls  
    ```

1. Use the'cd'command to change to the'RPi-GP60' directory.
    ```
    $ cd RPi-GP60  
    ```  
    
### Download Python sample files from GitHub
Download the Python sample file from GitHub.
1. Download sampleGp60.py
    ```
    $ wget https://github.com/ratocsystems/rpi-gp60_en/raw/master-en/python/sampleGp60.py
    ```  

1. Run the `ls` command to verify that the Python sample file` sampleGp60.py` has been downloaded.
    ```
    $ ls  
    sampleGp60.py  
    ```
  
***
## About Python sample files
  
`sampleGp60.py`  

This is a Python sample program that sends and receives serial datas using RPi-GP60.
The sample program performs the following processing.

1. **Initial setting of RPi-GP60 init_GP60 ()**  
    Make initial settings for GPIO.
    ※<u>This setting depends on the hardware, so do not change it.</u>  
    - Set GPIO to be specified by GPIO number
    - Set the power supply for the isolation circuit to ON   
        After turning on the power, wait until it stabilizes.

1. **Change serial setting information input_param(serial)**  
    Change the serial setting parameter of [pyserial module](https://pythonhosted.org/pyserial/pyserial_api.html#serial.Serial) to the input value.
    The following parameters can be specified. If you do not want to change it, enter only enter.
    --Baud rate [bps]
    --Byte length [bit]
    --Parity [None, odd, even, space, mark]
    --Stop bit length [bit]
    --Reception timeout time [sec]
    --Flow control XON / XOFF setting [False / True]
    --Flow control RTS / CTS setting [False / True]
    --Flow control DSR / DTR setting [False / True] 

1. **Menu display**  
    Display the following menu.

    1: Send / Receive test (RS232 / RS422 full duplex) 
    2: Send / receive test (RS485 half duplex) 
    3: Setting 
    0: Quit
    \>
  
1. **Send / receive test**  
    If 1 or 2 is entered in the menu, it runs a serial send / receive test.
    Enter the sending port number and receiving port number (0,1). Just enter return to the menu.
    `Port number for sending(0, 1), enter: Back to menu >`
    `Port number for receiving(0, 1), enter: Back to menu >`
    If 2 is entered in the menu, it enables RS485 full-duplex mode operation (automatic enable control of differential drivers).
    `Input data for sending, enter: Back to menu >`
    Enter the character string to be sent. The received character string is displayed after sending.
    Receiving continues until the configured timeout occurs.
    After the timeout, it returns to the transmission data input.
    When entering the transmission data, just enter return to the menu.

1. **Settings**  
    If 3 is entered in the menu, change the serial setting.
    Perform input_param() to change the serial setting information for port 0 and port 1.
  
1. **Finish**  
    If 0 is entered in the menu, terminate this program.

***
## How to use Python sample files
Execute `python3` with the sample file name 'sampleGp60.py'.
- **Serial transmission / receive test**    
    `Example) When performing a return transmission / reception test from port 0 to port 1 at a baud rate of 115200 bps`
    ~~~
    $ python3 sampleGp60.py
    sampleGp60.py:30: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(27,   GPIO.OUT, initial=GPIO.HIGH )        # Turn on isolated power supply of RPi-GP60
    Sample program for RPi-GP60
    1: Send / Receive test (RS232 / RS422 full duplex) 
    2: Send / receive test (RS485 half duplex) 
    3: Setting 
    0: Finish
     > 3
    [Current settings for Port0]
    Serial<id=0x769c0d10, open=False>(port='/dev/ttySC0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.5, xonxoff=False, rtscts=False, dsrdtr=False)
    Input setting parameters. enter:No change >
     baudrate(300,1200,2400,4800,9600,14400,19200,38400,57600,115200,230400,460800,921600) = 
     bytesize(5, 6, 7, 8) = 
     parity('N','E','O','S','M') = 
     stopbits(1, 1.5, 2) = 
     timeout = 
     xonxoff(False, True) = 
     rtscts(False, True) = 
     dsrdtr(False, True) = 
    [Current settings for Port1]
    Serial<id=0x769c0c30, open=False>(port='/dev/ttySC1', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.5, xonxoff=False, rtscts=False, dsrdtr=False)
    Input setting parameters. enter:No change >
     baudrate(300,1200,2400,4800,9600,14400,19200,38400,57600,115200,230400,460800,921600) = 
     bytesize(5, 6, 7, 8) = 
     parity('N','E','O','S','M') = 
     stopbits(1, 1.5, 2) = 
     timeout = 
     xonxoff(False, True) = 
     rtscts(False, True) = 
     dsrdtr(False, True) = 
    1: Send / Receive test (RS232 / RS422 full duplex) 
    2: Send / receive test (RS485 half duplex) 
    3: Setting 
    0: Finish
     > 1
    Port number for sending(0, 1) enter: Back to menu > 0
    Port number for receiving(0, 1) enter: Back to menu > 1
    Input data for sendig. enter: Back to menu > ABCD
    Received data: ABCD

    Input data for sendig. enter: Back to menu > EFGH
    Received data: EFGH

    Input data for sendig. enter: Back to menu > UUUU
    Received data: UUUU

    Input data for sendig. enter: Back to menu > 
    1: Send / Receive test (RS232 / RS422 full duplex) 
    2: Send / receive test (RS485 half duplex) 
    3: Setting 
    0: Finish

    ~~~