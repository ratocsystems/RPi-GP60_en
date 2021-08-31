# Raspberry Pi OS settings

This section describes the settings of Raspberry Pi OS (Rasbian), which is the OS for Raspberry Pi.
Raspberry Pi is described as 'Raspberry Pi3 ModelB', 
Raspberry Pi Imager is 'Raspberry Pi Imager 1.6.2',
Raspberry Pi OS is 'Raspberry Pi OS Version 2021-03-04)'.
* In May 2020, the name was changed from "Rasbian" to "Raspberry Pi OS".

## Raspberry Pi OS installation
<a name="osInstallation"></a>

### 1. Prepare a Class 10 microSD (8 to 32G)

*For SD cards of 64GB or more, it will be formatted with exFAT.
Raspbian does not support exFAT, so you need to format it with FAT16 or FAT32 using another tool.*

### 2. Download and install the Raspberry Pi Imager from the [Raspberry Foundation official homepage](https://raspberrypi.org/software/).


2-1. Double-click the downloaded file

![01](/install/img/imager-00.png)  

2-2. Click [Install] button

![02](/install/img/imager-01.png)  

2-3. It appears the below screen, click [Finish] button.

![03](/install/img/imager-02.png)  

### 3. Create the SD card for Raspberry Pi OS using Raspberry Pi Imager

3-1. When Raspberry Pi Imager starts, it appears the following screen

   ![01](/install/img/osInstall-01.png)  


3-2. Click [CHOOSE OS] button and select [Raspberry Pi OS (32-bit)].

   ![02](/install/img/osInstall-02.png) 

3-3. Click [CHOOSE SD CARD] button and select the device (SD Card) to write to.

  ![03](/install/img/osInstall-03.png) 

3-4. Click [WRITE] button.

  ![04](/install/img/osInstall-04.png) 

3-5. Select [YES] on the confirmation dialog to start writing to the SD Card.

  ![05](/install/img/osInstall-05.png) 

3-6. The progress of writing is displayed.

  ![06](/install/img/osInstall-07.png) 

3-7. When writing is completed, it appears the following completion screen.
Click [CONTINUE] button, then remove the microSD card.

  ![07](/install/img/osInstall-08.png) 

### 4. Boot Raspberry Pi OS and I2C enable setting

4-1. Connect the microSD card to the Raspberry Pi board and boot.

  ![08](/install/img/osInstall-09.png) 

4-2. Click [Preferense]-[Raspberry Pi Configuration].

  ![09](/install/img/i2cSetting-01.jpg) 

<a name="i2cEnableSetting"></a>
4-3. Click [Interface], then set to "enable" for the I2C

  ![10](/install/img/i2cSetting-02.jpg)  

Restart the OS for the settings to take effect, Then the Raspberry Pi OS installation and settings are complete.

