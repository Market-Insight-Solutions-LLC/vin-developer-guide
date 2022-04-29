.. _running-the-vin-windows:

***********************************
Running the VIN™ on Windows
***********************************

Currently, there are two ways to set up the *VIN™*: on the same host system or through a local network. Both require very similar setups but differ in the way that peers are configured. The method for instantiating the *VIN™* for both cases and a example to demonstrate the *VIN™'s* ``put``, ``get``, ``spread``, ``gather``, ``share``, ``getPeers``, and ``shutdown`` commands are detailed in the upcoming sections. For detailed information on all of the commands available to the *VIN™*, refer to :ref:`vin-cli`. Before running the *VIN™*, it is good to become familiar with the *VIN™* command flags listed in the following table. Examples of how these are used will be shown when setting up the *VIN™*. 

Note: The logs of all the *VIN™* transactions are located in ``C:\ProgramData\VIN\logs\``. The examples were completed on virtual machines connected to a system running *Windows 10*. 

.. csv-table:: VIN™ Command Flags
    :header: Flag Name, Command Line Instruction, Description
    :widths: 20 10 70 

    List Flag, -l, "Displays a list out all *VIN™* flags along with their descriptions."
    Bootstrap Flag, -b, "Indicates that the node being instantiated will be a bootstrap node."
    Node Flag, -n, "Indicates that the node being instantiated will be a peer node."
    Configuration Directory Flag, -c, "Specify the location of a configuration file to start with."
    Bootstrap IP Flag, -a, "This flag specifies that the next string will be the bootstrap node's IP address which the peer will connect to."
    Bootstrap Port Flag, -s, "Specify a custom bootstrap port."
    Kademlia Port Flag, -p, "This flag specifies that the next string will be the Kademlia port through which the node will communicate bi-directionally with the Kademlia network."
    Receipt Port Flag, -r, "This flag specifies that the next string will be the port through which the node will receive its cryptographic receipts."
    HTTP Port Flag, -h, "This flag specifies that the next string will be the port utilized for HTTP messages by the node."
    LVM Port Flag, -v, "This flag specifies that the next string will be the port through which the node communicates with the *LVM*."
    

Setting up the VIN™ on a Single Host Machine
================================================

While setting up the *VIN™* on single host machine doesn't represent a real-world scenario, it can be a useful architecture for developers to test and work with the *VIN™'s* functionality. To run a *VIN™* on a single host machine, a minimum of three *VIN™* nodes, one bootstrap node and two sender/receiver peer nodes, must be instantiated. Additionally, to perform commands with the network, the *VIN™ Command Line Interface* (*VIN™ CLI*) must be connected to one of the peer nodes. To do so, the following steps should be completed:

* With the *VIN™* installed (refer to :ref:`vin-install`), *VIN™* nodes can be launched from any directory using commands in a command line interface (CLI) terminal session. 
* Begin by opening four terminal windows.
* In one of the sessions, run ``VIN -app -b 127.0.0.1``. This will serve as the bootstrap node with the IP address of the host (``127.0.0.1``) and will occupy port ``8000`` for incoming connections. Note: ``VIN -app -b`` will also work.

.. admonition:: Bootstrap Connection Output 
  :class: admonition-vin-run

  .. code-block:: none

    PS C:\Dev> VIN -app -b 127.0.0.1
    16:39:32:106 benc: VIN
    16:39:32:106 benc: Version:    1.12.3
    16:39:32:106 benc: Git branch: HEAD - da8fd80c
    16:39:32:106 benc: Compiled:   Apr 27 2022 , 14:07:40
    16:39:32:106 benc: Log files:  LOG_04A98_*
    16:39:32:220 root: VIN initializing...
    LVMLibrary initialize_library...
    BuiltinLvmUDPClient.pl library loaded.

    Logical Virtual Machine (LVM)
    GraphStax (c) 2019-2021
    compiled 17:01:29 Apr 26 2022
    git WindowsDev - 64237729

    system.pl library loaded.

    16:39:32:264 root: License validated
    16:39:32:264 root: Recconnect time (s): 60
    16:39:32:264 root: VIN as bootstrap PID: 19096 , 0x04A98
    16:39:32:269 root: Machine name: DESKTOP-2AHN6VJ Available IPs:
    16:39:32:269 root: IP: 10.51.1.143
    16:39:32:269 root: IP: 192.168.1.20
    16:39:32:269 root: IP: 192.168.23.1
    16:39:32:269 root: IP: 192.168.56.1
    16:39:32:269 root: IP: 192.168.108.1
    16:39:32:378 root: Kademlia - peerless engine created (0.0.0.0:8000, :::8000)
    16:39:32:500 root: VIN bootstrap node started at: 0.0.0.0:8000

* In another terminal window, run ``VIN -app -n -a 127.0.0.1 -h 7070 -p 8080 -r 9090``. This will start a *VIN™* peer node and connect it to the bootstrap which has an IP address of ``127.0.0.1``. The peer node runs with an HTTP port of ``7070``, a data (Kademlia) port of ``8080`` and a receipt server port of ``9090``. These ports can be chosen based on the requirements/restrictions of the user. While peers are capable of both sending and receiving information, for clarity in this example, this peer will be treated and referred to as a ``sender`` peer.

.. admonition:: VIN™ Sender Peer Connection Output
  :class: admonition-vin-run

  .. code-block:: none

    PS C:\Dev> VIN -app -n -a 127.0.0.1 -h 7070 -p 8080 -r 9090
    16:39:36:716 benc: VIN
    16:39:36:716 benc: Version:    1.12.3
    16:39:36:716 benc: Git branch: HEAD - da8fd80c
    16:39:36:716 benc: Compiled:   Apr 27 2022 , 14:07:40
    16:39:36:716 benc: Log files:  LOG_04B80_*
    16:39:36:830 root: VIN initializing...
    LVMLibrary initialize_library...
    BuiltinLvmUDPClient.pl library loaded.

    Logical Virtual Machine (LVM)
    GraphStax (c) 2019-2021
    compiled 17:01:29 Apr 26 2022
    git WindowsDev - 64237729

    system.pl library loaded.

    16:39:36:870 root: License validated
    Initializing subsystem: Logging Subsystem
    16:39:36:870 root: Using HTTP port: 7070
    16:39:36:870 root: Recconnect time (s): 60
    16:39:36:870 root: VIN as node PID: 19328 , 0x04B80
    16:39:36:874 root: Node port:  8080
    16:39:36:874 root: HTTP port:  7070
    16:39:36:874 root: Recp port:  9090
    16:39:36:874 root: Bootstrap:  127.0.0.1:8000
    16:39:36:874 root: Chunk size: 1500
    16:39:36:874 root: Redundancy: 5
    16:39:36:877 root: Kademlia - peerless engine created (0.0.0.0:8080, :::8080)
    16:39:36:877 root: Connecting to bootstrap peer at: 127.0.0.1
    16:39:36:892 root: Initialized.Ready.
    16:39:37:016 root: Receipt server starting ( port: 9090 )...
    16:39:37:016 root: VIN node started. port: 8080 ;receipt port: 9090 ;http port: 7070
    16:39:37:016 root: Connected to bootstrap at: 127.0.0.1:8000

