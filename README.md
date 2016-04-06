# USB-RFID
Using FTDI drivers to input serial data from RFID readers to the linux machine. 

Link to FTDI drivers: http://www.ftdichip.com/Drivers/VCP.htm

Serial port can be seen in /dev directory. 

For Macs: By running "ls /dev/ | grep cu", you can get the serial port of the RFID.
For Raspberry Pi: The Serial port is usually "TTYUSB0"
