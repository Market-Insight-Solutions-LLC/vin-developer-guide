.. _running-the-vin-linux:

***********************************
Running the VIN™ on Linux
***********************************

Currently, there are two ways to set up the *VIN™*: on the same host system or through a local network. Both require very similar setups but differ in the way that peers are configured. The method for instantiating the *VIN™* for both cases and a example to demonstrate the *VIN™'s* ``put``, ``get``, ``spread``, ``gather``, ``share``, ``getPeers``, and ``shutdown`` commands are detailed in the upcoming sections. For detailed information on all of the commands available to the *VIN™*, refer to :ref:`vin-cli`. Before running the *VIN™*, it is good to become familiar with the *VIN™* command flags listed in the following table. Examples of how these are used will be shown when setting up the *VIN™*. 

Note: The logs of all the *VIN™* transactions are located in ``/var/log/VIN/logs/``. The examples were completed on virtual machines connected to a system running *Ubuntu*. 

.. This information came from C:\Dev\qtoken-cpp\apps\helper.cpp 

.. csv-table:: VIN™ Command Flags
    :header: Flag Name, Command Line Instruction, Description
    :widths: 20 10 70
    :width: 100%

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
* In one of the windows, run ``VIN -b 127.0.0.1``. This will serve as the bootstrap node with the IP address of the host (``127.0.0.1``) and will occupy port ``8000`` for incoming connections. Note: ``VIN -b`` will also work.

.. admonition:: Bootstrap Connection Output 
  :class: admonition-vin-run

  .. code-block:: none

    user@vin1:~$ VIN -b
    17:17:17:665 benc: VIN
    17:17:17:665 benc: Version:    1.12.3
    17:17:17:665 benc: Git branch: HEAD - da8fd80c
    17:17:17:665 benc: Compiled:   Apr  7 2022 , 15:28:19
    17:17:17:665 benc: Log files:  LOG_07C0F_*
    17:17:17:765 root: VIN initializing...
    LVMLibrary initialize_library...
    BuiltinLvmUDPClient.pl library loaded.

    Logical Virtual Machine (LVM)
    GraphStax (c) 2019-2021
    compiled 07:56:17 Dec 22 2021
    git WindowsDev - 94d910fc

    system.pl library loaded.

    17:17:17:819 root: License validated
    17:17:17:820 root: Recconnect time (s): 60
    17:17:17:820 root: VIN as bootstrap PID: 31759 , 0x07C0F
    17:17:17:820 root: Machine name: vin1 Available IPs:
    17:17:17:820 root: IP: 127.0.1.1
    17:17:17:921 root: Kademlia - peerless engine created (0.0.0.0:8000, :::8000)
    17:17:18:031 root: VIN bootstrap node started at: 0.0.0.0:8000


* In another terminal window, run ``VIN -n -a 127.0.0.1 -h 7070 -p 8080 -r 9090``. This will start a *VIN™* peer node and connect it to the bootstrap which has an IP address of ``127.0.0.1``. The peer node runs with an HTTP port of ``7070``, a data (Kademlia) port of ``8080`` and a receipt server port of ``9090``. These ports can be chosen based on the requirements/restrictions of the user. While peers are capable of both sending and receiving information, for clarity in this example, this peer will be treated and referred to as a ``sender`` peer.

.. admonition:: VIN™ Sender Peer Connection Output
  :class: admonition-vin-run

  .. code-block:: none
    
    user@vin1:~$ VIN -n -a 127.0.0.1 -h 7070 -p 8080 -r 9090
    18:10:28:288 benc: VIN
    18:10:28:288 benc: Version:    1.12.3
    18:10:28:288 benc: Git branch: HEAD - da8fd80c
    18:10:28:288 benc: Compiled:   Apr  7 2022 , 15:28:19
    18:10:28:288 benc: Log files:  LOG_07C25_*
    LVMLibrary initialize_library...
    18:10:28:389 root: VIN initializing...
    BuiltinLvmUDPClient.pl library loaded.

    Logical Virtual Machine (LVM)
    GraphStax (c) 2019-2021
    compiled 07:56:17 Dec 22 2021
    git WindowsDev - 94d910fc

    system.pl library loaded.

    18:10:28:415 root: License validated
    18:10:28:415 root: Using HTTP port: 7070
    18:10:28:415 root: Recconnect time (s): 60
    18:10:28:415 root: VIN as node PID: 31781 , 0x07C25
    18:10:28:416 fuse: Initializing fuse peer defaults
    Initializing subsystem: Logging Subsystem
    18:10:28:707 root: Node port:  8080
    18:10:28:707 root: HTTP port:  7070
    18:10:28:707 root: Recp port:  9090
    18:10:28:708 root: Bootstrap:  127.0.0.1:8000
    18:10:28:708 root: Chunk size: 1500
    18:10:28:708 root: Redundancy: 5
    18:10:28:710 root: Kademlia - peerless engine created (0.0.0.0:8080, :::8080)
    18:10:28:711 root: Connecting to bootstrap peer at: 127.0.0.1
    18:10:28:720 root: Initialized.Ready.
    18:10:28:830 root: Receipt server starting ( port: 9090 )...
    18:10:28:831 root: VIN node started. port: 8080 ;receipt port: 9090 ;http port: 7070
    18:10:28:831 root: Connected to bootstrap at: 127.0.0.1:8000
    FUSE: Interface thread started
    FUSE: Open pipe  

* On the third terminal window run ``VIN -n -a 127.0.0.1 -h 7071 -p 8081 -r 9091``. Note that the HTTP, data and receipt ports are different than the node which was first instantiated. This peer will be the ``receiver`` peer for this example.