* On the third terminal window run ``VIN -app -n -a 127.0.0.1 -h 7071 -p 8081 -r 9091``. Note that the HTTP, data and receipt ports are different than the node which was first instantiated. This peer will be the ``receiver`` peer for this example.

.. admonition:: VIN™ Receiver Peer Connection Output
  :class: admonition-vin-run

  .. code-block:: none

    PS C:\Dev> VIN -app -n -a 127.0.0.1 -h 7071 -p 8081 -r 9091
    16:42:38:534 benc: VIN
    16:42:38:534 benc: Version:    1.12.3
    16:42:38:534 benc: Git branch: HEAD - da8fd80c
    16:42:38:534 benc: Compiled:   Apr 27 2022 , 14:07:40
    16:42:38:534 benc: Log files:  LOG_04AE0_*
    16:42:38:644 root: VIN initializing...
    LVMLibrary initialize_library...
    BuiltinLvmUDPClient.pl library loaded.

    Logical Virtual Machine (LVM)
    GraphStax (c) 2019-2021
    compiled 17:01:29 Apr 26 2022
    git WindowsDev - 64237729

    system.pl library loaded.

    16:42:38:676 root: License validated
    Initializing subsystem: Logging Subsystem
    16:42:38:676 root: Using HTTP port: 7071
    16:42:38:676 root: Recconnect time (s): 60
    16:42:38:676 root: VIN as node PID: 19168 , 0x04AE0
    16:42:38:680 root: Node port:  8081
    16:42:38:680 root: HTTP port:  7071
    16:42:38:680 root: Recp port:  9091
    16:42:38:680 root: Bootstrap:  127.0.0.1:8000
    16:42:38:680 root: Chunk size: 1500
    16:42:38:680 root: Redundancy: 5
    16:42:38:682 root: Kademlia - peerless engine created (0.0.0.0:8081, :::8081)
    16:42:38:682 root: Connecting to bootstrap peer at: 127.0.0.1
    16:42:38:750 root: Initialized.Ready.
    16:42:38:874 root: Receipt server starting ( port: 9091 )...
    16:42:38:874 root: VIN node started. port: 8081 ;receipt port: 9091 ;http port: 7071
    16:42:38:874 root: Connected to bootstrap at: 127.0.0.1:8000

* On the fourth terminal window run ``VIN_CLI 127.0.0.1 7070``. This will successfully launch the *VIN™ CLI* and connect it to the ``sender`` peer with the HTTP port of ``7070``. If everything is working correctly, the terminal window should contain the following:

.. admonition:: VIN™ CLI Connection Output
  :class: admonition-vin-run

  :bold-underline:`VIN™ CLI Output`

  .. code-block:: none

    PS C:\Dev> VIN_CLI 127.0.0.1 7070
    connecting to 127.0.0.1:7070 with timeout: 100 seconds
    Server pong!
    Connected!

  :bold-underline:`Sender Peer Output`

  .. code-block:: none

    16:43:57:970 http: URI: /ping? ; request from: 127.0.0.1:50699


Network Interaction on a Single Host Machine
---------------------------------------------

Put and Get A Key-Value Pair
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following will showcase how to a put key-value pair onto the network as a simple test to ensure the functionality of the *VIN™*. 

* To put a key-value onto the network, in the *VIN™ CLI* terminal window run ``put <key> <value>``; where ``<key>`` and ``<value>`` can be any string that does not contain spaces. For this example ``test_key`` was used for the ``<key>`` and ``test_value`` for the ``<value>``. The following figure displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the peer.

.. admonition:: Successful Put Output
  :class: admonition-vin-run

  :bold-underline:`VIN™ CLI Output`

  .. code-block:: none

    VIN@127.0.0.1:7070> put test_key test_value
    Sending payload:
    {"key":"test_key","value":"test_value"}

    Waiting for response...
    Status : 200
    Reason : 'putValue' successful:  Key: test_key ; Value: test_value
    Response received

    [test_key]:test_value   put successfully

  :bold-underline:`Sender Peer Output`

  .. code-block:: none

    16:46:11:859 http: URI: /putValue ; request from: 127.0.0.1:50730
    16:46:11:859 benc: 'putValue' request latency 0 min 0 sec 0 msec
    16:46:11:859 http: 'putValue' request received
    16:46:11:859 http: 'putValue' successful:  Key: test_key ; Value: test_value

* To view the value that was placed on the *Kademlia* network, navigate to ``C:\ProgramData\VIN\kademlia\data\`` and proceed through the folder structure.
* To get a value from the network, in the *VIN™ CLI* terminal window run ``get <key>``; where ``<key>`` is ``test_key`` for this example. The following displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the ``sender`` peer.

.. admonition:: Successful Get Output
  :class: admonition-vin-run

  :bold-underline:`VIN™ CLI Output`

  .. code-block:: none

    VIN@127.0.0.1:7070> get test_key
    Sending payload:
    {"key":"test_key"}

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    value for test_key got successfully

    [test_key]:test_value  is a valid [key]:value pair

  :bold-underline:`Sender Peer Output`

  .. code-block:: none

    16:49:33:041 http: URI: /getValue ; request from: 127.0.0.1:50776
    16:49:33:041 benc: 'getValue' request latency 0 min 0 sec 0 msec
    16:49:33:041 http: 'getValue' request received
    16:49:33:041 http: 'getValue' successful:  Key: test_key ; Value: test_value


Spread and Gather a File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *VIN™* can spread any file type onto its network. To do a ``spread`` its default configuration (see :ref:`vin-configuration` and :ref:`vin-cli` for more details), perform the following:

* In the *VIN™ CLI* terminal window run ``spread <filepath>``; where the ``<filepath>`` is the absolute (or relative) path and name of the file to be spread. For this example, it is ``C:\Dev\vin_test.txt``. An encrypted cryptographic receipt is generated upon spreading and is stored in ``C:\ProgramData\VIN\receipts\sent\`` and the encrypted data is placed onto the *Kademlia* network and can be seen in ``C:\ProgramData\VIN\kademlia\data\``. Additionally, the data, broken into shards, is viewable in ``C:\ProgramData\VIN\shards\``. Note: the number of shards is dependant on the size of the file and the parameters set in the ``chunker`` object, which is set in ``defaults.cfg`` (see :ref:`vin-configuration` for more details).
* The output of a successful ``spread`` is shown below.

