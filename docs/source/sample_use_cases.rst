:orphan:


.. _sample_use_cases:

****************
Sample Use Cases
****************




.. panels::

    **Putting and Getting A Key-Value Pair**

    * The following will showcase how to a put key-value pair onto the network as a simple test to ensure the functionality of the *VIN™*. 
    * To put a key-value onto the network, in the *VIN™ CLI* session run ``put <key> <value>``; where ``<key>`` and ``<value>`` can be any string that does not contain spaces. For this example ``test_key`` was used for the ``<key>`` and ``test_value`` for the ``<value>``. The following figure displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the peer.
    * To view the shard that was placed on the *Kademlia* network, navigate to ``/opt/VIN/kademlia/data/`` and proceed through the folder structure until reaching the file.
    * To get a value from the network, in the *VIN™ CLI* session run ``get <key>``; where ``<key>`` is ``test_key`` for this example. The following figure displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the peer.

    ---
    

    **VIN_CLI Output**

    .. code-block:: rst
        
        VIN@127.0.0.1:7070> put key value
        Sending payload:
        {"key":"key","value":"value"}

        Waiting for response...
        Status : 200
        Reason : 'putValue' successful:  Key: key ; Value: value
        Response received

        [key]:value   put successfully

    **VIN Node Response**

    .. code-block:: powershell

        14:47:49:680 http: URI: /putValue ; request from: 127.0.0.1:38936
        14:47:49:680 http: 'putValue' request received
        14:47:49:680 http: 'putValue' successful:  Key: key ; Value: value
        14:47:49:680 benc: 'putValue' request latency 0 min 0 sec 0 msec



.. panels::

    

    * The following will showcase how to a put key-value pair onto the network as a simple test to ensure the functionality of the *VIN™*. 
 

    ---
    

    **VIN_CLI Output**

    .. code:: none

        VIN@127.0.0.1:7070> put key value
        Sending payload:
        {"key":"key","value":"value"}

        Waiting for response...
        Status : 200
        Reason : 'putValue' successful:  Key: key ; Value: value
        Response received

        [key]:value   put successfully


Introduction
============

Provided with the *VIN™* installation package is a number of scripts that can be easily executed to showcase the functionality of the *VIN™*. Be sure to shut down any current instances of the *VIN™* before running each script.


Sample Scripts
==============


Setting Up a Network
====================


Sharing a File
==============


Put
---


Spread
------


Share
-----


Gathering a File
================


Get
---


Gather
------


Deleting a Node
===============


Shutting Down a Network
=======================
