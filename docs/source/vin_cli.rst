.. _vin-cli:

***********************************
VIN™ Command Line Interface (CLI)
***********************************

*VIN™* commands are assessable through the *VIN™ Command Line Interface (CLI)* which acts as a Hypertext Transfer Protocol (HTTP) client for reaching the *VIN™* HTTP server from the command line. Note: the *VIN™ CLI* will be installed during the installation of the *VIN™*.

The following table displays a list of APIs that are accessible through the *VIN™ CLI*. For examples, and the outputs of each API, please refer to the :ref:`vin-cli-func` section.

.. _supported-commands:

.. csv-table:: VIN™ CLI Commands
    :header: Command, Command Line Instruction, Description
    :widths: 15 40 50 

    Help, help, "Displays a list of commands available to the *VIN™ CLI*."
    Exit, exit, "Quits the current session of the *VIN™ CLI*."
    Ping, ping, "Pings the connected node to check its status. The connected node responds with a 'Server pong!' message if successful."
    GetPeers, getPeers, "Get the IP addresses and data ports for all nodes connected on this network. Note: some of the nodes may be stale."
    Put, put <key> <value>, "Puts a user provided value (string) onto the network which corresponds to the user provided key (string).
    
    Example: ``put k1 v1``"
    Get, get <key>, "Requires a given key (string) and returns the Key-Value pair from the respective node. The value is displayed in the *VIN™ CLI* window. No other output is displayed.
    
    Example: ``get k1``"
    Spread, spread <filepath>, "Splits a file of any type located in a given filepath (string) into tokens and then spreads them across the network. An encrypted cryptographic receipt is then generated and stored in ``/opt/VIN/receipts/sent`` in *Linux* and ``VIN\receipts\sent\`` in *Windows*.
    
    Example: ``spread /home/foo/baz.zip``"
    Spread, spread <filepath> <pipe_confg>, "Splits a file of any type located in a given filepath (string) into tokens and then spreads them across the network with a stated pipeline configuration. An encrypted cryptographic receipt is then generated and stored in ``/opt/VIN/receipts/sent`` in *Linux* and ``VIN\receipts\sent\`` in *Windows*.
    
    Example 1: ``spread /home/foo/baz.zip /home/foo/pipeline.json``
    
    Example 2: ``spread /home/foo/baz.zip [ConcurrentEncoder,EntanglementEncoder,NamingEncoder,ValidationEncoder,ValidationDecoder,EntanglementDecoder,ConcurrentDecoder]``
    
    Example 3: ``spread /home/foo/baz.zip [coe,ene,nae,vae,vad,end,cod]``
    
    Example 4: ``spread /home/foo/baz.zip {'pipeline string'}``"
    Gather, gather <receipt_filepath>, "Gathers a spread file using the given receipt_filepath (string). It will be reassembled as a new file into the output directory ``/opt/VIN/outputs`` in *Linux* and ``VIN\outputs\`` in *Windows*.
    
    Example: ``gather /home/foo/CR1593084390``"
    Gather, gather <command> <receipt_filepath>, "Gathers a file but enables control over how the file is stored after gathered. The commands available are: ``append``, ``-a``, ``a`` to append data to existing file; ``overwrite``, ``-o``, ``o`` to overwrite the existing file; ``create``, ``-c``, ``c`` to create a new file.
    
    Example: ``gather append /home/foo/CR1593084390``" 
    Share, share <filepath> <ip_address> <receipt_port>, "The peer spreads a file from a given filepath (string), automatically establishes a secure channel with the ip_address (string) and receipt port (string) of another peer in the network, and transfers the encrypted cryptographic receipt. The receiver peer will automatically call ``gather`` on the receipt once decrypted.
    
    Example: ``share /home/foo/baz.zip 12.345.678.90 9091``"
    Share, share <command> <filepath> <ip_address> <receipt_port>, "Performs a spread but enables control over how the file is stored after gathered. The commands available are: ``append``, ``-a``, ``a`` to append data to existing file; ``overwrite``, ``-o``, ``o`` to overwrite the existing file; ``create``, ``-c``, ``c`` to create a new file.
    
    Example: ``share append /home/foo/baz.zip 12.345.678.90 9091``" 
    Share, share <command> <filepath> <ip_address> <receipt_port> <pipe_config>, "Performs a spread, enables control over how the file is stored and specifies a stated pipeline configuration. The commands available are: ``append``, ``-a``, ``a`` to append data to existing file; ``overwrite``, ``-o``, ``o`` to overwrite the existing file; ``create``, ``-c``, ``c`` to create a new file.
    
    Example 1: ``share append /home/foo/baz.zip 12.345.678.90 9091 /home/foo/pipeline.json``
    
    Example 2: ``share append /home/foo/baz.zip 12.345.678.90 9091 [ConcurrentEncoder,EntanglementEncoder,NamingEncoder, ValidationEncoder,ValidationDecoder,EntanglementDecoder,ConcurrentDecoder]``
    
    Example 3: ``share create /home/foo/baz.zip 12.345.678.90 9091 [coe,ene,nae,vae,vad,end,cod]``
    
    Example 4: ``share create /home/foo/baz.zip 12.345.678.90 9091 {'pipeline string'}``"
    Share, share <command> <filepath> <ip_address> <receipt_port> <runs>, "Performs a spread, enables control over how the file is stored, specifies a stated pipeline configuration and specifies the number of runs (string) to attempt to successfully spread the file. The commands available are: ``append``, ``-a``, ``a`` to append data to existing file; ``overwrite``, ``-o``, ``o`` to overwrite the existing file; ``create``, ``-c``, ``c`` to create a new file.
    
    Example 1: ``share append /home/foo/baz.zip 12.345.678.90 9091 /home/foo/pipeline.json 10``
    
    Example 2: ``share append /home/foo/baz.zip 12.345.678.90 9091 [ConcurrentEncoder,EntanglementEncoder,NamingEncoder, ValidationEncoder,ValidationDecoder,EntanglementDecoder,ConcurrentDecoder] 10``
    
    Example 3: ``share create /home/foo/baz.zip 12.345.678.90 9091 [coe,ene,nae,vae,vad,end,cod] 10``
    
    Example 4: ``share create /home/foo/baz.zip 12.345.678.90 9091 {'pipeline string'} 10``"
    Download, download <file_path> <save_path>, "Download file from provided absolute path to crypto receipt file. File saved at given path.
    
    Example: ``download /home/foo/CR1593084390``"
    Update Peer, update_peer <ip_add_rec> <recp_port_rec> <folder_path>, "Add a receiver peer via its IP address, receipt port, to a fuse folder path.
    
    Example: ``update_peer 12.345.678.90 9091 /home/target/share/foo/``"
    Health Check, health_check, "Displays health information for the node."
    Receipt Validation, receipt_validation <file_path>, "Validates a cryptographic receipt at the given file path (including receipt name).
    
    Example: ``receipt_validation /opt/VIN/receipts/sent/CR3736596702``"
    Shutdown, shutdown, "Send a shutdown signal to the current node that the user is connected to."