.. admonition:: Successful Spread Output
  :class: admonition-vin-run

  :bold-underline:`VIN™ CLI Output`

  .. code-block:: none

    VIN@127.0.0.1:7070> spread C:\Dev\vin_test.txt

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File spread successfully

    Receipt saved to location : C:\ProgramData\VIN\receipts\sent\CR1906674528

  :bold-underline:`Sender Peer Output`

  .. code-block:: none

    16:58:36:001 http: URI: /spread ; request from: 127.0.0.1:50910
    16:58:36:001 benc: 'spread' chunking latency 0 min 0 sec 0 msec
    16:58:36:001 root: Using default coders pipeline
    Unable to open file
    16:58:36:002 benc: 'spread' file: vin_test.txt size: 31
    16:58:36:001 http: 'spread' request received
    16:58:36:002 root: Validate encoders...
    16:58:36:004 enco: ConcurrentEncoder: avg marks: 1013
    16:58:36:002 root: Enc: ConcurrentEncoder EntanglementEncoder NamingEncoder ValidationEncoder
    16:58:36:005 benc: 'spread' encoding latency 0 min 0 sec 3 msec
    16:58:36:002 root: Validate decoders...
    16:58:36:002 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    16:58:36:002 root: Validate channels...
    16:58:36:002 root: No channels specified
    16:58:36:002 root: Logging pre-encoded file
    16:58:36:003 root: Encoding
    Job Watchdog (1): Job finished signal received
    Job Watchdog (1): Tasks (Processing 0, Pending 0)
    16:58:36:191 benc: 'spread' uploading latency 0 min 0 sec 186 msec
    16:58:36:191 benc: 'spread' total latency 0 min 0 sec 189 msec
    16:58:36:194 http: 'spread' receipt saved to: C:\ProgramData\VIN\receipts\sent\CR1906674528
    16:58:36:191 benc: 'spread' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    16:58:36:191 benc: 'spread' system data size:  20480 ( redundancy = 5 )

* After a file has been spread to the network a cryptographic receipt will be generated on the ``sender`` peer with the path and filename listed in the ``sender`` peers terminal output (for this example it is ``C:\ProgramData\VIN\receipts\sent\CR1906674528``). Using this receipt, the file can be retrieved from the network via the ``gather`` command. To do a ``gather`` with its default configuration, in the *VIN™ CLI* terminal window run ``gather <receipt_path>`` where the ``<receipt_path>`` is ``C:\ProgramData\VIN\receipts\sent\CR1906674528``. For all of the options available to ``gather``, refer to :ref:`vin-cli`. If the file was successfully gathered, the following output should be displayed.

.. admonition:: Successful Gather Output
  :class: admonition-vin-run

  :bold-underline:`VIN™ CLI Output`

  .. code-block:: none
    
    VIN@127.0.0.1:7070> gather C:\ProgramData\VIN\receipts\sent\CR1906674528

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File gathered successfully

    File reconstructed at : C:\ProgramData\VIN\outputs\vin_test\vin_test.txt on node host.
    

  :bold-underline:`Sender Peer Output`

  .. code-block:: none
    
    17:01:23:976 http: URI: /gather ; request from: 127.0.0.1:50950
    17:01:23:977 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    17:01:23:977 benc: 'gather' file: vin_test.txt size: 31
    17:01:23:976 http: 'gather' request received
    Job Watchdog (1): Job finished signal received
    Job Watchdog (1): Tasks (Processing 0, Pending 0)
    17:01:23:978 root: Decoding
    17:01:23:978 benc: 'gather' acquisition latency 0 min 0 sec 1 msec
    17:01:23:978 benc: 'gather' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    17:01:23:983 benc: 'gather' decoding latency 0 min 0 sec 4 msec
    17:01:23:983 root: File rebuild at: C:\ProgramData\VIN\outputs\vin_test\vin_test.txt
    17:01:23:983 benc: 'gather' total latency 0 min 0 sec 6 msec

* To inspect the gathered file, navigate to ``C:\ProgramData\VIN\outputs\`` and enter ``ls``. A folder with the name of the file which was shared should be listed. Enter this folder (``cd <folder_name>``) and run ``ls``. The file which was shared will be displayed and can be inspected to ensure it was successfully shared. 
* Note: the ``gather`` command, by default, will create a new file on the system after it finishes; thus, the gathered file may have a number appended to end of the filename if spread more than once. For more information on how to overwrite the file, or append to its contents, refer to the :ref:`vincli-commands` table.


Share a File
^^^^^^^^^^^^^^^^

The following will describe how to do a ``share`` with its default configuration (see :ref:`vin-configuration` and :ref:`vin-cli` for more details). 

* In the *VIN™ CLI* session, the following command should be run after the required information is determined: ``share <filepath> <ip_address> <receipt_port>``. ``<filepath>`` is the path and filename of the file to be shared, for example, in this case it is ``C:\Dev\vin_test.txt``. Note: any file type can be shared. The ``<ip_address>`` and ``<receipt_port>`` are ``127.0.0.1`` and ``9091``, or the IP address of the host system and the ``receipt_port`` of the second peer running on it.
* Thus, the command to run, for this example, becomes ``share C:\Dev\vin_test.txt 127.0.0.1 9091``. For all of the options available to ``share``, refer to :ref:`vin-cli`. If everything worked correctly, the following should be displayed on the CLI sessions. 

.. admonition:: Successful Share Output
  :class: admonition-vin-run

  :bold-underline:`VIN™ CLI Output`

  .. code-block:: none

    VIN@127.0.0.1:7070> share C:\Dev\vin_test.txt 127.0.0.1 9091

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File shared to 127.0.0.1 9091 successfully (run: 1)

  :bold-underline:`Sender Peer Output`

  .. code-block:: none

    17:02:54:682 http: URI: /share ; request from: 127.0.0.1:50970
    17:02:54:682 benc: 'share' chunking latency 0 min 0 sec 0 msec
    17:02:54:683 root: Using default coders pipeline
    Unable to open file
    17:02:54:682 http: 'share' request received
    17:02:54:683 root: Validate encoders...
    17:02:54:683 benc: 'spread' file: vin_test.txt size: 31
    17:02:54:682 http: Share to: 127.0.0.1:9091 ; File: vin_test.txt ; Size: 31 ; Flag: create
    17:02:54:683 root: Enc: ConcurrentEncoder EntanglementEncoder NamingEncoder ValidationEncoder
    17:02:54:686 enco: ConcurrentEncoder: avg marks: 1013
    17:02:54:683 root: Validate decoders...
    17:02:54:686 benc: 'spread' encoding latency 0 min 0 sec 2 msec
    17:02:54:683 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    17:02:54:683 root: Validate channels...
    17:02:54:683 root: No channels specified
    17:02:54:683 root: Logging pre-encoded file
    17:02:54:684 root: Encoding
    Job Watchdog (1): Job finished signal received
    Job Watchdog (1): Tasks (Processing 0, Pending 0)
    17:02:54:833 benc: 'spread' uploading latency 0 min 0 sec 147 msec
    17:02:54:833 root: Sharing to peer: 127.0.0.1:9091
    17:02:54:833 benc: 'spread' total latency 0 min 0 sec 150 msec
    17:02:54:833 benc: 'spread' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    17:02:54:833 benc: 'spread' system data size:  20480 ( redundancy = 5 )
    17:02:54:859 root: Receipt session started
    17:02:54:859 root: Connected to peer: 127.0.0.1:9091
    17:02:54:860 root: Session token obtained
    17:02:54:860 root: Sending receipt
    17:02:54:865 root: Sending status request
    17:02:54:867 root: Status: File rebuild OK
    17:02:54:867 benc: 'share' receipt latency 0 min 0 sec 34 msec
    17:02:54:867 root: Sharing end session
    17:02:54:867 benc: 'share' encoded data size: 4096
    17:02:54:867 benc: 'share' system data size:  20480 ( redundancy = 5 )
    17:02:54:867 benc: 'share' total latency 0 min 0 sec 185 msec

  :bold-underline:`Receiver Peer Output`

  .. code-block:: none

    17:02:54:849 benc: Share session created. Peer addr: 127.0.0.1:50971
    17:02:54:860 cr-s: Start sharing session
    17:02:54:861 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    17:02:54:861 benc: 'gather' file: vin_test.txt size: 31
    Job Watchdog (1): Job finished signal received
    Job Watchdog (1): Tasks (Processing 0, Pending 0)
    17:02:54:862 root: Decoding
    17:02:54:860 cr-s: Send session id
    17:02:54:862 benc: 'gather' acquisition latency 0 min 0 sec 0 msec
    17:02:54:862 benc: 'gather' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    17:02:54:860 cr-s: Receipt received from: 127.0.0.1:50971
    17:02:54:865 benc: 'gather' decoding latency 0 min 0 sec 3 msec
    17:02:54:865 benc: 'gather' total latency 0 min 0 sec 4 msec
    17:02:54:866 cr-s: Status request from: 127.0.0.1:50971
    17:02:54:866 root: File rebuild at: C:\ProgramData\VIN\outputs\vin_test\vin_test(1).txt