.. admonition:: VIN™ Receiver Peer Connection Output
  :class: admonition-vin-run

  .. code-block:: none

    user@vin1:~$ VIN -n -a 127.0.0.1 -h 7071 -p 8081 -r 9091
    18:13:56:809 benc: VIN
    18:13:56:809 benc: Version:    1.12.3
    18:13:56:809 benc: Git branch: HEAD - da8fd80c
    18:13:56:809 benc: Compiled:   Apr  7 2022 , 15:28:19
    18:13:56:809 benc: Log files:  LOG_07C8F_*
    LVMLibrary initialize_library...
    18:13:56:910 root: VIN initializing...
    BuiltinLvmUDPClient.pl library loaded.

    Logical Virtual Machine (LVM)
    GraphStax (c) 2019-2021
    compiled 07:56:17 Dec 22 2021
    git WindowsDev - 94d910fc

    system.pl library loaded.

    18:13:56:937 root: License validated
    18:13:56:937 root: Using HTTP port: 7071
    18:13:56:937 root: Recconnect time (s): 60
    18:13:56:937 root: VIN as node PID: 31887 , 0x07C8F
    18:13:56:940 root: Node port:  8081
    18:13:56:940 root: HTTP port:  7071
    18:13:56:940 root: Recp port:  9091
    18:13:56:940 root: Bootstrap:  127.0.0.1:8000
    18:13:56:940 root: Chunk size: 1500
    18:13:56:941 root: Redundancy: 5
    18:13:56:938 fuse: Initializing fuse peer defaults
    Initializing subsystem: Logging Subsystem
    18:13:56:944 root: Kademlia - peerless engine created (0.0.0.0:8081, :::8081)
    18:13:56:944 root: Connecting to bootstrap peer at: 127.0.0.1
    18:13:57:194 root: Initialized.Ready.
    18:13:57:305 root: Receipt server starting ( port: 9091 )...
    18:13:57:305 root: VIN node started. port: 8081 ;receipt port: 9091 ;http port: 7071
    18:13:57:306 root: Connected to bootstrap at: 127.0.0.1:8000
    FUSE: Interface thread started
    FUSE: Open pipe

* On the fourth terminal window run ``VIN_CLI 127.0.0.1 7070``. This will successfully launch the *VIN™ CLI* and connect it to the ``sender`` peer with the HTTP port of ``7070``. If everything is working correctly, the terminal window should contain the following:

.. admonition:: VIN™ CLI Connection Output
  :class: admonition-vin-run

  :bold-underline-admonition:`VIN™ CLI Output`

  .. code-block:: none

    user@vin1:~$ VIN_CLI 127.0.0.1 7070
    connecting to 127.0.0.1:7070 with timeout: 100 seconds
    Server pong!
    Connected!

  :bold-underline-admonition:`Sender Peer Output`

  .. code-block:: none

    18:15:28:353 http: URI: /ping? ; request from: 127.0.0.1:50018


Network Interaction on a Single Host Machine
------------------------------------------------

Put and Get A Key-Value Pair
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following will showcase how to a put key-value pair onto the network as a simple test to ensure the functionality of the *VIN™*. 

* To put a key-value onto the network, in the *VIN™ CLI* terminal window run ``put <key> <value>``; where ``<key>`` and ``<value>`` can be any string that does not contain spaces. For this example ``test_key`` was used for the ``<key>`` and ``test_value`` for the ``<value>``. The following figure displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the peer.


.. admonition:: Successful Put Output
  :class: admonition-vin-run

  :bold-underline-admonition:`VIN™ CLI Output`

  .. code-block:: none

    VIN@127.0.0.1:7070> put test_key test_value
    Sending payload:
    {"key":"test_key","value":"test_value"}

    Waiting for response...
    Status : 200
    Reason : 'putValue' successful:  Key: test_key ; Value: test_value
    Response received

    [test_key]:test_value   put successfully

  :bold-underline-admonition:`Sender Peer Output`

  .. code-block:: none

    18:29:03:041 http: URI: /putValue ; request from: 127.0.0.1:51072
    18:29:03:041 http: 'putValue' request received
    18:29:03:041 http: 'putValue' successful:  Key: test_key ; Value: test_value
    18:29:03:041 benc: 'putValue' request latency 0 min 0 sec 0 msec


* To view the value that was placed on the *Kademlia* network, navigate to ``/opt/VIN/kademlia/data/`` and proceed through the folder structure.
* To get a value from the network, in the *VIN™ CLI* terminal window run ``get <key>``; where ``<key>`` is ``test_key`` for this example. The following displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the ``sender`` peer.

.. admonition:: Successful Get Output
  :class: admonition-vin-run

  :bold-underline-admonition:`VIN™ CLI Output`

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

  :bold-underline-admonition:`Sender Peer Output`

  .. code-block:: none

    18:53:04:111 http: URI: /getValue ; request from: 127.0.0.1:51076
    18:53:04:111 http: 'getValue' request received
    18:53:04:111 http: 'getValue' successful:  Key: test_key ; Value: test_value
    18:53:04:112 benc: 'getValue' request latency 0 min 0 sec 0 msec



Spread and Gather a File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *VIN™* can spread any file type onto its network. To do a ``spread`` with its default configuration (see :ref:`vin-configuration` and :ref:`vin-cli` for more details), perform the following:

* In the *VIN™ CLI* terminal window run ``spread <filepath>``; where the ``<filepath>`` is the absolute (or relative) path and name of the file to be spread. For this example, it is ``/home/user/Dev/vin_test.txt``. For all of the options available to ``spread``, refer to :ref:`vin-cli`. An encrypted cryptographic receipt is generated upon spreading and is stored in ``/opt/VIN/receipts/sent/`` and the encrypted data is placed onto the *Kademlia* network and can be seen in ``/opt/VIN/kademlia/data/``. Additionally, the data, broken into shards, is viewable in ``/var/log/VIN/shards/``. Note: the number of shards is dependant on the size of the file and the parameters set in the ``chunker`` object, which is set in ``defaults.cfg`` (see :ref:`vin-configuration` for more details).
* The output of a successful ``spread`` is shown below.

.. admonition:: Successful Spread Output
  :class: admonition-vin-run

  :bold-underline-admonition:`VIN™ CLI Output`

  .. code-block:: none

    VIN@127.0.0.1:7070> spread /home/user/Dev/vin_test.txt

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File spread successfully

    Receipt saved to location : /opt/VIN/receipts/sent/CR1299958208

  :bold-underline-admonition:`Sender Peer Output`

  .. code-block:: none

    18:56:39:390 http: URI: /spread ; request from: 127.0.0.1:51078
    18:56:39:390 http: 'spread' request received
    18:56:39:391 root: Using default coders pipeline
    18:56:39:391 root: Validate encoders...
    18:56:39:391 root: Enc: ConcurrentEncoder EntanglementEncoder NamingEncoder ValidationEncoder
    18:56:39:391 root: Validate decoders...
    18:56:39:391 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    18:56:39:391 root: Validate channels...
    18:56:39:391 root: No channels specified
    18:56:39:391 root: Logging pre-encoded file
    18:56:39:392 root: Encoding
    18:56:39:391 benc: 'spread' chunking latency 0 min 0 sec 0 msec
    18:56:39:391 benc: 'spread' file: vin_test.txt size: 27
    18:56:39:395 benc: 'spread' encoding latency 0 min 0 sec 3 msec
    18:56:39:395 enco: ConcurrentEncoder: avg marks: 1017
    18:56:39:871 benc: Found: 3 peers
    Job Watchdog (0): Job finished signal received
    Job Watchdog (0): Tasks (Processing 0, Pending 0)
    18:56:39:872 http: 'spread' receipt saved to: /opt/VIN/receipts/sent/CR1299958208
    18:56:39:872 benc: 'spread' uploading latency 0 min 0 sec 476 msec
    18:56:39:872 benc: 'spread' total latency 0 min 0 sec 480 msec
    18:56:39:872 benc: 'spread' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    18:56:39:872 benc: 'spread' system data size:  20480 ( redundancy = 5 )