.. _vin-cli-func:

VIN™ CLI Functionality 
=======================

The following instructions assume that a two *VIN™* nodes and one bootstrap node have been instantiated and that one instance of the *VIN™ CLI* is running. For more information on how to get these set up, refer to :ref:`running-the-vin-linux` (or :ref:`running-the-vin-windows`).


HELP
----

.. panels::
    :card: none

    Displays a list of commands available to the *VIN™ CLI*.

    **Parameters**
    
    None.

    **Returns**
    
    None.
    
    ---

    **VIN_CLI RESPONSE**

    .. code-block:: none
      
      Commands available:
      - help
              This help message
      - exit
              Quit the session
      - ping
              Pings connected node to check its status.

      - getPeers
              Get all peers known to connected node. N.B. some of these hosts may be stale.

      - put <string> <string>
              Put provided <string>:<string> key-value pair on the network.
              Example:  'put k1 v1'

      - get <string>
              Get value for provided <string> key pair.
              Example:  'get k1'

      - spread <string> <string>
              Spread provided <string> absolute path to file and a ,<string> pipeline config file
              or pipeline encoders to use. Use
              Returns a path to the receipt file.
              Example:  'spread /home/foo/baz.zip /home/foo/pipeline.json'
              Example:  'spread /home/foo/baz.zip
              [ConcurrentEncoder,EntanglementEncoder,NamingEncoder,
              ValidationEncoder,ValidationDecoder,EntanglementDecoder,ConcurrentDecoder]
              Example:  'spread /home/foo/baz.zip [coe,ene,nae,vae,vad,end,cod]'
              Example:  'spread /home/foo/baz.zip {'pipeline string'}'

      - spread <string>
              Spread provided <string> absolute path to file
              Returns a path to the receipt file.
              Example:  'spread /home/foo/baz.zip'

      - gather <string>
              Gather file (create) from provided <string> absolute path to crypto receipt file.
              Example:  'gather /home/foo/CR1593084390'

      - download <string> <string>
              Download file from provided <string> absolute path to crypto receipt file. File Saved at given path <string>.
              Example:  'download /home/foo/CR1593084390 ./'

      - gather <string> <string>
              Gather file <string> mode from provided <string> absolute path to crypto receipt file.Use:
              'append'    / '-a' / 'a' to append data to existing file
              'overwrite' / '-o' / 'o' to overwrite existing file or
              'create'    / '-c' / 'c' to create a new one.
              Example:  'gather append /home/foo/CR1593084390'

      - share <string> <string> <string>
              Share file (create) provided <string> absolute path to file with <string> IP address
              at <string> receipt port.
              Example:  'share /home/foo/baz.zip 12.345.678.90 9091'

      - share <string> <string> <string> <string>
              Share file using <string> mode , provided <string> absolute path to file with <string> IP address
              at <string> receipt port and a <string> pipeline config file
              or pipeline encoders to use. Use:
              'append'    / '-a' / 'a' to append data to existing file
              'overwrite' / '-o' / 'o' to overwrite existing file or
              'create'    / '-c' / 'c' to create a new one.
              Example:  'share append /home/foo/baz.zip 12.345.678.90 9091

      - share <string> <string> <string> <string> <string>
              Share file using <string> mode , provided <string> absolute path to file with <string> IP address
              at <string> receipt port and a <string> pipeline config file
              or pipeline encoders to use. Use:
              'append'    / '-a' / 'a' to append data to existing file
              'overwrite' / '-o' / 'o' to overwrite existing file or
              'create'    / '-c' / 'c' to create a new one.
              Example:  'share append /home/foo/baz.zip 12.345.678.90 9091 /home/foo/pipeline.json'
              Example:  'share append /home/foo/baz.zip 12.345.678.90 9091
              [ConcurrentEncoder,EntanglementEncoder,NamingEncoder,
              ValidationEncoder,ValidationDecoder,EntanglementDecoder,ConcurrentDecoder]
              Example:  'share create /home/foo/baz.zip 12.345.678.90 9091 [coe,ene,nae,vae,vad,end,cod]'
              Example:  'share create /home/foo/baz.zip 12.345.678.90 9091 {'pipeline string'}'

      - share <string> <string> <string> <string> <string> <string>
              Share file using <string> mode , provided <string> absolute path to file with <string> IP address
              at <string> receipt port and a <string> pipeline config file
              or pipeline encoders to use and repeat <string> Use:
              'append'   / '-a' / 'a' to append data to existing file
              'overwrite'/ '-o' / 'o' to overwrite existing file or
              'create'   / '-c' / 'c' to create a new one.
              Example:  'share create /home/foo/baz.zip 12.345.678.90 9091 /home/foo/pipeline.json 10'
              Example:  'share create /home/foo/baz.zip 12.345.678.90 9091
              [ConcurrentEncoder,EntanglementEncoder,NamingEncoder,
              ValidationEncoder,ValidationDecoder,EntanglementDecoder,ConcurrentDecoder] 10'
              Example:  'share create /home/foo/baz.zip 12.345.678.90 9091 [coe,ene,nae,vae,vad,end,cod] 10'
              Example:  'share create /home/foo/baz.zip 12.345.678.90 9091 {'pipeline string'} 10'

      - [EXPERIMENTAL] stream_test <string> <string>
              Test unbounded stream to local node at <address>:<port>.
      - update_peer <string> <string> <string>
              Add a peer to a fuse folder
              Example:  'update_peer 12.345.678.90 9091 /home/target/share/foo/'
      - health_check
              Print health metrics for the node
              Example:  'health_check'
      - receipt_validation <string>
              Validate a crypto receipt
              Example:  'receipt_validation /opt/VIN/receipts/sent/CR3736596702'
      - shutdown
              Shutdown connected node.