* To manually confirm that the file was shared correctly, enter ``ls`` in a terminal window pointing to the ``C:\ProgramData\VIN\outputs\`` folder directory. A folder with the name of the file which was shared should be listed. Enter this folder (``cd <folder_name>``) and run ``ls``. The file which was shared will be displayed and can be inspected to ensure it was successfully shared.
* Note the ``(1)`` added to the the reconstructed file name ``vin_test(1).txt`` in the above output. As a ``share`` with a default configuration was performed, a copy of the file that was spread in the above example was created. To overwrite, append to the existing, or create a new file, ad for all other options for ``share`` refer to the available options in the :ref:`vin-cli` section. 
* Additionally, the cryptographic receipt for the share is stored in ``C:\ProgramData\VIN\receipts\sent\``, the encrypted data can be seen in ``C:\ProgramData\VIN\kademlia\data\``, and the sharded data is viewable in ``C:\ProgramData\VIN\shards\``. Note: the number of shards is dependant on the size of the file and the parameters set in the ``chunker`` object, which is set in ``defaults.cfg`` (see :ref:`vin-configuration` for more details).


Getting (Listing) the available Peers on the Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the *VIN™ CLI* terminal window connected to the ``sender`` peer, run ``getPeers`` to generate a list of all peers available to the ``sender`` peer. The result will be an output similar to the one displayed in the figure below. 

.. admonition:: Successful GetPeers Output
  :class: admonition-vin-run

  :bold-underline:`VIN™ CLI Output`

  .. code-block:: none

    VIN@127.0.0.1:7070> getPeers
    Sending payload:
    {}

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    Got Peers successfully
    {
        "127.0.0.1:8000": {
            "ip": "127.0.0.1",
            "meta_data": {
            },
            "port": "8000"
        },
        "127.0.0.1:8081": {
            "ip": "127.0.0.1",
            "meta_data": {
                "http_port": "7071",
                "kad_port": "8081",
                "receipt_port": "9091"
            },
            "port": "8081"
        }
    }

  :bold-underline:`Sender Peer Output`

  .. code-block:: none

    17:05:11:894 http: URI: /getPeers ; request from: 127.0.0.1:51018
    17:05:11:894 http: 'getPeers' request received
    17:05:11:957 http: Listing peer: 127.0.0.1:8000
    17:05:11:957 http: MetaData: {}
    17:05:11:957 http: Listing peer: 127.0.0.1:8081
    17:05:11:957 http: MetaData: {"kad_port":"8081","receipt_port":"9091","http_port":"7071"}

As two peers (the bootstrap and the ``receiver`` peer) are connected to ``sender`` peer, the result contain two outputs. The first listed is the bootstrap (``127.0.0.1:8000``), while the second is the ``receiver`` peer (``127.0.0.1:8081``). Note how the ``receiver`` peer contains additional port information which was supplied during its instantiation.


Shutting Down the Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Press **ctrl + c** while the bootstrap node's terminal window is active to stop the process.

.. admonition:: Bootstrap Shutdown Output
  :class: admonition-vin-run

  .. code-block:: none
    
    17:09:39:136 root: VIN exit

* To shutdown a peer node which is connected to the *VIN™ CLI*, run ``shutdown`` in the *VIN™ CLI* terminal window connected to the peer. Alternatively, press **ctrl + c** while the peer node's terminal window is active to end the process.

.. admonition:: Sender Peer Shutdown Output
  :class: admonition-vin-run

  :bold-underline:`VIN™ CLI Output`

  .. code-block:: none
    
    VIN@127.0.0.1:7070> shutdown
    <h1>Exit<h1>

  :bold-underline:`Sender Peer Output`

  .. code-block:: none

    17:10:12:416 http: URI: /exit ; request from: 127.0.0.1:51079
    17:10:12:416 http: 'exit' request received
    17:10:12:416 http: HTTP server exit
    Uninitializing subsystem: Logging Subsystem
    17:10:20:105 root: VIN exit


* Press **ctrl + c** while the peer node's terminal window is active to kill the process.

.. admonition:: Receiver Peer Shutdown Output
  :class: admonition-vin-run

  .. code-block:: none

    17:11:45:248 http: HTTP server exit
    Uninitializing subsystem: Logging Subsystem
    17:11:53:205 root: VIN exit


* To exit from the *VIN™ CLI*, type **exit** and hit **enter** in the *VIN™ CLI* terminal window. Alternatively, **ctrl + c** may be pressed.

.. admonition:: VIN™ CLI Shutdown Output
  :class: admonition-vin-run

  .. code-block:: none
    
    VIN@127.0.0.1:7070> So long for now.

--------------------------------------------------------------------

.. _vin-local-network-windows:

Setting up the VIN™ on a Local Network 
===========================================

To run the *VIN™* on an IP based network, such as *Amazon Web Services (AWS)*, a Local Area Network (LAN) with routers/switches and Dynamic Host Communication Protocol (DHCP), *VMware*, etc., complete the following steps:

* For this example, two systems will be used: ``system_1`` and ``system_2``.
* Complete the *VIN™* installation procedure on each system (refer to :ref:`vin-install`).
* On each system, open three terminal windows. 
* Since each system will have it's own IP address, deemed ``<ip_1>`` and ``<ip_2>`` for this example, it is imperative to determine and record them.
* Run ``ipconfig`` in one of the sessions to generate an output similar to the one below.