* After a file has been spread to the network a cryptographic receipt will be generated on the ``sender`` peer with the path and filename listed in the ``sender`` peers terminal output (for this example it is ``/opt/VIN/receipts/sent/CR1299958208``). Using this receipt, the file can be retrieved from the network via the ``gather`` command. To do a ``gather`` with its default configuration, in the *VIN™ CLI* terminal window run ``gather <receipt_path>`` where the ``<receipt_path>`` is ``/opt/VIN/receipts/sent/CR1299958208``. For all of the options available to ``gather``, refer to :ref:`vin-cli`. If the file was successfully gathered, the following output should be displayed.

.. admonition:: Successful Gather Output
  :class: admonition-vin-run

  :bold-underline-admonition:`VIN™ CLI Output`

  .. code-block:: none
    
    VIN@127.0.0.1:7070> gather /opt/VIN/receipts/sent/CR1299958208

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File gathered successfully

    File reconstructed at : /opt/VIN/outputs/vin_test/vin_test.txt on node host.
    

  :bold-underline-admonition:`Sender Peer Output`

  .. code-block:: none
    
    19:01:24:611 http: URI: /gather ; request from: 127.0.0.1:51080
    19:01:24:611 http: 'gather' request received
    19:01:24:612 benc: 'gather' file: vin_test.txt size: 27
    19:01:24:612 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    Job Watchdog (0): Job finished signal received
    Job Watchdog (0): Tasks (Processing 0, Pending 0)
    19:01:24:614 benc: 'gather' acquisition latency 0 min 0 sec 2 msec
    19:01:24:614 benc: 'gather' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    19:01:24:614 root: Decoding
    19:01:24:621 benc: 'gather' decoding latency 0 min 0 sec 7 msec
    19:01:24:622 benc: 'gather' total latency 0 min 0 sec 9 msec
    19:01:24:623 root: File rebuild at: /opt/VIN/outputs/vin_test/vin_test.txt


* To inspect the gathered file, navigate to ``/opt/VIN/outputs/`` and enter ``ls``. A folder with the name of the file which was gathered should be listed. Enter this folder (``cd <folder_name>``) and run ``ls``. The file which was shared will be displayed and can be inspected to ensure it was successfully gathered. 
* Note: the ``gather`` command, by default, will create a new file on the system after it finishes; thus, the gathered file may have a number appended to end of the filename if spread more than once. For more information on how to overwrite the file, or append to its contents, refer to the :ref:`vincli-commands` table.


Share a File
^^^^^^^^^^^^^^^^^^

The following will describe how to do a ``share`` with its default configuration (see :ref:`vin-configuration` and :ref:`vin-cli` for more details).

* In the *VIN™ CLI* terminal window, the following command should be run after the required information is determined: ``share <filepath> <ip_address> <receipt_port>``. ``<filepath>`` is the path and filename of the file to be shared, for example, in this case it is ``/home/user/Dev/vin_test.txt``. Note: any file type can be shared. The ``<ip_address>`` and ``<receipt_port>`` are ``127.0.0.1`` and ``9091``, or the IP address of the host system and the ``receipt_port`` of the second peer running on it.
* Thus, the command to run, for this example, becomes ``share /home/user/Dev/vin_test.txt 127.0.0.1 9091``. For all of the options available to ``share``, refer to :ref:`vin-cli`. If everything worked correctly, the following should be displayed: 

.. admonition:: Successful Share Output
  :class: admonition-vin-run

  :bold-underline-admonition:`VIN™ CLI Output`

  .. code-block:: none

    share /home/user/Dev/vin_test.txt 127.0.0.1 9091

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File shared to 127.0.0.1 9091 successfully (run: 1)

  :bold-underline-admonition:`Sender Peer Output`

  .. code-block:: none

    19:06:55:723 http: URI: /share ; request from: 127.0.0.1:51082
    19:06:55:723 http: 'share' request received
    19:06:55:723 root: Using default coders pipeline
    19:06:55:723 benc: 'share' chunking latency 0 min 0 sec 0 msec
    19:06:55:723 http: Share to: 127.0.0.1:9091 ; File: vin_test.txt ; Size: 27 ; Flag: create
    19:06:55:723 root: Validate encoders...
    19:06:55:723 root: Enc: ConcurrentEncoder EntanglementEncoder NamingEncoder ValidationEncoder
    19:06:55:723 root: Validate decoders...
    19:06:55:723 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    19:06:55:723 root: Validate channels...
    19:06:55:723 root: No channels specified
    19:06:55:723 root: Logging pre-encoded file
    19:06:55:724 root: Encoding
    19:06:55:723 benc: 'spread' file: vin_test.txt size: 27
    19:06:55:726 enco: ConcurrentEncoder: avg marks: 1017
    19:06:55:727 benc: 'spread' encoding latency 0 min 0 sec 3 msec
    Job Watchdog (0): Job finished signal received
    Job Watchdog (0): Tasks (Processing 0, Pending 0)
    19:06:55:962 benc: 'spread' uploading latency 0 min 0 sec 235 msec
    19:06:55:962 benc: 'spread' total latency 0 min 0 sec 238 msec
    19:06:55:962 benc: 'spread' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    19:06:55:962 benc: 'spread' system data size:  20480 ( redundancy = 5 )
    19:06:55:962 root: Sharing to peer: 127.0.0.1:9091
    19:06:55:969 root: Receipt session started
    19:06:55:969 root: Connected to peer: 127.0.0.1:9091
    19:06:55:970 root: Session token obtained
    19:06:55:970 root: Sending receipt
    19:06:56:981 root: Sending status request
    19:06:56:983 root: Status: File rebuild OK
    19:06:56:983 root: Sharing end session
    19:06:56:983 benc: 'share' receipt latency 0 min 1 sec 20 msec
    19:06:56:983 benc: 'share' encoded data size: 4096
    19:06:56:983 benc: 'share' system data size:  20480 ( redundancy = 5 )
    19:06:56:983 benc: 'share' total latency 0 min 1 sec 260 msec

  :bold-underline-admonition:`Receiver Peer Output`

  .. code-block:: none

    19:06:55:963 benc: Share session created. Peer addr: 127.0.0.1:43648
    19:06:55:971 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    19:06:55:971 benc: 'gather' file: vin_test.txt size: 27
    19:06:55:970 cr-s: Start sharing session
    19:06:55:970 cr-s: Send session id
    19:06:55:971 cr-s: Receipt received from: 127.0.0.1:43648
    Job Watchdog (110): Tasks (Processing 0, Pending 0)
    19:06:56:973 benc: 'gather' acquisition latency 0 min 1 sec 1 msec
    19:06:56:973 benc: 'gather' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    19:06:56:973 root: Decoding
    19:06:56:980 benc: 'gather' decoding latency 0 min 0 sec 7 msec
    19:06:56:980 benc: 'gather' total latency 0 min 1 sec 9 msec
    19:06:56:981 cr-s: Status request from: 127.0.0.1:43648
    19:06:56:982 benc: 'gather' end_stream_session
    19:06:56:982 root: File rebuild at: /opt/VIN/outputs/vin_test/vin_test(1).txt
    19:06:56:982 benc: 'gather' rebuilt latency: 0 min 0 sec 0 msec
    19:06:56:984 cr-s: Status: File rebuild OK
    19:06:56:984 cr-s: Share ended. 0 min 1 sec 21 msec
    19:06:57:035 cr-s: Connection with peer: 127.0.0.1:43648 ended

