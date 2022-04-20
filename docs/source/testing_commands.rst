.. _testing-commands:

*****************
TESTING COMMANDS
*****************

EXAMPLE 1: USING PANELS 
========================================

.. panels::
    :card: none
    :container: container-lg pb-3

    **Putting and Getting A Key-Value Pair**

    * The following will showcase how to a put key-value pair onto the network as a simple test to ensure the functionality of the *VIN™*. 
    * To put a key-value onto the network, in the *VIN™ CLI* session run ``put <key> <value>``; where ``<key>`` and ``<value>`` can be any string that does not contain spaces. For this example ``test_key`` was used for the ``<key>`` and ``test_value`` for the ``<value>``. The following figure displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the peer.
    * To view the shard that was placed on the *Kademlia* network, navigate to ``/opt/VIN/kademlia/data/`` and proceed through the folder structure until reaching the file.
    * To get a value from the network, in the *VIN™ CLI* session run ``get <key>``; where ``<key>`` is ``test_key`` for this example. The following figure displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the peer.

    ---  

    **VIN_CLI Output**

    .. code-block:: none
        
        VIN@127.0.0.1:7070> put key value
        Sending payload:
        {"key":"key","value":"value"}

        Waiting for response...
        Status : 200
        Reason : 'putValue' successful:  Key: key ; Value: value
        Response received

        [key]:value   put successfully

    **VIN Node Response**

    .. code-block:: none

        14:47:49:680 http: URI: /putValue ; request from: 127.0.0.1:38936
        14:47:49:680 http: 'putValue' request received
        14:47:49:680 http: 'putValue' successful:  Key: key ; Value: value
        14:47:49:680 benc: 'putValue' request latency 0 min 0 sec 0 msec



.. panels::
    :container: container-lg pb-3
    

    .. admonition:: TEST
        :class: myownstyle

        .. code-block:: none

            14:47:49:680 http: URI: /putValue ; request from: 127.0.0.1:38936
            14:47:49:680 http: 'putValue' request received
            14:47:49:680 http: 'putValue' successful:  Key: key ; Value: value
            14:47:49:680 benc: 'putValue' request latency 0 min 0 sec 0 msec
    ---
    
    .. admonition:: VIN CLI OUTPUT
        :class: vincli

        .. code-block:: none

            14:47:49:680 http: URI: /putValue ; request from: 127.0.0.1:38936
            14:47:49:680 http: 'putValue' request received
            14:47:49:680 http: 'putValue' successful:  Key: key ; Value: value
            14:47:49:680 benc: 'putValue' request latency 0 min 0 sec 0 msec


    ---
    :column: col-lg-12 p-2
    .. note::
        SOme text



EXAMPLE 2: USING RAW HTML 
===========================

.. raw:: html

    <div class="row">
    <div class="column">
        <h2>Putting and Getting A Key-Value Pair </h2>
        <p>
        
        The following will showcase how to a put key-value pair onto the network as a simple test to ensure the functionality of the *VIN™*.

        <ul style=“list-style-type:circle”>


        <li>To put a key-value onto the network, in the *VIN™ CLI* session run ``put <key> <value>``; where ``<key>`` and ``<value>`` can be any string that does not contain spaces. For this example ``test_key`` was used for the ``<key>`` and ``test_value`` for the ``<value>``. The following figure displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the peer.</li>

        <li>To view the shard that was placed on the *Kademlia* network, navigate to ``/opt/VIN/kademlia/data/`` and proceed through the folder structure until reaching the file.</li>

        <li>To get a value from the network, in the *VIN™ CLI* session run ``get <key>``; where ``<key>`` is ``test_key`` for this example. The following figure displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the peer.</li>
        
        </p>
    </div>
    <div class="column">    
        <h2>VIN_CLI OUTPUT</h2>
        <p> VIN@127.0.0.1:7070> put key value
        <br> Sending payload:
        <br> {"key":"key","value":"value"}
        <br> 
        <br> Waiting for response...
        <br> Status : 200
        <br> Reason : 'putValue' successful:  Key: key ; Value: value
        <br> Response received
        <br> 
        <br> [key]:value   put successfully
        </p>
        <h2>VIN NODE RESPONSE</h2>
        <p>14:47:49:680 http: URI: /putValue ; request from: 127.0.0.1:38936
        <br>14:47:49:680 http: 'putValue' request received
        <br>14:47:49:680 http: 'putValue' successful:  Key: key ; Value: value
        <br>14:47:49:680 benc: 'putValue' request latency 0 min 0 sec 0 msec
        </p>
    </div>
    </div>

----------------------------------------------------------------------------------------------


EXAMPLE 3: USING CONTAINERS 
================================
    
    .. container:: 

        .. container:: leftside

            **Putting and Getting A Key-Value Pair**

            * The following will showcase how to a put key-value pair onto the network as a simple test to ensure the functionality of the *VIN™*. 
            * To put a key-value onto the network, in the *VIN™ CLI* session run ``put <key> <value>``; where ``<key>`` and ``<value>`` can be any string that does not contain spaces. For this example ``test_key`` was used for the ``<key>`` and ``test_value`` for the ``<value>``. The following figure displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the peer.
           


        .. container:: rightside-col

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

            .. code-block:: none

                14:47:49:680 http: URI: /putValue ; request from: 127.0.0.1:38936
                14:47:49:680 http: 'putValue' request received
                14:47:49:680 http: 'putValue' successful:  Key: key ; Value: value
                14:47:49:680 benc: 'putValue' request latency 0 min 0 sec 0 msec