.. admonition:: System 1 ipconfig Output
  :class: admonition-vin-run

  .. code-block:: none
    
    Ethernet adapter Ethernet 2:

      Connection-specific DNS Suffix  . : mis.local
      IPv6 Address. . . . . . . . . . . : 2606:7100:1cac:1:2::2
      Link-local IPv6 Address . . . . . : fe80::9a8:be53:6b18:d46b%11
      IPv4 Address. . . . . . . . . . . : 10.51.1.143
      Subnet Mask . . . . . . . . . . . : 255.0.0.0
      Default Gateway . . . . . . . . . :

    Wireless LAN adapter Wi-Fi:

      Connection-specific DNS Suffix  . :
      Link-local IPv6 Address . . . . . : fe80::4d82:b482:59ef:8305%10
      IPv4 Address. . . . . . . . . . . : 192.168.1.20
      Subnet Mask . . . . . . . . . . . : 255.255.255.0
      Default Gateway . . . . . . . . . : 192.168.1.1

* Record the address next to the ``IPv4 Address`` parameter for the required network connection (i.e., wired or wireless). From the output above, the ``IPv4 Address`` value of ``192.168.1.20`` corresponds to a wireless connection, ``Wireless LAN adapter Wi-Fi``, and was recorded as ``<ip_1>``.
* Repeat the above instructions for ``system_2`` and record ``<ip_2>`` (for this example it is ``192.168.23.128``).
* In one of the terminal windows on ``system_1`` run ``VIN -app -b <ip_1>``. For this example, ``<ip_1>`` is ``192.168.1.20``. This will serve as the bootstrap node and will occupy port ``8000`` for incoming connections. If the bootstrap was successfully launched, its terminal window will output similar results to those below.

.. admonition:: System 1 Bootstrap Connection Output 
  :class: admonition-vin-run

  .. code-block:: none

    PS C:\Dev> VIN -app -b 192.168.1.20
    17:19:30:596 benc: VIN
    17:19:30:596 benc: Version:    1.12.3
    17:19:30:596 benc: Git branch: HEAD - da8fd80c
    17:19:30:596 benc: Compiled:   Apr 27 2022 , 14:07:40
    17:19:30:596 benc: Log files:  LOG_048FC_*
    17:19:30:705 root: VIN initializing...
    LVMLibrary initialize_library...
    BuiltinLvmUDPClient.pl library loaded.

    Logical Virtual Machine (LVM)
    GraphStax (c) 2019-2021
    compiled 17:01:29 Apr 26 2022
    git WindowsDev - 64237729

    system.pl library loaded.

    17:19:30:799 root: License validated
    17:19:30:799 root: Recconnect time (s): 60
    17:19:30:799 root: VIN as bootstrap PID: 18684 , 0x048FC
    17:19:30:804 root: Machine name: DESKTOP-2AHN6VJ Available IPs:
    17:19:30:804 root: IP: 10.51.1.143
    17:19:30:804 root: IP: 192.168.1.20
    17:19:30:804 root: IP: 192.168.23.1
    17:19:30:804 root: IP: 192.168.56.1
    17:19:30:804 root: IP: 192.168.108.1
    17:19:30:905 root: Kademlia - peerless engine created (0.0.0.0:8000, :::8000)
    17:19:31:043 root: VIN bootstrap node started at: 0.0.0.0:8000

* In another terminal window on ``system_1``, run ``VIN -app -n -a <ip_1> -h 7070 -p 8080 -r 9090``. This will start a *VIN™* peer node with an HTTP port of ``7080``, a data (*Kademlia*) port of ``8080`` and a receipt server port of ``9090`` and connect to the bootstrap on ``<ip_1>``. Note: these ports can be chosen based on the requirements/restrictions of the user. 
* If the peer connects to the bootstrap successfully, the terminal window will contain a similar output to the one below. Take note that it displays the ports and IP address that was used during the peer's instantiation.

.. admonition:: System 1 VIN™ Peer Connection Output
  :class: admonition-vin-run

  .. code-block:: none 

    PS C:\Dev> VIN -app -n -a 192.168.1.20 -h 7070 -p 8080 -r 9090
    17:20:08:300 benc: VIN
    17:20:08:300 benc: Version:    1.12.3
    17:20:08:300 benc: Git branch: HEAD - da8fd80c
    17:20:08:300 benc: Compiled:   Apr 27 2022 , 14:07:40
    17:20:08:300 benc: Log files:  LOG_00C30_*
    17:20:08:410 root: VIN initializing...
    LVMLibrary initialize_library...
    BuiltinLvmUDPClient.pl library loaded.

    Logical Virtual Machine (LVM)
    GraphStax (c) 2019-2021
    compiled 17:01:29 Apr 26 2022
    git WindowsDev - 64237729

    system.pl library loaded.

    17:20:08:443 root: License validated
    Initializing subsystem: Logging Subsystem
    17:20:08:443 root: Using HTTP port: 7070
    17:20:08:443 root: Recconnect time (s): 60
    17:20:08:443 root: VIN as node PID: 3120 , 0x00C30
    17:20:08:456 root: Node port:  8080
    17:20:08:456 root: HTTP port:  7070
    17:20:08:456 root: Recp port:  9090
    17:20:08:456 root: Bootstrap:  192.168.1.20:8000
    17:20:08:456 root: Chunk size: 1500
    17:20:08:456 root: Redundancy: 5
    17:20:08:458 root: Kademlia - peerless engine created (0.0.0.0:8080, :::8080)
    17:20:08:458 root: Connecting to bootstrap peer at: 192.168.1.20
    17:20:08:471 root: Initialized.Ready.
    17:20:08:594 root: Receipt server starting ( port: 9090 )...
    17:20:08:594 root: VIN node started. port: 8080 ;receipt port: 9090 ;http port: 7070
    17:20:08:594 root: Connected to bootstrap at: 192.168.1.20:8000

* In the third terminal window on ``system_1``, run ``VIN_CLI <ip_1> 7070``. This will launch the *VIN™ CLI* if the above steps were completed successfully. If everything is working correctly, the terminal windows should contain the following:

.. admonition:: System 1 VIN™ CLI Connection Output
  :class: admonition-vin-run

  :bold-underline:`System 1 VIN™ CLI Output`

  .. code-block:: none

    PS C:\Dev> VIN_CLI 192.168.1.20 7070
    connecting to 192.168.1.20:7070 with timeout: 100 seconds
    Server pong!
    Connected!

  :bold-underline:`System 1 Peer Output`

  .. code-block:: none

    17:22:15:269 http: URI: /ping? ; request from: 192.168.1.20:51293