* To manually confirm that the file was shared correctly, enter ``ls`` in a terminal window pointing to the ``/opt/VIN/outputs/`` folder directory. A folder with the name of the file which was shared should be listed. Enter this folder (``cd <folder_name>``) and run ``ls``. The file which was shared will be displayed and can be inspected to ensure it was successfully shared.
* Note the ``(1)`` added to the the reconstructed file name ``vin_test(1).txt`` in the above output. As a ``share`` with a default configuration was performed, a copy of the file that was spread in the above example was created. To overwrite, append to the existing, or create a new file, ad for all other options for ``share`` refer to the available options in the :ref:`vin-cli` section. 
* Additionally, the cryptographic receipt for the share is stored in ``/opt/VIN/receipts/sent/``, the encrypted data can be seen in ``/opt/VIN/kademlia/data/``, and the sharded data is viewable in ``/var/log/VIN/shards/``. Note: the number of shards is dependant on the size of the file and the parameters set in the ``chunker`` object, which is set in ``defaults.cfg`` (see :ref:`vin-configuration` for more details).


Getting the available Peers on the Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the *VIN™ CLI* terminal window connected to the ``sender`` peer, run ``getPeers`` to generate a list of all peers available to the ``sender`` peer. The result will be an output similar to the one displayed in the figure below.  

.. admonition:: Successful GetPeers Output
  :class: admonition-vin-run

  :bold-underline-admonition:`VIN™ CLI Output`

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

  :bold-underline-admonition:`Sender Peer Output`

  .. code-block:: none

    20:27:00:685 http: URI: /getPeers ; request from: 127.0.0.1:51118
    20:27:00:685 http: 'getPeers' request received
    20:27:00:947 benc: Found: 3 peers
    20:27:00:948 http: Listing peer: 127.0.0.1:8000
    20:27:00:948 http: MetaData: {}
    20:27:00:948 http: Listing peer: 127.0.0.1:8081
    20:27:00:948 http: MetaData: {"kad_port":"8081","receipt_port":"9091","http_port":"7071"}


As two peers (the bootstrap and the ``receiver`` peer) are connected to ``sender`` peer, the result contain two outputs. The first listed is the bootstrap (``127.0.0.1:8000``), while the second is the ``receiver`` peer (``127.0.0.1:8081``). Note how the ``receiver`` peer contains additional port information which was supplied during its instantiation.


Shutting Down the Network
"""""""""""""""""""""""""

* Press **ctrl + c** while the bootstrap node's terminal window is active to stop the process.

.. admonition:: Bootstrap Shutdown Output
  :class: admonition-vin-run

  .. code-block:: none
    
    20:33:25:500 root: VIN exit

* To shutdown a peer node which is connected to the *VIN™ CLI*, run ``shutdown`` in the *VIN™ CLI* terminal window connected to the peer. Alternatively, press **ctrl + c** while the peer node's terminal window is active to end the process.

.. admonition:: Sender Peer Shutdown Output
  :class: admonition-vin-run

  :bold-underline-admonition:`VIN™ CLI Output`

  .. code-block:: none
    
    VIN@127.0.0.1:7070> shutdown
    <h1>Exit<h1>

  :bold-underline-admonition:`Sender Peer Output`

  .. code-block:: none

    20:34:51:455 http: URI: /exit ; request from: 127.0.0.1:51120
    20:34:51:455 http: 'exit' request received
    20:34:51:455 http: HTTP server exit
    Uninitializing subsystem: Logging SubsystemFUSE: Handle end thread signal 10
  
    20:34:55:871 root: VIN exit


* Press **ctrl + c** while the peer node's terminal window is active to kill the process.

.. admonition:: Receiver Peer Shutdown Output
  :class: admonition-vin-run

  .. code-block:: none

    20:36:16:654 http: HTTP server exit


* To exit from the *VIN™ CLI*, type **exit** and hit **enter** in the *VIN™ CLI* terminal window. Alternatively, **ctrl + c** may be pressed.

.. admonition:: VIN™ CLI Shutdown Output
  :class: admonition-vin-run

  .. code-block:: none
    
    VIN@127.0.0.1:7070> exit
    So long for now.


--------------------------------------------------------------------

.. _vin-local-network-linux:


Setting up the VIN™ on a Local Network 
===========================================

To run the *VIN™* on an IP based network, such as *Amazon Web Services (AWS)*, a Local Area Network (LAN) with routers/switches and Dynamic Host Communication Protocol (DHCP), *VMware*, etc., complete the following steps:

* For this example, two systems will be used: ``system_1`` and ``system_2``.
* Complete the *VIN™* installation procedure on each system (refer to :ref:`vin-install`).
* On each system, open three terminal windows. 
* Since each system will have it's own IP address, deemed ``<ip_1>`` and ``<ip_2>`` for this example, it is imperative to determine and record them.
* Run ``ifconfig`` in one of the terminal windows. Note: if this feature is not installed a message will appear recommending that ``sudo apt-get install -y net-tools`` be run. If this is the case, run this command and re-run ``ifconfig`` to generate an output similar to the one below. 
  