EXIT
-----

.. panels::
    :card: none

    Quits the current session of the *VIN™ CLI*.

    ---

    **VIN_CLI RESPONSE**

    .. code-block:: none

      VIN@10.51.2.22:7070> exit
      So long for now.


PING
-----

.. panels::
    :card: none

    Pings the connected node to check its status. The connected node responds with a "Server pong!" message if successful.

    ---

    **VIN_CLI RESPONSE**

    .. code-block:: none

      VIN@10.51.2.22:7070> ping
      Server pong!

    **VIN™ NODE RESPONSE**

    .. code-block:: none

      17:56:06:605 http: URI: /ping? ; request from: 10.51.2.22:45512

PUT
--------------------------------

.. panels::
    :card: none

    A simple way to ensure that the network as been properly configured is to put a key-value pair onto the network. To do so, in the *VIN™ CLI* window, run ``put <key> <value>``. For this example ``test_key`` was used for the ``<key>`` and ``test_value`` for the ``<value>``. Note that the ``<key>`` and ``<value>`` can be any string that doesn't contain spaces. 

    **Parameters**
    
    ``key`` *string*: The unique identifier used to locate the given ``value``.

    ``value`` *string*: The value which will be associated with the given ``key``.

    **Returns**
    
    None.

    ---

    **VIN_CLI RESPONSE**

    .. code-block:: none

      VIN@10.51.2.22:7070> put test_key test_value
      Sending payload:
      {"key":"test_key","value":"test_value"}

      Waiting for response...
      Status : 200
      Reason : 'putValue' successful:  Key: test_key ; Value: test_value
      Response received

      [test_key]:test_value   put successfully

    **VIN™ NODE RESPONSE**

    .. code-block:: none

      17:47:30:360 http: URI: /putValue ; request from: 10.51.2.22:45502
      17:47:30:360 http: 'putValue' request received
      17:47:30:360 http: 'putValue' successful:  Key: test_key ; Value: test_value
      17:47:30:360 benc: 'putValue' request latency 0 min 0 sec 0 msec




