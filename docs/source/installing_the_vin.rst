.. _vin-install:

**************************************
Installing the VIN™
**************************************


Introduction
============

The sections below contain the instructions for installing the *VIN™* for multiple operating systems. After installation, it is recommended the instructions in :ref:`running-the-vin-linux`, or :ref:`running-the-vin-windows`, depending on the operating system in use, be followed to gain an understand on how to interact with the *VIN™*.


Installation
============

Linux (Ubuntu 20.04+)
----------------------
  
* Navigate to the folder containing the ``DEB`` file on the system and run:  

  * ``sudo dpkg -i <deb_name>.deb``, where ``<deb_name>`` is the name of the file (e.g., ``QToken-CPP_1.12.3-x86_64.deb``).

* Note: If installing the *VIN™* on a system with a previous installation, ``dpkg`` may produce errors regarding overwriting files. Make a backup of those files and then run the following command to do the upgrade:

  * ``sudo dpkg -i --force-overwrite <deb_name>.deb``, where ``<deb_name>`` is the name of the file (e.g., ``QToken-CPP_1.12.3-x86_64.deb``).

To ensure the *VIN™* is directed to the required libraries run:

* ``echo "export LD_LIBRARY_PATH=/usr/local/lib:/usr/lib" > ~/.profile``
* ``export LD_LIBRARY_PATH=/usr/local/lib:/usr/lib`` 


Windows
----------

* Navigate to the folder containing the ``VIN.zip`` file on the system
* Run ``tar -xf VIN.zip`` from a CLI session (as an administrator) or double click the file and follow the prompts to extract the contents 
* Navigate to the extracted folder and run ``msiexec /i VIN.msi`` from a CLI session (as an administrator) or double click the file and follow the prompts to install the *VIN™*  
    

Components
----------

* *VIN™ Command Line Interface (CLI)*: the *VIN™ CLI* acts as a Hypertext Transfer Protocol (HTTP) client for reaching the *VIN™* HTTP server from the command line in a *Linux* environment. 
* ``defaults.cfg``: a modifiable configuration file located in the ``/etc/opt/VIN/`` directory for *Linux* and under ``Program Files\Virgil\VIN`` for *Windows*. For more information on the configuration, refer to the :ref:`vin-configuration` section.
  

Disk
====

All *VIN™* Disk IO occurs and is located in ``/opt/VIN`` for *Linux* based operating systems and ``Program Files\Virgil\VIN\`` for *Windows*. Any cryptographic receipts and reconstructed data will be stored here.


Debug Logs
==========

*VIN™* nodes store log outputs in ``/var/log/VIN/logs/`` for *Linux* based operating systems and ``Program Files\Virgil\VIN\logs\`` for *Windows*. If any support from Virgil Systems is required, these logs can be sent along with any support requests to obtain more visibility into the issue.