* In one of the terminal windows on ``system_2`` run ``VIN -app -n -a <ip_1> -h 7070 -p 8080 -r 9090``, where ``<ip_1>`` is ``192.168.1.20`` for this example. This will connect to the bootstrap located on ``system_1`` with its IP address of ``<ip_1>``.
* In the second terminal window, run ``VIN_CLI <ip_2> 7071`` to connect to the peer on ``system_2`` using ``<ip_2>`` (or ``192.168.23.128`` for this example).  
* In the final terminal window, navigate to ``C:\ProgramData\VIN\outputs``. This directory will contain the received file after it has been reconstructed during the example in the following section. 


Network Interaction on a Local Network 
-------------------------------------------------

With *VIN™* peers successfully running on both systems, a number of commands can be entered to interact with the instantiated network and between the peers themselves. The following examples will highlight the use of the ``put``, ``get``, ``share``, ``spread``, ``gather``, ``getPeers`` and ``shutdown`` commands with the *VIN™ CLI*.  For a full list of the *VIN™ CLI's* functionality refer to :ref:`vin-cli`. Additionally, refer to :ref:`vin-configuration` for more information regarding locations of files generated while using the *VIN™ CLI*.


Put and Get A Key-Value Pair
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following will showcase how to put a key-value pair onto the network. While the *VIN™ CLI* connected to the peer on ``system_1`` will be utilized for the ``put``, any peer connected to a *VIN™ CLI* has this capability.  

* To put a key-value pair onto the network, in the *VIN™ CLI* terminal window on ``system_1``, run ``put <key> <value>``; where ``<key>`` and ``<value>`` can be any string that does not contain spaces. For this example ``test_key`` was used for the ``<key>`` and ``test_value`` for the ``<value>``. The following figure displays the result of  running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the peer.

.. admonition:: Successful Put Output
  :class: admonition-vin-run

  :bold-underline:`System 1 VIN™ CLI Output`

  .. code-block:: none

    VIN@192.168.1.20:7070> put test_key test_value
    Sending payload:
    {"key":"test_key","value":"test_value"}

    Waiting for response...
    Status : 200
    Reason : 'putValue' successful:  Key: test_key ; Value: test_value
    Response received

    [test_key]:test_value   put successfully

  :bold-underline:`System 1 Peer Output`

  .. code-block:: none

    17:30:06:303 http: URI: /putValue ; request from: 192.168.1.20:51389
    17:30:06:304 benc: 'putValue' request latency 0 min 0 sec 0 msec
    17:30:06:304 http: 'putValue' request received
    17:30:06:304 http: 'putValue' successful:  Key: test_key ; Value: test_value

* To view the shard that was placed on the *Kademlia* network, navigate to ``C:\ProgramData\VIN\kademlia\data\`` and proceed through the folder structure until reaching the file.
* To get a value from the network, in the *VIN™ CLI* terminal window on ``system_2``, run ``get <key>``; where ``<key>`` is ``test_key`` for this example. The following output displays the result of running this command.

.. admonition:: Successful Get Output
  :class: admonition-vin-run

  :bold-underline:`System 2 VIN™ CLI Output`

  .. code-block:: none

    VIN@192.168.23.128:7070> get test_key
    Sending payload:
    {"key":"test_key"}

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    value for test_key got successfully

    [test_key]:test_value  is a valid [key]:value pair

  :bold-underline:`System 2 Peer Output`

  .. code-block:: none

    13:00:40:873 http: URI: /getValue ; request from: 192.168.23.128:52087
    13:00:40:873 benc: Found candidates number: 2
    13:00:40:873 http: 'getValue' request received
    13:00:41:076 http: 'getValue' successful:  Key: test_key ; Value: test_value
    13:00:41:076 benc: 'getValue' request latency 0 min 0 sec 202 msec



Spread and Gather a File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *VIN™* can spread any file type onto its network. To do a ``spread`` with its default configuration (see :ref:`vin-configuration` and :ref:`vin-cli` for more details), perform the following:

* In the *VIN™ CLI* terminal window on ``system_`1`` run ``spread <filepath>``; where the ``<filepath>`` is the path and name of the file to be spread. For this example, it is ``C:\Dev\vin_network_test.txt``. For all of the options available to ``spread``, refer to :ref:`vin-cli`. An encrypted cryptographic receipt is generated upon spreading and is stored in ``C:\ProgramData\VIN\receipts\sent\`` and the encrypted data is placed onto the *Kademlia* network and can be seen in ``C:\ProgramData\VIN\kademlia\data\``. Additionally, the data, broken into shards, is viewable in ``C:\ProgramData\VIN\shards\``. Note: the number of shards is dependant on the size of the file and the parameters set in the ``chunker`` object, which is set in ``defaults.cfg`` (see :ref:`vin-configuration` for more details).
* The output of a successful ``spread`` is shown below.

.. admonition:: Successful Spread Output
  :class: admonition-vin-run

  :bold-underline:`System 1 VIN™ CLI Output`

  .. code-block:: none

    VIN@192.168.1.20:7070> spread C:\Dev\vin_network_test.txt

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File spread successfully

    Receipt saved to location : C:\ProgramData\VIN\receipts\sent\CR1908902645

  :bold-underline:`System 1 Peer Output`

  .. code-block:: none

    17:35:40:278 http: URI: /spread ; request from: 192.168.1.20:51466
    17:35:40:278 benc: 'spread' chunking latency 0 min 0 sec 0 msec
    17:35:40:278 http: 'spread' request received
    17:35:40:279 root: Using default coders pipeline
    17:35:40:279 root: Validate encoders...
    17:35:40:279 root: Enc: ConcurrentEncoder EntanglementEncoder NamingEncoder ValidationEncoder
    17:35:40:279 benc: 'spread' file: vin_network_test.txt size: 32
    17:35:40:280 root: Validate decoders...
    17:35:40:280 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    17:35:40:280 root: Validate channels...
    17:35:40:280 root: No channels specified
    17:35:40:280 root: Logging pre-encoded file
    17:35:40:280 root: Encoding
    17:35:40:281 enco: ConcurrentEncoder: avg marks: 1016
    17:35:40:281 benc: 'spread' encoding latency 0 min 0 sec 31 msec
    17:35:40:281 benc: Found: 3 peers
    Job Watchdog (1): Job finished signal received
    Job Watchdog (1): Tasks (Processing 0, Pending 0)
    17:35:40:281 benc: 'spread' uploading latency 0 min 0 sec 296 msec
    17:35:40:281 benc: 'spread' total latency 0 min 0 sec 327 msec
    17:35:40:281 benc: 'spread' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    17:35:40:281 benc: 'spread' system data size:  20480 ( redundancy = 5 )
    17:35:40:285 http: 'spread' receipt saved to: C:\ProgramData\VIN\receipts\sent\CR1908902645


* After a file has been spread to the network a cryptographic receipt will be generated as is shown in the ``system_1`` output. Using this receipt, the file can be retrieved from the network via the ``gather`` command. However, the receipt is located on ``system_1`` (the system which did the spread), and ``system_2`` will need to have access to it. Therefore it must be copied to that system before a ``gather`` from ``system_2`` can be complete.