GET
-----

.. panels::
    :card: none

    With a value on the network it can be retrieved by running ``get <key>``. For this example ``test_key`` was used for the ``<key>``. 

    **Parameters**
    
    ``key`` *string*: The unique identifier used to locate the given ``value``.

    **Returns**
    
    None.

    ---

    **VIN_CLI RESPONSE**

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

    **VIN™ NODE RESPONSE**

    .. code-block:: none

      17:53:36:417 http: URI: /getValue ; request from: 10.51.2.22:45510
      17:53:36:417 http: 'getValue' request received
      17:53:36:417 http: 'getValue' successful:  Key: test_key ; Value: test_value
      17:53:36:417 benc: 'getValue' request latency 0 min 0 sec 0 msec







SPREAD
---------

.. panels::
    :card: none

    TEXT

    ---

    TEXT


The *VIN™* can spread any file type onto it's network. To do a basic spread run ``spread <filepath>`` where the ``<filepath>`` is the absolute path and name of the file to be spread. For this example, it is ``/home/user/Dev/test/vin_test.txt``. An encrypted cryptographic receipt is generated upon spreading, is outputted in the terminal window, and is stored in ``/opt/VIN/receipts/sent`` and ``VIN\receipts\sent\`` directories in *Linux* and *Windows*, respectively. The output of a successful ``spread`` is shown below.