.. admonition:: System 1 ifconfig Output
  :class: admonition-vin-run

  .. code-block:: none

    user@vin1:~$ ifconfig
    eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 10.51.2.21  netmask 255.255.255.0  broadcast 10.51.2.255
            inet6 fe80::ff:fe38:e  prefixlen 64  scopeid 0x20<link>
            ether 02:00:00:38:00:0e  txqueuelen 1000  (Ethernet)
            RX packets 604704  bytes 444718362 (444.7 MB)
            RX errors 0  dropped 1  overruns 0  frame 0
            TX packets 115106  bytes 13463699 (13.4 MB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 2300  bytes 277149 (277.1 KB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 2300  bytes 277149 (277.1 KB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


* Record the address next to the ``inet`` parameter for the required network connection (i.e., wired or wireless). From the output above, the ``inet`` value of ``10.51.2.21`` corresponds to an ethernet connection, ``eth0``, and was recorded as ``<ip_1>``.
* Repeat the above instructions for ``system_2`` and record ``<ip_2>`` (for this example it is ``10.51.2.22``).
* In one of the terminal windows on ``system_1`` run ``VIN -b <ip_1>``. For this example, ``<ip_1>`` is ``10.51.2.21``. This will serve as the bootstrap node and will occupy port ``8000`` for incoming connections. If the bootstrap was successfully launched, its terminal window will output similar results to those below.


.. admonition:: System 1 Bootstrap Connection Output 
  :class: admonition-vin-run

  .. code-block:: none

    user@vin1:~$ VIN -b 10.51.2.21
    15:58:07:277 benc: VIN
    15:58:07:277 benc: Version:    1.12.3
    15:58:07:277 benc: Git branch: HEAD - da8fd80c
    15:58:07:277 benc: Compiled:   Apr  7 2022 , 15:28:19
    15:58:07:277 benc: Log files:  LOG_09301_*
    15:58:07:378 root: VIN initializing...
    LVMLibrary initialize_library...
    BuiltinLvmUDPClient.pl library loaded.

    Logical Virtual Machine (LVM)
    GraphStax (c) 2019-2021
    compiled 07:56:17 Dec 22 2021
    git WindowsDev - 94d910fc

    system.pl library loaded.

    15:58:07:412 root: License validated
    15:58:07:413 root: Recconnect time (s): 60
    15:58:07:413 root: VIN as bootstrap PID: 37633 , 0x09301
    15:58:07:413 root: Machine name: vin1 Available IPs:
    15:58:07:413 root: IP: 127.0.1.1
    15:58:07:514 root: Kademlia - peerless engine created (0.0.0.0:8000, :::8000)
    15:58:07:624 root: VIN bootstrap node started at: 0.0.0.0:8000


* In another terminal window on ``system_1``, run ``VIN -n -a <ip_1> -h 7070 -p 8080 -r 9090``. This will start a *VIN™* peer node with an HTTP port of ``7080``, a data (*Kademlia*) port of ``8080`` and a receipt server port of ``9090`` and connect to the bootstrap on ``<ip_1>``. Note: these ports can be chosen based on the requirements/restrictions of the user. 
* If the peer connects to the bootstrap successfully, the terminal window will contain a similar output to the one below. Take note that it displays the ports and IP address that was used during the peer's instantiation.

.. admonition:: System 1 VIN™ Peer Connection Output
  :class: admonition-vin-run

  .. code-block:: none    

    user@vin1:~$ VIN -n -a 10.51.2.21 -h 7070 -p 8080 -r 9090
    16:02:23:352 benc: VIN
    16:02:23:352 benc: Version:    1.12.3
    16:02:23:352 benc: Git branch: HEAD - da8fd80c
    16:02:23:352 benc: Compiled:   Apr  7 2022 , 15:28:19
    16:02:23:352 benc: Log files:  LOG_09307_*
    LVMLibrary initialize_library...
    16:02:23:452 root: VIN initializing...
    BuiltinLvmUDPClient.pl library loaded.

    Logical Virtual Machine (LVM)
    GraphStax (c) 2019-2021
    compiled 07:56:17 Dec 22 2021
    git WindowsDev - 94d910fc

    system.pl library loaded.

    16:02:23:484 root: License validated
    16:02:23:485 root: Using HTTP port: 7070
    16:02:23:485 root: Recconnect time (s): 60
    16:02:23:485 root: VIN as node PID: 37639 , 0x09307
    16:02:23:486 fuse: Initializing fuse peer defaults
    Initializing subsystem: Logging Subsystem
    16:02:23:495 root: Node port:  8080
    16:02:23:496 root: HTTP port:  7070
    16:02:23:496 root: Recp port:  9090
    16:02:23:496 root: Bootstrap:  10.51.2.21:8000
    16:02:23:496 root: Chunk size: 1500
    16:02:23:496 root: Redundancy: 5
    16:02:23:499 root: Kademlia - peerless engine created (0.0.0.0:8080, :::8080)
    16:02:23:499 root: Connecting to bootstrap peer at: 10.51.2.21
    16:02:23:715 root: Initialized.Ready.
    16:02:23:826 root: Receipt server starting ( port: 9090 )...
    16:02:23:826 root: VIN node started. port: 8080 ;receipt port: 9090 ;http port: 7070
    16:02:23:827 root: Connected to bootstrap at: 10.51.2.21:8000
    FUSE: Interface thread started
    FUSE: Open pipe


* In the third terminal window on ``system_1``, run ``VIN_CLI <ip_1> 7070``. This will launch the *VIN™ CLI* if the above steps were completed successfully. If everything is working correctly, the terminal windows should contain the following:

.. admonition:: System 1 VIN™ CLI Connection Output
  :class: admonition-vin-run

  :bold-underline-admonition:`System 1 VIN™ CLI Output`

  .. code-block:: none

    user@vin1:~$ VIN_CLI 10.51.2.21 7070
    connecting to 10.51.2.21:7070 with timeout: 100 seconds
    Server pong!
    Connected!

  :bold-underline-admonition:`System 1 Peer Output`

  .. code-block:: none

    16:06:28:353 http: URI: /ping? ; request from: 10.51.2.21:38238

* In one of the terminal windows on ``system_2`` run ``VIN -n -a <ip_1> -h 7070 -p 8080 -r 9090``, where ``<ip_1>`` is ``10.51.2.21`` for this example. This will connect to the bootstrap located on ``system_1`` with its IP address of ``<ip_1>``.
* In the second terminal window, run ``VIN_CLI <ip_2> 7070`` to connect to the peer on ``system_2`` using ``<ip_2>`` (or ``10.51.2.22`` for this example).  
* In the final terminal window, navigate to ``/opt/VIN/outputs/``. This directory will contain the received file after it has been reconstructed during the example in the following section. 


Network Interaction on a Local Network 
-------------------------------------------

With *VIN™* peers successfully running on both systems, a number of commands can be entered to interact with the instantiated network and between the peers themselves. The following examples will highlight the use of the ``put``, ``get``, ``share``, ``spread``, ``gather``, ``getPeers`` and ``shutdown`` commands with the *VIN™ CLI*. For a full list of the *VIN™ CLI's* functionality refer to :ref:`vin-cli`. Additionally, refer to :ref:`vin-configuration` for more information regarding locations of files generated while using the *VIN™ CLI*.


Put and Get A Key-Value Pair
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following will showcase how to a put a key-value pair onto the network. While the *VIN™ CLI* connected to the peer on ``system_1`` will be utilized for the ``put``, any peer connected to a *VIN™ CLI* has this capability. 

* To put a key-value pair onto the network, in the *VIN™ CLI* terminal window on ``system_1``, run ``put <key> <value>``; where ``<key>`` and ``<value>`` can be any string that does not contain spaces. For this example ``test_key`` was used for the ``<key>`` and ``test_value`` for the ``<value>``. The following figure displays the result of running this command; where the top image is the output from the *VIN™ CLI* and the bottom is from the peer.


.. admonition:: Successful Put Output
  :class: admonition-vin-run

  :bold-underline-admonition:`System 1 VIN™ CLI Output`

  .. code-block:: none

    VIN@10.51.2.21:7070> put test_key test_value
    Sending payload:
    {"key":"test_key","value":"test_value"}

    Waiting for response...
    Status : 200
    Reason : 'putValue' successful:  Key: test_key ; Value: test_value
    Response received

    [test_key]:test_value   put successfully

  :bold-underline-admonition:`System 1 Peer Output`

  .. code-block:: none

    16:16:32:130 http: URI: /putValue ; request from: 10.51.2.21:38240
    16:16:32:130 http: 'putValue' request received
    16:16:32:130 http: 'putValue' successful:  Key: test_key ; Value: test_value
    16:16:32:130 benc: 'putValue' request latency 0 min 0 sec 0 msec


* To view the value that was placed on the *Kademlia* network, navigate to ``/opt/VIN/kademlia/data/`` and proceed through the folder structure until reaching the file.
* To get a value from the network, in the *VIN™ CLI* terminal window on ``system_2``, run ``get <key>``; where ``<key>`` is ``test_key`` for this example. The following output displays the result of running this command.

.. admonition:: Successful Get Output
  :class: admonition-vin-run

  :bold-underline-admonition:`System 2 VIN™ CLI Output`

  .. code-block:: none

    VIN@10.51.2.22:7070> get test_key
    Sending payload:
    {"key":"test_key"}

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    value for test_key got successfully

    [test_key]:test_value  is a valid [key]:value pair

  :bold-underline-admonition:`System 2 Peer Output`

  .. code-block:: none

    16:23:19:911 http: URI: /getValue ; request from: 10.51.2.22:45704
    16:23:19:911 http: 'getValue' request received
    16:23:19:912 benc: 'getValue' request latency 0 min 0 sec 1 msec
    16:23:19:912 http: 'getValue' successful:  Key: test_key ; Value: test_value



Spread and Gather a File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *VIN™* can spread any file type onto its network. To do a ``spread`` with its default configuration (see :ref:`vin-configuration` and :ref:`vin-cli` for more details), perform the following:

* In the *VIN™ CLI* terminal window on ``system_`1`` run ``spread <filepath>``; where the ``<filepath>`` is the path and name of the file to be spread. For this example, it is ``/home/user/Dev/vin_network_test.txt``. For all of the options available to ``spread``, refer to :ref:`vin-cli`. An encrypted cryptographic receipt is generated upon spreading and is stored in ``/opt/VIN/receipts/sent/`` and the encrypted data is placed onto the *Kademlia* network and can be seen in ``/opt/VIN/kademlia/data/``. Additionally, the data, broken into shards, is viewable in ``/var/log/VIN/shards/``. Note: the number of shards is dependant on the size of the file and the parameters set in the ``chunker`` object, which is set in ``defaults.cfg`` (see :ref:`vin-configuration` for more details).
* The output of a successful ``spread`` is shown below.

.. admonition:: Successful Spread Output
  :class: admonition-vin-run

  :bold-underline-admonition:`System 1 VIN™ CLI Output`

  .. code-block:: none

    VIN@10.51.2.21:7070> spread /home/user/Dev/vin_network_test.txt

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File spread successfully

    Receipt saved to location : /opt/VIN/receipts/sent/CR1637078311

  :bold-underline-admonition:`System 1 Peer Output`

  .. code-block:: none

    16:35:19:866 http: URI: /spread ; request from: 10.51.2.21:38242
    16:35:19:866 http: 'spread' request received
    16:35:19:866 root: Using default coders pipeline
    16:35:19:866 benc: 'spread' chunking latency 0 min 0 sec 0 msec
    16:35:19:867 root: Validate encoders...
    16:35:19:867 root: Enc: ConcurrentEncoder EntanglementEncoder NamingEncoder ValidationEncoder
    16:35:19:867 root: Validate decoders...
    16:35:19:867 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    16:35:19:867 root: Validate channels...
    16:35:19:867 root: No channels specified
    16:35:19:867 benc: 'spread' file: vin_test.txt size: 27
    16:35:19:868 root: Logging pre-encoded file
    16:35:19:868 root: Encoding
    16:35:19:870 benc: 'spread' encoding latency 0 min 0 sec 2 msec
    16:35:19:870 enco: ConcurrentEncoder: avg marks: 1017
    16:35:19:974 benc: Found: 3 peers
    Job Watchdog (0): Job finished signal received
    Job Watchdog (0): Tasks (Processing 0, Pending 0)
    16:35:19:975 benc: 'spread' uploading latency 0 min 0 sec 104 msec
    16:35:19:975 benc: 'spread' total latency 0 min 0 sec 107 msec
    16:35:19:975 benc: 'spread' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    16:35:19:975 benc: 'spread' system data size:  20480 ( redundancy = 5 )
    16:35:19:975 http: 'spread' receipt saved to: /opt/VIN/receipts/sent/CR1637078311


* After a file has been spread to the network a cryptographic receipt will be generated as is shown in the ``system_1`` output. Using this receipt, the file can be retrieved from the network via the ``gather`` command. However, the receipt is located on ``system_1`` (the system which did the spread), and ``system_2`` will need to have access to it. Therefore it must be copied to that system before a ``gather`` from ``system_2`` can be complete.
* With the cryptographic receipt copied, to do a ``gather``, in the *VIN™ CLI* terminal window on ``system_2`` run ``gather <receipt_path>``. The ``<receipt_path>`` for this example is ``/opt/VIN/receipts/received/CR1637078311``. For all of the options available to ``gather``, refer to :ref:`vin-cli`. If the file was successfully gathered, the following output should be displayed.

.. admonition:: Successful Gather Output
  :class: admonition-vin-run

  :bold-underline-admonition:`System 2 VIN™ CLI Output`

  .. code-block:: none
    
    VIN@10.51.2.22:7070> gather /opt/VIN/receipts/received/CR1637078311

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File gathered successfully

    File reconstructed at : /opt/VIN/outputs/vin_network_test/vin_network_test.txt on node host.

  :bold-underline-admonition:`System 2 Peer Output`

  .. code-block:: none
    
    gather /opt/VIN/receipts/received/CR1637078311

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File gathered successfully

    File reconstructed at : /opt/VIN/outputs/vin_network_test/vin_network_test.txt on node host.
   

* To inspect the gathered file, refer to the folder ``/opt/VIN/outputs/`` and enter ``ls``. A folder with the name of the file which was gathered should be listed. Enter this folder (``cd <folder_name>``) and run ``ls``. The file which was shared will be displayed and can be inspected to ensure it was successfully gathered. 
* Note: the ``gather`` command, by default, will create a new file on the system after it finishes; thus, the gathered file may have a number appended to end of the filename. For more information on how to overwrite the file, or append to its contents, refer to the :ref:`vincli-commands` table.


Share a File
^^^^^^^^^^^^^^^^

The following will describe how to share files between the peer on ``system_1`` to the peer located on ``system_2``. Note: the peer/*VIN™ CLI* connection on ``system_2`` could also be used to perform the share.

* In the *VIN™ CLI* terminal window on ``system_1``, the following command should be run after the required information is determined: ``share <filepath> <ip_address> <receipt_port>``. ``<filepath>`` is the path and filename of the file to be shared, for example, in this case it is ``/home/user/Dev/vin_network_test.txt``. Note: any file type can be shared. The ``<ip_address>`` and ``<receipt_port>`` are ``<ip_2>`` (or ``10.51.2.22`` for this example) and ``9090``, or the IP address of ``system_2`` and the ``receipt_port`` of the peer running on it.
* Thus, the command to run, for this example, becomes ``share /home/user/Dev/vin_network_test.txt 10.51.2.22 9090``. If everything worked correctly, the following should be displayed on ``system_1`` and ``system_2``. 

.. admonition:: Successful Share Output
  :class: admonition-vin-run

  :bold-underline-admonition:`System 1 VIN™ CLI Output`

  .. code-block:: none

    VIN@10.51.2.21:7070> share /home/user/Dev/vin_network_test.txt 10.51.2.22 9090

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    File shared to 10.51.2.22 9090 successfully (run: 1)
    

  :bold-underline-admonition:`System 1 Peer Output`

  .. code-block:: none

    18:06:42:094 http: URI: /share ; request from: 10.51.2.21:38262
    18:06:42:094 http: 'share' request received
    18:06:42:094 http: Share to: 10.51.2.22:9090 ; File: vin_network_test.txt ; Size: 27 ; Flag: create
    18:06:42:094 benc: 'share' chunking latency 0 min 0 sec 0 msec
    18:06:42:094 root: Using default coders pipeline
    18:06:42:095 root: Validate encoders...
    18:06:42:095 root: Enc: ConcurrentEncoder EntanglementEncoder NamingEncoder ValidationEncoder
    18:06:42:095 root: Validate decoders...
    18:06:42:095 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    18:06:42:095 root: Validate channels...
    18:06:42:095 root: No channels specified
    18:06:42:096 benc: 'spread' file: vin_test.txt size: 27
    18:06:42:096 root: Logging pre-encoded file
    18:06:42:096 root: Encoding
    18:06:42:098 benc: 'spread' encoding latency 0 min 0 sec 2 msec
    18:06:42:098 enco: ConcurrentEncoder: avg marks: 1017
    18:06:42:391 benc: Found: 3 peers
    Job Watchdog (0): Job finished signal received
    Job Watchdog (0): Tasks (Processing 0, Pending 0)
    18:06:42:391 benc: 'spread' uploading latency 0 min 0 sec 292 msec
    18:06:42:392 benc: 'spread' total latency 0 min 0 sec 296 msec
    18:06:42:392 benc: 'spread' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    18:06:42:392 benc: 'spread' system data size:  20480 ( redundancy = 5 )
    18:06:42:392 root: Sharing to peer: 10.51.2.22:9090
    18:06:42:399 root: Receipt session started
    18:06:42:399 root: Connected to peer: 10.51.2.22:9090
    18:06:42:399 root: Session token obtained
    18:06:42:400 root: Sending receipt
    18:06:42:412 root: Sending status request
    18:06:42:414 root: Status: File rebuild OK
    18:06:42:414 root: Sharing end session
    18:06:42:414 benc: 'share' receipt latency 0 min 0 sec 22 msec
    18:06:42:415 benc: 'share' encoded data size: 4096
    18:06:42:415 benc: 'share' system data size:  20480 ( redundancy = 5 )
    18:06:42:415 benc: 'share' total latency 0 min 0 sec 321 msec


  :bold-underline-admonition:`System 2 Peer Output`

  .. code-block:: none

    18:06:42:383 benc: Share session created. Peer addr: 10.51.2.21:50276
    18:06:42:388 cr-s: Start sharing session
    ob Watchdog (0): Job finished signal received
    Job Watchdog (0): Tasks (Processing 0, Pending 0)
    1m18:06:42:389 cr-s: Send session id
    18:06:42:390 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
    18:06:42:390 benc: 'gather' file: vin_test.txt size: 27
    18:06:42:391 benc: 'gather' acquisition latency 0 min 0 sec 1 msec
    18:06:42:391 benc: 'gather' encoded data size: 4096  ( 1 chunks of 4096 bytes )
    18:06:42:389 cr-s: Receipt received from: 10.51.2.21:50276
    18:06:42:391 root: Decoding
    18:06:42:400 benc: 'gather' decoding latency 0 min 0 sec 8 msec
    18:06:42:401 benc: 'gather' total latency 0 min 0 sec 11 msec
    18:06:42:402 cr-s: Status request from: 10.51.2.21:50276
    18:06:42:402 benc: 'gather' end_stream_session
    18:06:42:402 root: File rebuild at: /opt/VIN/outputs/vin_network_test/vin_network_test(1).txt
    18:06:42:403 benc: 'gather' rebuilt latency: 0 min 0 sec 0 msec
    18:06:42:403 cr-s: Status: File rebuild OK
    18:06:42:404 cr-s: Share ended. 0 min 0 sec 20 msec
    18:06:42:454 cr-s: Connection with peer: 10.51.2.21:50276 ended
    


* To manually confirm that the file was shared correctly, on ``system_2`` navigate to the ``/opt/VIN/outputs/`` folder directory and enter ``ls``. A folder with the name of the file which was shared should be listed. Enter this folder (``cd <folder_name>``) and run ``ls``. The file which was shared will be displayed and can be inspected to ensure it was successfully shared.
* Note the ``(1)`` added to the the reconstructed file name ``vin_network_test(1).txt``. As a basic ``share`` was performed, a copy of the file that was spread in the above example was created. To overwrite, append to the existing, or create a new file, refer to the available options in the :ref:`vin-cli` section. The table located on this page also details all of the options available to ``share``.
* Additionally, the cryptographic receipt for the ``share`` is stored in ``/opt/VIN/receipts/sent/``, the encrypted data can be seen in ``/opt/VIN/kademlia/data/``, and the sharded data is viewable in ``/var/log/VIN/shards/``. Note: the number of shards is dependant on the size of the file and the parameters set in the ``chunker`` object, which is set in ``defaults.cfg`` (see :ref:`vin-configuration` for more details).


Getting the available Peers on the Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the *VIN™ CLI* terminal on ``system_1``, run ``getPeers`` to generate a list of all peers connected to a bootstrap node. The result will be an output similar to the one displayed in the figure below.  

.. admonition:: System 1 Successful GetPeers Output
  :class: admonition-vin-run

  :bold-underline-admonition:`System 1 VIN™ CLI Output`

  .. code-block:: none

    VIN@10.51.2.21:7070> getPeers
    Sending payload:
    {}

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    Got Peers successfully
    {
        "10.51.2.21:8000": {
            "ip": "10.51.2.21",
            "meta_data": {
            },
            "port": "8000"
        },
        "10.51.2.22:8080": {
            "ip": "10.51.2.22",
            "meta_data": {
                "http_port": "7070",
                "kad_port": "8080",
                "receipt_port": "9090"
            },
            "port": "8080"
        }
    }

  :bold-underline-admonition:`System 1 Peer Output`

  .. code-block:: none

    18:26:37:000 http: URI: /getPeers ; request from: 10.51.2.21:38266
    18:26:37:000 http: 'getPeers' request received
    18:26:37:158 http: Listing peer: 10.51.2.21:8000
    18:26:37:158 http: MetaData: {}
    18:26:37:158 http: Listing peer: 10.51.2.22:8080
    18:26:37:158 http: MetaData: {"kad_port":"8080","receipt_port":"9090","http_port":"7070"}


* As two peers (the bootstrap and the ``system_2`` peer) are connected to ``system_1`` peer, the result contain two outputs. The first listed is the bootstrap (``10.51.2.21:8000``), while the second is the ``system_2`` peer (``10.51.2.22:8080``). Note how the ``system_2`` peer contains additional port information which was supplied during its instantiation.
* In the *VIN™ CLI* terminal on ``system_2``, run ``getPeers`` to generate a list of all peers connected to a bootstrap node. The result will be an output similar to the one displayed in the figure below.  

.. admonition:: System 2 Successful GetPeers Output
  :class: admonition-vin-run

  :bold-underline-admonition:`System 2 VIN™ CLI Output`

  .. code-block:: none

    VIN@10.51.2.22:7070> getPeers
    Sending payload:
    {}

    Waiting for response...
    Status : 200
    Reason : OK
    Response received
    Got Peers successfully
    {
        "10.51.2.21:8000": {
            "ip": "10.51.2.21",
            "meta_data": {
            },
            "port": "8000"
        },
        "10.51.2.21:8080": {
            "ip": "10.51.2.21",
            "meta_data": {
                "http_port": "7070",
                "kad_port": "8080",
                "receipt_port": "9090"
            },
            "port": "8080"
        }
    }

  :bold-underline-admonition:`System 2 Peer Output`

  .. code-block:: none

    18:28:27:155 http: URI: /getPeers ; request from: 10.51.2.22:45712
    18:28:27:155 http: 'getPeers' request received
    18:28:27:396 benc: Found: 3 peers
    18:28:27:396 http: Listing peer: 10.51.2.21:8000
    18:28:27:396 http: MetaData: {}
    18:28:27:396 http: Listing peer: 10.51.2.21:8080
    18:28:27:396 http: MetaData: {"kad_port":"8080","receipt_port":"9090","http_port":"7070"}

* Once again two peers (the bootstrap and the ``system_1`` peer) are displayed in the outputs. The first listed is the bootstrap (``10.51.2.21:8000``), while the second is the ``system_1`` peer (``10.51.2.21:8080``). 

Shutting Down the Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Press **ctrl + c** while the bootstrap node's terminal window is active to stop the process.

.. admonition:: Bootstrap Shutdown Output
  :class: admonition-vin-run

  .. code-block:: none
    
    19:12:07:715 root: VIN exit

* To shutdown a peer node which is connected to the *VIN™ CLI*, run ``shutdown`` in the *VIN™ CLI* terminal window connected to the peer. Alternatively, press **ctrl + c** while the peer node's terminal window is active to end the process.

.. admonition:: System 1 Peer Shutdown Output
  :class: admonition-vin-run

  :bold-underline-admonition:`System 1 VIN™ CLI Output`

  .. code-block:: none
    
    VIN@10.51.2.21:7070> shutdown
    <h1>Exit<h1>

  :bold-underline-admonition:`System 1 Peer Output`

  .. code-block:: none

    19:12:19:418 http: URI: /exit ; request from: 10.51.2.21:38304
    19:12:19:418 http: 'exit' request received
    19:12:19:418 http: HTTP server exit
    Uninitializing subsystem: Logging SubsystemFUSE: Handle end thread signal 10

    19:12:25:348 root: VIN exit


* To exit from the *VIN™ CLI*, type **exit** and hit **enter** in the *VIN™ CLI* terminal window. Alternatively, **ctrl + c** may be pressed.

.. admonition:: System 1 VIN™ CLI Shutdown Output
  :class: admonition-vin-run

  .. code-block:: none
    
    VIN@127.0.0.1:7070> exit
    So long for now.


* The peer and *VIN™ CLI* for ``system_2`` can be shut down in the same manner listed above.