..
  _* One way of securely copying the file from ``system_1`` to ``system_2`` is _by doing the following:
  _
  _
  _* scp C:\Dev\vin_test.txt 192.168.23.128:\C\Dev\
  _
  _.. admonition:: scp of the Cryptographic Receipt
  _  :class: admonition-vin-run
  _
  _  .. code-block:: none
  _
  _    scp C:\Dev\vin_test.txt 192.168.23.128:\C\Dev\

* With the cryptographic receipt copied, to do a ``gather``, in the *VIN™ CLI* terminal window on ``system_2`` run ``gather <receipt_path>``. The ``<receipt_path>`` for this example is ``C:\ProgramData\VIN\receipts\received\CR1908902645``. For all of the options available to ``gather``, refer to :ref:`vin-cli`. If the file was successfully gathered, the following output should be displayed.

.. admonition:: Successful Gather Output
  :class: admonition-vin-run

  :bold-underline:`System 2 VIN™ CLI Output`

  .. code-block:: none
    
    VIN@192.168.23.128:7070> gather C:\ProgramData\VIN\receipts\received\CR1908902645

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File gathered successfully

    File reconstructed at : C:\ProgramData\VIN\outputs\vin_network_test\vin_network_test.txt on node host.
    VIN@192.168.23.128:7070>

  :bold-underline:`System 2 Peer Output`

  .. code-block:: none
    
    13:08:38:328 http: URI: /gather ; request from: 192.168.23.128:52090
    13:08:38:328 http: 'gather' request received
    13:08:38:328 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    13:08:38:328 benc: 'gather' file: vin_network_test.txt size: 32
    Job Watchdog (1): Job finished signal received
    Job Watchdog (1): Tasks (Processing 0, Pending 0)
    13:08:38:672 benc: 'gather' acquisition latency 0 min 0 sec 343 msec
    13:08:38:672 root: Decoding
    13:08:38:672 benc: 'gather' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    13:08:38:672 benc: 'gather' decoding latency 0 min 0 sec 0 msec
    13:08:38:672 benc: 'gather' total latency 0 min 0 sec 343 msec
    13:08:38:672 root: File rebuild at: C:\ProgramData\VIN\outputs\vin_network_test\vin_network_test.txt

* To inspect the gathered file, refer to the folder ``C:\ProgramData\VIN\outputs\outputs\`` and enter ``ls``. A folder with the name of the file which was gathered should be listed. Enter this folder (``cd <folder_name>``) and run ``ls``. The file which was shared will be displayed and can be inspected to ensure it was successfully gathered. 
* Note: the ``gather`` command, by default, will create a new file on the system after it finishes; thus, the gathered file may have a number appended to end of the filename. For more information on how to overwrite the file, or append to its contents, refer to the :ref:`vincli-commands` table.


Share a File
^^^^^^^^^^^^^^^