.. figure:: images/vin_cli/vincli_spread.png
  :scale: 100
  :align: center
  :alt: Successful Spread

  Successful Get (*VIN™ CLI* = top, Peer_1 = bottom)


GATHER
--------

.. panels::
    :card: none

    TEXT

    ---

    TEXT

After a file as been spread to the network a cryptographic receipt will be generated. Using this receipt, the file can be retrieved from the network via the ``gather`` command. To do a basic ``gather``, run ``gather <receipt_path>``. Copy the ``<receipt_path>`` generated from the :ref:`spread-file` example; in this case, it was ``/opt/VIN/receipts/sent/CR899957170``. If the file was successfully gathered, the following output should be displayed.

.. figure:: images/vin_cli/vincli_gather.png
  :scale: 100
  :align: center
  :alt: Successful Gather

  Successful Get (*VIN™ CLI* = top, Peer_1 = bottom)

Note: this ``gather`` created a new ``vin_test.txt`` file, thus there is a ``(2)`` at the end of the filename. To overwrite the file, or append to its contents, refer to the :ref:`supported-commands` table.


SHARE
--------------

.. panels::
    :card: none

    TEXT

    ---

    TEXT

The *VIN™* is capable of sharing any file type that is required by the user. To do a basic share run ``share <filepath> <ip_address> <receipt_port>``. For this example, ``<filepath>`` is ``/home/user/Dev/test/vin_test.txt``, the ``<ip_address>`` and ``<receipt_port>`` are the IP address and receipt port of the *VIN™* node not being utilized by the *VIN™ CLI*, or ``127.0.0.1`` and ``9091``, respectively. Completing a successful share will generate the following output:

.. figure:: images/vin_cli/vincli_share.png
  :scale: 100
  :align: center
  :alt: Successful Share

  Successful Share Between Peers (*VIN™ CLI* = top, Peer_1 = left, Peer_2 = right)

To manually confirm that the file has been received navigate to ``/opt/VIN/outputs/`` for *Linux* and ``C:\ProgramData\VIN\outputs`` for *Windows* and ensure that the file is located in this directory. Additionally, ``/opt/VIN/receipts/sent/`` for *Linux* and ``C:\ProgramData\VIN\receipts\sent`` for *Windows* should contain a new cryptographic receipt.

For all of the options available with the ``share`` command, refer to the :ref:`supported-commands` table.


GETPEERS
----------------------------------------

.. panels::
    :card: none

    TEXT

    ---

    TEXT


Run ``getPeers`` in the *VIN™ CLI* window to generate a list of all peers connected to a bootstrap node as displayed in the figure below.  


.. figure:: images/vin_cli/vincli_getpeers.png
  :scale: 100
  :align: center
  :alt: getPeers

  getPeers Example

In this example, there are two peers with their information listed as follows: ``[unique_node_identifier: { ip_address_of_peers_host peers_data_port }]``


DOWNLOAD
----------

.. panels::
    :card: none

    TEXT

    ---

    TEXT



UPDATE_PEER
-----------

.. panels::
    :card: none

    TEXT

    ---

    TEXT



HEALTH_CHECK
-------------

.. panels::
    :card: none

    TEXT

    ---

    TEXT



RECEIPT_VALIDATION
------------------

.. panels::
    :card: none

    TEXT

    ---

    TEXT





SHUTDOWN
-----------------------

.. panels::
    :card: none

    To shutdown the particular node which the *VIN™ CLI* is currently connected to, run ``shutdown``.

    **Parameters**
    
    None.

    **Returns**
    
    None.

    ---

    **VIN_CLI RESPONSE**

    .. code-block:: none

      VIN@10.51.2.22:7070> shutdown
      <h1>Exit<h1>

    **VIN™ NODE RESPONSE**

    .. code-block:: none

      16:53:13:409 http: URI: /exit ; request from: 10.51.2.22:45494
      16:53:13:409 http: 'exit' request received
      16:53:13:409 http: HTTP server exit
      Uninitializing subsystem: Logging SubsystemFUSE: Handle end thread signal 10

      16:53:19:146 root: VIN exit