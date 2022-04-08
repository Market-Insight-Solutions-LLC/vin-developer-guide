*************
Release Notes
*************

The following are added as an example...


November 22, 2021
=================

This release contains many upgrades to the VIN encryption/decryption and encoding/decoding capabilities...


Features
--------

#. Reed-Solomon Coder...
#. Concurrent Coder...
#. SHA-256 Encryption...


Improvements/Changes
--------------------

* Improvements...


Bugfixes
--------

* Bugfixes...


===========================================

July 14, 2021
=============

This release includes many features and fixes to improve the performance and reliability of the application. 


Features 
--------

#. *Windows* Integration
   
   Allows the application to be built using *Visual Studio 2019*, improving the overall scale and usability of the DTxTM. This allows for a *Windows* Installer package (``MSI``) file to be created and utilized to easily install the application where necessary. 

#. Sharing to Multiple Peers (One to Many) 

   A single node can now share the same data with a single or multiple peers automatically depending on the desired request. 

#. Receipt Streaming 

   Shared files are now split into multiple smaller files and then spread with the resulting receipts sent to the peer. The receiving node handles successive crypto receipts, each receipt is gathered and the shards are appended together. When the connection ends the appended shards are built and saved. 


Improvements/Changes 
--------------------

* Alerts for errors found in data 
* Updated the *Kademlia* library 
* Added in the underlying *LVM*   
* Added in license enforcement 
* Removed *Boost* dependency  
* A node’s status is routinely checked to determine if it’s connected to the bootstrap 
* Added support for ECDH single pass allowing objects to be encrypted using ECC keys with 256 bits of strength. 
* Added ability to sign CMS objects to verity source prior to decrypting 
* Websocket integration 


Bugfixes 
--------

* Share instability (due to timeouts) 
* Share protocol race condition 
* Reactor timeout 
* Many to one bug 
* Application service starts before the network is ready 
* High CPU Core usage during Share operations 
* Receipt server persisting 
* Stream overloads client 
* UUID memory leak 