The following will describe how to share files between the peer on ``system_1`` to the peer located on ``system_2``. Note: the peer/*VIN™ CLI* connection on ``system_2`` could also be used to perform the share.

* In the *VIN™ CLI* terminal window on ``system_1``, the following command should be run after the required information is determined: ``share <filepath> <ip_address> <receipt_port>``. ``<filepath>`` is the path and filename of the file to be shared, for example, in this case it is ``C:\Dev\vin_network_test.txt``. Note: any file type can be shared. The ``<ip_address>`` and ``<receipt_port>`` are ``<ip_2>`` (or ``192.168.23.128`` for this example) and ``9090``, or the IP address of ``system_2`` and the ``receipt_port`` of the peer running on it.
* Thus, the command to run, for this example, becomes ``share C:\Dev\vin_network_test.txt 192.168.23.128 9090``. If everything worked correctly, the following should be displayed on ``system_1`` and ``system_2``. 

.. admonition:: Successful Share Output
  :class: admonition-vin-run

  :bold-underline:`System 1 VIN™ CLI Output`

  .. code-block:: none

    VIN@192.168.1.20:7070> share C:\Dev\vin_network_test.txt 192.168.23.128 9090

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File shared to 192.168.23.128 9090 successfully (run: 1)
    

  :bold-underline:`System 1 Peer Output`

    17:41:27:439 http: URI: /share ; request from: 192.168.1.20:54843
    17:41:27:439 benc: 'share' chunking latency 0 min 0 sec 0 msec
    17:41:27:439 root: Using default coders pipeline
    Unable to open file
    17:41:27:440 http: 'share' request received
    17:41:27:440 root: Validate encoders...
    17:41:27:440 benc: 'spread' file: vin_network_test.txt size: 32
    17:41:27:440 root: Enc: ConcurrentEncoder EntanglementEncoder NamingEncoder ValidationEncoder
    17:41:27:440 enco: ConcurrentEncoder: avg marks: 1014
    17:41:27:440 http: Share to: 192.168.23.128:9090 ; File: vin_network_test.txt ; Size: 32 ; Flag: create
    17:41:27:440 benc: 'spread' encoding latency 0 min 0 sec 2 msec
    17:41:27:441 root: Validate decoders...
    17:41:27:441 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    17:41:27:441 root: Validate channels...
    17:41:27:441 root: No channels specified
    17:41:27:441 root: Logging pre-encoded file
    17:41:27:441 root: Encoding
    17:41:27:441 benc: Found: 3 peers
    Job Watchdog (1): Job finished signal received
    Job Watchdog (1): Tasks (Processing 0, Pending 0)
    17:41:27:443 root: Sharing to peer: 192.168.23.128:9090
    17:41:27:443 benc: 'spread' uploading latency 0 min 0 sec 163 msec
    17:41:27:443 benc: 'spread' total latency 0 min 0 sec 166 msec
    17:41:27:443 benc: 'spread' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    17:41:27:443 benc: 'spread' system data size:  20480 ( redundancy = 5 )
    17:41:27:463 root: Receipt session started
    17:41:27:463 root: Connected to peer: 192.168.23.128:9090
    17:41:27:525 root: Session token obtained
    17:41:27:525 root: Sending receipt
    17:41:27:525 root: Sending status request
    17:41:27:538 root: Status: File rebuild OK
    17:41:27:538 benc: 'share' receipt latency 0 min 0 sec 110 msec
    17:41:27:538 root: Sharing end session
    17:41:27:539 benc: 'share' encoded data size: 4096
    17:41:27:539 benc: 'share' system data size:  20480 ( redundancy = 5 )
    17:41:27:539 benc: 'share' total latency 0 min 0 sec 277 msec


  :bold-underline:`System 2 Peer Output`

  .. code-block:: none
    
    13:11:31:487 benc: Share session created. Peer addr: 192.168.1.20:54844
    13:11:31:492 cr-s: Start sharing session
    13:11:31:492 cr-s: Send session id
    13:11:31:492 cr-s: Receipt received from: 192.168.1.20:54844
    13:11:31:492 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    Job Watchdog (1): Job finished signal received
    Job Watchdog (1): Tasks (Processing 0, Pending 0)
    13:11:31:493 benc: 'gather' file: vin_network_test.txt size: 32
    13:11:31:493 root: Decoding
    13:11:31:494 benc: 'gather' acquisition latency 0 min 0 sec 15 msec
    13:11:31:494 benc: 'gather' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    13:11:31:494 benc: 'gather' decoding latency 0 min 0 sec 0 msec
    13:11:31:494 benc: 'gather' total latency 0 min 0 sec 15 msec
    13:11:31:495 cr-s: Status request from: 192.168.1.20:54844
    13:11:31:495 benc: 'gather' end_stream_session
    13:11:31:495 root: File rebuild at: C:\ProgramData\VIN\outputs\vin_network_test\vin_network_test(1).txt
    13:11:31:496 benc: 'gather' rebuilt latency: 0 min 0 sec 0 msec
    13:11:31:496 cr-s: Status: File rebuild OK
    13:11:31:496 cr-s: Share ended. 0 min 0 sec 93 msec
    13:11:31:554 cr-s: Connection with peer: 192.168.1.20:54844 ended


* To manually confirm that the file was shared correctly, on ``system_2`` navigate to the ``Program Files\Virgil\VIN\outputs`` folder directory and enter ``ls``. A folder with the name of the file which was shared should be listed. Enter this folder (``cd <folder_name>``) and run ``ls``. The file which was shared will be displayed and can be inspected to ensure it was successfully shared.
* Note the ``(1)`` added to the the reconstructed file name ``vin_network_test(1).txt``. As a basic ``share`` was performed, a copy of the file that was spread in the above example was created. To overwrite, append to the existing, or create a new file, refer to the available options in the :ref:`vin-cli` section. The table located on this page also details all of the options available to ``share``.
* Additionally, the cryptographic receipt for the ``share`` is stored in ``C:\ProgramData\VIN\receipts\sent\``, the encrypted data can be seen in ``C:\ProgramData\VIN\kademlia\data``, and the sharded data is viewable in ``C:\ProgramData\VIN\shards\``. Note: the number of shards is dependant on the size of the file and the parameters set in the ``chunker`` object, which is set in ``defaults.cfg`` (see :ref:`vin-configuration` for more details).


Getting (Listing) the available Peers on the Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the *VIN™ CLI* terminal on ``system_1``, run ``getPeers`` to generate a list of all peers connected to a bootstrap node. The result will be an output similar to the one displayed in the figure below.   

.. admonition:: System 1 Successful GetPeers Output
  :class: admonition-vin-run

  :bold-underline:`System 1 VIN™ CLI Output`

  .. code-block:: none

    VIN@192.168.1.20:7070> getPeers
    Sending payload:
    {}

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    Got Peers successfully
    {
        "192.168.1.20:8000": {
            "ip": "192.168.1.20",
            "meta_data": {
            },
            "port": "8000"
        },
        "192.168.23.128:8080": {
            "ip": "192.168.23.128",
            "meta_data": {
                "http_port": "7070",
                "kad_port": "8080",
                "receipt_port": "9090"
            },
            "port": "8080"
        }       
    }

  :bold-underline:`System 1 Peer Output`

  .. code-block:: none

    17:43:46:229 http: URI: /getPeers ; request from: 192.168.1.20:51585
    17:43:46:229 http: 'getPeers' request received
    17:43:47:244 http: Listing peer: 192.168.1.20:8000
    17:43:47:244 http: MetaData: {}
    17:43:47:244 http: Listing peer: 192.168.23.128:8080
    17:43:47:244 http: MetaData: {"kad_port":"8080","receipt_port":"9090","http_port":"7070"}

* As two peers (the bootstrap and the ``system_2`` peer) are connected to ``system_1`` peer, the result contain two outputs. The first listed is the bootstrap (``192.168.1.20:8000``), while the second is the ``system_2`` peer (``192.168.23.128:8080``). Note how the ``system_2`` peer contains additional port information which was supplied during its instantiation.
* In the *VIN™ CLI* terminal on ``system_2``, run ``getPeers`` to generate a list of all peers connected to a bootstrap node. The result will be an output similar to the one displayed in the figure below.  

.. admonition:: System 2 Successful GetPeers Output
  :class: admonition-vin-run

  :bold-underline:`System 2 VIN™ CLI Output`

  .. code-block:: none

    VIN@192.168.23.128:7070> getPeers
    Sending payload:
    {}

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    Got Peers successfully
    {
        "192.168.1.20:8000": {
            "ip": "192.168.1.20",
            "meta_data": {
            },
            "port": "8000"
        },
        "192.168.1.20:8080": {
            "ip": "192.168.1.20",
            "meta_data": {
                "http_port": "7070",
                "kad_port": "8080",
                "receipt_port": "9090"
            },
            "port": "8080"
        }    
    }

  :bold-underline:`System 2 Peer Output`

  .. code-block:: none

    17:45:56:331 http: URI: /getPeers ; request from: 192.168.23.128:51585
    17:45:57:331 http: 'getPeers' request received
    17:45:57:445 http: Listing peer: 192.168.1.20:8000
    17:45:57:445 http: MetaData: {}
    17:45:57:445 http: Listing peer: 192.168.1.20:8080
    17:45:57:445 http: MetaData: {"kad_port":"8080","receipt_port":"9090","http_port":"7070"}

* Once again two peers (the bootstrap and the ``system_1`` peer) are displayed in the outputs. The first listed is the bootstrap (``192.168.1.20:8000``), while the second is the ``system_1`` peer (``192.168.1.20:8080``). 

Shutting Down the Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Press **ctrl + c** while the bootstrap node's terminal window is active to stop the process.

.. admonition:: Bootstrap Shutdown Output
  :class: admonition-vin-run

  .. code-block:: none
    
    17:52:28:925 root: VIN exit

* To shutdown a peer node which is connected to the *VIN™ CLI*, run ``shutdown`` in the *VIN™ CLI* terminal window connected to the peer. Alternatively, press **ctrl + c** while the peer node's terminal window is active to end the process.

.. admonition:: System 1 Peer Shutdown Output
  :class: admonition-vin-run

  :bold-underline:`System 1 VIN™ CLI Output`

  .. code-block:: none
    
    VIN@192.168.1.20:7070> shutdown
    <h1>Exit<h1>

  :bold-underline:`System 1 Peer Output`

  .. code-block:: none

    17:52:58:451 http: URI: /exit ; request from: 192.168.1.20:51700
    17:52:58:451 http: 'exit' request received
    17:52:58:452 http: HTTP server exit
    Uninitializing subsystem: Logging Subsystem
    17:53:07:502 root: VIN exit


* To exit from the *VIN™ CLI*, type **exit** and hit **enter** in the *VIN™ CLI* terminal window. Alternatively, **ctrl + c** may be pressed.

.. admonition:: System 1 VIN™ CLI Shutdown Output
  :class: admonition-vin-run

  .. code-block:: none
    
    VIN@192.168.1.20:7070> exit
    So long for now.


* The peer and *VIN™ CLI* for ``system_2`` can be shut down in the same manner listed above.

