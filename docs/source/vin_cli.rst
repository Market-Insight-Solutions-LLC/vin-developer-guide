.. _vin-cli:

***********************************
VIN™ Command Line Interface (CLI)
***********************************

*VIN™* commands are assessable through the *VIN™ Command Line Interface (CLI)* which acts as a Hypertext Transfer Protocol (HTTP) client for reaching the *VIN™* HTTP server from the command line. Note: the *VIN™ CLI* will be installed during the installation of the *VIN™*.

The following table displays a list of APIs that are accessible through the *VIN™ CLI*. For examples, and the outputs of each command, please refer to the :ref:`vin-cli-func` section.

.. _vincli-commands:

.. csv-table:: VIN™ CLI Commands
    :header: Command, Command Line Instruction, Description
    :widths: 15 40 50 
    :width: 100%

    Help, help, "Displays a list of commands available to the *VIN™ CLI*."
    Exit, exit, "Quits the current session of the *VIN™ CLI*."
    Ping, ping, "Pings the connected node to check its status. The connected node responds with a 'Server pong!' message if successful."
    GetPeers, getPeers, "Get the IP addresses and data ports for all peers connected to this peer (the one invoking ``getPeers``) on the network. Note: some of the nodes may be stale."
    Put, put <key> <value>, "Puts a user provided value (string) onto the network which corresponds to the user provided key (string).
    
    Example: ``put k1 v1``"
    Get, get <key>, "Requires a given key (string) and returns the Key-Value pair from the respective node. The value is displayed in the *VIN™ CLI* window. No other output is displayed.
    
    Example: ``get k1``"
    Spread, spread <filepath>, "Splits a file of any type located in a given filepath (string) into tokens and then spreads them across the network. An encrypted cryptographic receipt is then generated and stored in ``/opt/VIN/receipts/sent`` in *Linux* and ``VIN\receipts\sent\`` in *Windows*.
    
    Example: ``spread /home/foo/baz.zip``"
    Spread, spread <filepath> <pipe_config>, "Splits a file of any type located in a given filepath (string) into tokens and then spreads them across the network with a stated pipeline configuration. An encrypted cryptographic receipt is then generated and stored in ``/opt/VIN/receipts/sent`` in *Linux* and ``VIN\receipts\sent\`` in *Windows*.
    
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
    Share, share <command> <filepath> <ip_address> <receipt_port> <pipe_config> <runs>, "Performs a spread, enables control over how the file is stored, specifies a stated pipeline configuration and specifies the number of times (runs) to share the file. The commands available are: ``append``, ``-a``, ``a`` to append data to existing file; ``overwrite``, ``-o``, ``o`` to overwrite the existing file; ``create``, ``-c``, ``c`` to create a new file.
    
    Example 1: ``share append /home/foo/baz.zip 12.345.678.90 9091 /home/foo/pipeline.json 10``
    
    Example 2: ``share append /home/foo/baz.zip 12.345.678.90 9091 [ConcurrentEncoder,EntanglementEncoder,NamingEncoder, ValidationEncoder,ValidationDecoder,EntanglementDecoder,ConcurrentDecoder] 10``
    
    Example 3: ``share create /home/foo/baz.zip 12.345.678.90 9091 [coe,ene,nae,vae,vad,end,cod] 10``
    
    Example 4: ``share create /home/foo/baz.zip 12.345.678.90 9091 {'pipeline string'} 10``"
    Download, download <file_path> <save_path>, "Download file from provided absolute path to cryptographic receipt file. The file will be saved at given save path.
    
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

The following instructions assume that a two *VIN™* nodes and one bootstrap node have been instantiated and that one instance of the *VIN™ CLI* is running. For more information on how to set these up, refer to :ref:`running-the-vin-linux` (or :ref:`running-the-vin-windows`). 

Note: the following *VIN™ CLI* descriptions were gathered from a *Linux* operating system. However, other operating systems will have the same outputs unless otherwise noted.

..
  HELP
  -----

.. panels::
    :card: none

    **help**
    ^^^^^^^^^

    Displays a list of commands available to the *VIN™ CLI*.

    :bold-underline:`Parameters`
    
    None.

    :bold-underline:`Returns`
    
    None.
    
    ---

    :bold-underline:`VIN™ CLI Response`

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


---------------------------

..
  EXIT
  -----

.. panels::
    :card: none

    **exit**
    ^^^^^^^^^

    Quits the current session of the *VIN™ CLI*.

    :bold-underline:`Parameters`
    
    None.

    :bold-underline:`Returns`
    
    None.

    ---

    :bold-underline:`VIN™ CLI Response`

    .. code-block:: none

      VIN@10.51.2.22:7070> exit
      So long for now.

---------------------------

..
  PING
  -----

.. panels::
    :card: none

    **ping**
    ^^^^^^^^^

    Pings the connected node to check its status. The connected node responds with a "Server pong!" message if successful.

    :bold-underline:`Parameters`
    
    None.

    :bold-underline:`Returns`
    
    None.

    ---

    :bold-underline:`VIN™ CLI Response`

    .. code-block:: none

      VIN@10.51.2.22:7070> ping
      Server pong!

    :bold-underline:`VIN™ Node Response`

    .. code-block:: none

      17:56:06:605 http: URI: /ping? ; request from: 10.51.2.22:45512

---------------------------

..
  PUT
  -----

.. panels::
    :card: none

    **put**
    ^^^^^^^^^

    To do a put so, in the *VIN™ CLI* window, run ``put <key> <value>``. Note that the ``<key>`` and ``<value>`` can be any string that doesn't contain spaces. 

    :bold-underline:`Parameters`
    
    ``key`` *string*: The unique identifier used to locate the given ``value``.

    ``value`` *string*: The value which will be associated with the given ``key``.

    :bold-underline:`Returns`
    
    None.

    ---

    :bold-underline:`VIN™ CLI Response`

    .. code-block:: none

      VIN@10.51.2.22:7070> put test_key test_value
      Sending payload:
      {"key":"test_key","value":"test_value"}

      Waiting for response...
      Status : 200
      Reason : 'putValue' successful:  Key: test_key ; Value: test_value
      Response received

      [test_key]:test_value   put successfully

    :bold-underline:`VIN™ Node Response`

    .. code-block:: none

      17:47:30:360 http: URI: /putValue ; request from: 10.51.2.22:45502
      17:47:30:360 http: 'putValue' request received
      17:47:30:360 http: 'putValue' successful:  Key: test_key ; Value: test_value
      17:47:30:360 benc: 'putValue' request latency 0 min 0 sec 0 msec

---------------------------

..
  GET
  -----

.. panels::
    :card: none

    **get**
    ^^^^^^^^^

    With a value on the network it can be retrieved by running ``get <key>``. For this example ``test_key`` was used for the ``<key>``. 

    :bold-underline:`Parameters`
    
    ``key`` *string*: The unique identifier used to locate the given ``value``.

    :bold-underline:`Returns`
    
    None.

    ---

    :bold-underline:`VIN™ CLI Response`

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

    :bold-underline:`VIN™ Node Response`

    .. code-block:: none

      17:53:36:417 http: URI: /getValue ; request from: 10.51.2.22:45510
      17:53:36:417 http: 'getValue' request received
      17:53:36:417 http: 'getValue' successful:  Key: test_key ; Value: test_value
      17:53:36:417 benc: 'getValue' request latency 0 min 0 sec 0 msec

---------------------------

..
  SPREAD
  ---------

.. panels::
    :card: none

    **spread**
    ^^^^^^^^^^^^^
    The *VIN™* can spread any file type onto its network. To do do run ``spread <filepath> <pipe_confg>``. Refer to the :ref:`vincli-commands` table for more information regarding these options. An encrypted cryptographic receipt is generated upon spreading, is outputted in the terminal window, and is stored in ``/opt/VIN/receipts/sent`` and ``VIN\receipts\sent\`` directories in *Linux* and *Windows*, respectively. Note: running ``spread`` without a ``<pipe_confg>`` will result in the command utilizing the default pipeline located in the ``defaults.cfg`` file (refer to :ref:`vin-configuration`).

    :bold-underline:`Parameters`
    
    ``filepath`` *string*: The absolute path and name of the file to be spread.

    ``pipe_config`` *string*: The encoders/decoders to use during the spread. Refer to the :ref:`vin-configuration` table for more information.    

    :bold-underline:`Returns`
    
    ``cryptocraphic_receipt_location`` *string*: The location and name of the cryptographic receipt generated by the ``spread`` command.

    ---

    :bold-underline:`VIN™ CLI Response`

    .. code-block:: none

      VIN@10.51.2.22:7070> spread /home/dion/Dev/vin_test.txt [coe,ene,nae,vae,vad,end,cod]
      Creating a basic pipeline...
      Pipeline:
      {encoders:[{name:ConcurrentEncoder},{name:EntanglementEncoder},{name:NamingEncoder},{name:ValidationEncoder}],decoders:[{name:ValidationDecoder},{name:EntanglementDecoder},{name:ConcurrentDecoder}],channels:[]}

      Waiting for response...
      Status : 200
      Reason : OK
      Response received
      File spread successfully

      Receipt saved to location : /opt/VIN/receipts/sent/CR1213465839

    :bold-underline:`VIN™ Node Response`

    .. code-block:: none

      18:55:07:369 http: URI: /spread ; request from: 10.51.2.22:45520
      18:55:07:369 benc: 'spread' chunking latency 0 min 0 sec 0 msec
      18:55:07:369 root: Using received custom coders pipeline
      18:55:07:370 root: Validate encoders...
      18:55:07:370 root: Add: ConcurrentEncoder (cw_density = 0.33)
      18:55:07:370 root: Add: ConcurrentEncoder (cw_size_2_pow = 15)
      18:55:07:370 root: Add: ConcurrentEncoder (log = false)
      18:55:07:370 root: Add: ConcurrentEncoder (msg_len = 1000)
      18:55:07:370 root: Add: ConcurrentEncoder (red_bits = 30)
      18:55:07:370 root: Add: EntanglementEncoder (log = false)
      18:55:07:370 root: Add: NamingEncoder (log = false)
      18:55:07:370 root: Add: ValidationEncoder (id = network_data)
      18:55:07:370 root: Add: ValidationEncoder (log = false)
      18:55:07:370 root: Enc: ConcurrentEncoder EntanglementEncoder NamingEncoder ValidationEncoder
      18:55:07:370 root: Validate decoders...
      18:55:07:370 root: Add: ValidationDecoder (id = network_data)
      18:55:07:370 root: Add: ValidationDecoder (log = false)
      18:55:07:370 root: Add: EntanglementDecoder (log = false)
      18:55:07:370 root: Add: ConcurrentDecoder (log = false)
      18:55:07:370 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
      18:55:07:370 root: Validate channels...
      18:55:07:370 root: No channels specified
      18:55:07:369 http: 'spread' request received
      18:55:07:431 benc: 'spread' file: vin_test.txt size: 16
      18:55:07:432 root: Logging pre-encoded file
      18:55:07:432 root: Encoding
      18:55:07:433 enco: ConcurrentEncoder: avg marks: 1021
      18:55:07:434 benc: 'spread' encoding latency 0 min 0 sec 2 msec
      Job Watchdog (0): Job finished signal received
      Job Watchdog (0): Tasks (Processing 0, Pending 0)
      18:55:07:502 benc: 'spread' uploading latency 0 min 0 sec 68 msec
      18:55:07:503 benc: 'spread' total latency 0 min 0 sec 71 msec
      18:55:07:503 benc: 'spread' encoded data size: 4096  ( 1 chunks of 4096 bytes )
      18:55:07:503 benc: 'spread' system data size:  20480 ( redundancy = 5 )
      18:55:07:540 http: 'spread' receipt saved to: /opt/VIN/receipts/sent/CR1213465839

---------------------------

..
  GATHER
  --------

.. panels::
    :card: none

    **gather**
    ^^^^^^^^^^^^^

    With a file spread to the network, a cryptographic receipt will be generated. Using this receipt, the file can be retrieved from the network via the ``gather`` command. To do so, run ``gather <command> <receipt_path>``. 

    :bold-underline:`Parameters`
    
    ``command`` *string*: The commands available are ``append``, ``-a``, ``a`` to append data to existing file; ``overwrite``, ``-o``, ``o`` to overwrite the existing file; ``create``, ``-c``, ``c`` to create a new file.

    ``receipt_path`` *string*: The location and name of the cryptographic receipt.  

    :bold-underline:`Returns`
    
    ``file_location`` *string*: The location and name of gathered file.

    ---

    :bold-underline:`VIN™ CLI Response`

    .. code-block:: none

      VIN@10.51.2.22:7070> gather create /opt/VIN/receipts/sent/CR1213465839

      Waiting for response...
      Status : 200
      Reason : OK
      Response received
      File gathered successfully

      File reconstructed at : /opt/VIN/outputs/vin_test/vin_test.txt on node host.

    :bold-underline:`VIN™ Node Response`

    .. code-block:: none
      
      19:11:42:011 http: URI: /gather ; request from: 10.51.2.22:45522
      19:11:42:012 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
      19:11:42:011 http: 'gather' request received
      19:11:42:027 benc: 'gather' file: vin_test.txt size: 16
      Job Watchdog (110): Tasks (Processing 0, Pending 0)
      19:11:43:028 benc: 'gather' acquisition latency 0 min 1 sec 16 msec
      19:11:43:029 benc: 'gather' encoded data size: 4096  ( 1 chunks of 4096 bytes )
      19:11:43:029 root: Decoding
      19:11:43:036 benc: 'gather' decoding latency 0 min 0 sec 7 msec
      19:11:43:037 benc: 'gather' total latency 0 min 1 sec 25 msec
      19:11:43:061 root: File rebuild at: /opt/VIN/outputs/vin_test/vin_test.txt

---------------------------

..
  SHARE
  --------------

.. panels::
    :card: none

    **share**
    ^^^^^^^^^^^^^

    The *VIN™* is capable of sharing any file type that is required by the user. To do a basic share run ``share <command> <filepath> <ip_address> <receipt_port> <pipe_config> <runs>``. For more examples of the ``share`` command refer to :ref:`vincli-commands`. Note: To manually confirm that the file has been received navigate to ``/opt/VIN/outputs/`` for *Linux* and ``C:\ProgramData\VIN\outputs`` for *Windows* on teh receiver node. Additionally, ``/opt/VIN/receipts/sent/`` for *Linux* and ``C:\ProgramData\VIN\receipts\sent`` for *Windows* should contain a new cryptographic receipt.

    :bold-underline:`Parameters`

    ``command`` *string*: The commands available are ``append``, ``-a``, ``a`` to append data to existing file; ``overwrite``, ``-o``, ``o`` to overwrite the existing file; ``create``, ``-c``, ``c`` to create a new file.
    
    ``filepath`` *string*: The absolute path and name of the file to be spread.

    ``ip_address`` *string*: The IP address of the receiver peer.

    ``receipt_port`` *string*: The receipt port of the receiver peer.

    ``pipe_confg`` *string*: The encoders/decoders to use during the spread. Refer to the :ref:`vin-configuration` table for more information.    

    :bold-underline:`Returns`
    
    None.

    ---

    :bold-underline:`VIN™ CLI Response`

    .. code-block:: none

      VIN@10.51.2.22:7070> share create /home/user/Dev/vin_test.txt 10.51.2.21 9090 [coe,ene,nae,vae,vad,end,cod] 2
      Creating a basic pipeline...
      Pipeline:
      {encoders:[{name:ConcurrentEncoder},{name:EntanglementEncoder},{name:NamingEncoder},{name:ValidationEncoder}],decoders:[{name:ValidationDecoder},{name:EntanglementDecoder},{name:ConcurrentDecoder}],channels:[]}

      Waiting for response...
      Status : 200
      Reason : OK
      Response received
      File shared to 10.51.2.21 9090 successfully (run: 1)

      Waiting for response...
      Status : 200
      Reason : OK
      Response received
      File shared to 10.51.2.21 9090 successfully (run: 2)

    :bold-underline:`VIN™ Node Response`

    .. code-block:: none

      19:39:02:596 http: URI: /share ; request from: 10.51.2.22:45530
      19:39:02:596 http: 'share' request received
      19:39:02:596 http: Share to: 10.51.2.21:9090 ; File: vin_test.txt ; Size: 16 ; Flag: create
      19:39:02:596 benc: 'share' chunking latency 0 min 0 sec 0 msec
      19:39:02:597 benc: 'spread' file: vin_test.txt size: 16
      19:39:02:596 root: Using received custom coders pipeline
      19:39:02:597 root: Validate encoders...
      19:39:02:597 root: Add: ConcurrentEncoder (cw_density = 0.33)
      19:39:02:597 root: Add: ConcurrentEncoder (cw_size_2_pow = 15)
      19:39:02:597 root: Add: ConcurrentEncoder (log = false)
      19:39:02:597 root: Add: ConcurrentEncoder (msg_len = 1000)
      19:39:02:597 root: Add: ConcurrentEncoder (red_bits = 30)
      19:39:02:597 root: Add: EntanglementEncoder (log = false)
      19:39:02:597 root: Add: NamingEncoder (log = false)
      19:39:02:597 root: Add: ValidationEncoder (id = network_data)
      19:39:02:597 root: Add: ValidationEncoder (log = false)
      19:39:02:597 root: Enc: ConcurrentEncoder EntanglementEncoder NamingEncoder ValidationEncoder
      19:39:02:597 root: Validate decoders...
      19:39:02:597 root: Add: ValidationDecoder (id = network_data)
      19:39:02:597 root: Add: ValidationDecoder (log = false)
      19:39:02:597 root: Add: EntanglementDecoder (log = false)
      19:39:02:597 root: Add: ConcurrentDecoder (log = false)
      19:39:02:597 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
      19:39:02:597 root: Validate channels...
      19:39:02:597 root: No channels specified
      19:39:02:597 root: Logging pre-encoded file
      19:39:02:597 root: Encoding
      19:39:02:601 benc: 'spread' encoding latency 0 min 0 sec 4 msec
      19:39:02:601 enco: ConcurrentEncoder: avg marks: 1021
      19:39:02:803 benc: Found: 3 peers
      Job Watchdog (0): Job finished signal received
      Job Watchdog (0): Tasks (Processing 0, Pending 0)
      19:39:02:803 benc: 'spread' uploading latency 0 min 0 sec 201 msec
      19:39:02:803 benc: 'spread' total latency 0 min 0 sec 206 msec
      19:39:02:803 benc: 'spread' encoded data size: 4096  ( 1 chunks of 4096 bytes )
      19:39:02:803 benc: 'spread' system data size:  20480 ( redundancy = 5 )
      19:39:02:803 root: Sharing to peer: 10.51.2.21:9090
      19:39:02:844 root: Receipt session started
      19:39:02:845 root: Connected to peer: 10.51.2.21:9090
      19:39:02:846 root: Session token obtained
      19:39:02:846 root: Sending receipt
      19:39:03:858 root: Sending status request
      19:39:03:860 root: Status: File rebuild OK
      19:39:03:860 root: Sharing end session
      19:39:03:860 benc: 'share' receipt latency 0 min 1 sec 57 msec
      19:39:03:861 benc: 'share' encoded data size: 4096
      19:39:03:861 benc: 'share' system data size:  20480 ( redundancy = 5 )
      19:39:03:861 benc: 'share' total latency 0 min 1 sec 264 msec
      19:39:03:863 http: URI: /share ; request from: 10.51.2.22:45534
      19:39:03:863 http: 'share' request received
      19:39:03:863 http: Share to: 10.51.2.21:9090 ; File: vin_test.txt ; Size: 16 ; Flag: create
      19:39:03:863 benc: 'share' chunking latency 0 min 0 sec 0 msec
      19:39:03:863 root: Using received custom coders pipeline
      19:39:03:864 root: Validate encoders...
      19:39:03:864 root: Add: ConcurrentEncoder (cw_density = 0.33)
      19:39:03:864 root: Add: ConcurrentEncoder (cw_size_2_pow = 15)
      19:39:03:864 root: Add: ConcurrentEncoder (log = false)
      19:39:03:864 root: Add: ConcurrentEncoder (msg_len = 1000)
      19:39:03:864 root: Add: ConcurrentEncoder (red_bits = 30)
      19:39:03:864 root: Add: EntanglementEncoder (log = false)
      19:39:03:864 root: Add: NamingEncoder (log = false)
      19:39:03:864 root: Add: ValidationEncoder (id = network_data)
      19:39:03:864 root: Add: ValidationEncoder (log = false)
      19:39:03:864 root: Enc: ConcurrentEncoder EntanglementEncoder NamingEncoder ValidationEncoder
      19:39:03:864 root: Validate decoders...
      19:39:03:864 root: Add: ValidationDecoder (id = network_data)
      19:39:03:864 root: Add: ValidationDecoder (log = false)
      19:39:03:864 root: Add: EntanglementDecoder (log = false)
      19:39:03:864 root: Add: ConcurrentDecoder (log = false)
      19:39:03:864 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
      19:39:03:864 root: Validate channels...
      19:39:03:864 root: No channels specified
      19:39:03:864 root: Logging pre-encoded file
      19:39:03:864 root: Encoding
      19:39:03:864 benc: 'spread' file: vin_test.txt size: 16
      19:39:03:867 enco: ConcurrentEncoder: avg marks: 1021
      19:39:03:867 benc: 'spread' encoding latency 0 min 0 sec 3 msec
      Job Watchdog (0): Job finished signal received
      Job Watchdog (0): Tasks (Processing 0, Pending 0)
      19:39:03:907 benc: 'spread' uploading latency 0 min 0 sec 39 msec
      19:39:03:907 benc: 'spread' total latency 0 min 0 sec 43 msec
      19:39:03:907 benc: 'spread' encoded data size: 4096  ( 1 chunks of 4096 bytes )
      19:39:03:907 benc: 'spread' system data size:  20480 ( redundancy = 5 )
      19:39:03:907 root: Sharing to peer: 10.51.2.21:9090
      19:39:03:914 root: Receipt session started
      19:39:03:914 root: Connected to peer: 10.51.2.21:9090
      19:39:03:915 root: Session token obtained
      19:39:03:915 root: Sending receipt
      19:39:04:927 root: Sending status request
      19:39:04:929 root: Status: File rebuild OK
      19:39:04:929 root: Sharing end session
      19:39:04:929 benc: 'share' receipt latency 0 min 1 sec 21 msec
      19:39:04:929 benc: 'share' encoded data size: 4096
      19:39:04:929 benc: 'share' system data size:  20480 ( redundancy = 5 )
      19:39:04:929 benc: 'share' total latency 0 min 1 sec 66 msec

---------------------------

..
  GETPEERS
  ------------

.. panels::
    :card: none

    **getPeers**
    ^^^^^^^^^^^^^

    Generates a list of all peers connected to (and including) the bootstrap node.

    :bold-underline:`Parameters`

    None.
    
    :bold-underline:`Returns`

    ``peer_list``: A list of peers connected to (and including) the bootstrap node.

    ---

    :bold-underline:`VIN™ CLI Response`

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

    
    :bold-underline:`VIN™ Node Response`

    .. code-block:: none

        19:52:18:957 http: URI: /getPeers ; request from: 10.51.2.22:45542
        19:52:18:957 http: 'getPeers' request received
        19:52:19:070 http: Listing peer: 10.51.2.21:8000
        19:52:19:070 http: MetaData: {}
        19:52:19:070 http: Listing peer: 10.51.2.21:8080
        19:52:19:070 http: MetaData: {"kad_port":"8080","receipt_port":"9090","http_port":"7070"}

---------------------------

..
  DOWNLOAD
  ----------

.. panels::
    :card: none

    **download**
    ^^^^^^^^^^^^^

    Downloads a file from the network given the provided absolute path to cryptographic receipt file. The file will be saved at given save path.

    :bold-underline:`Parameters`

    ``filepath`` *string*: The absolute path and name of the cryptographic receipt.

    ``save_file`` *string*: The absolute path to the location the file will be saved upon being downloaded.

    :bold-underline:`Returns`

    None.

    ---

    :bold-underline:`VIN™ CLI Response`

    .. code-block:: none

      VIN@10.51.2.22:7070> download /opt/VIN/receipts/sent/CR1216842901 /home/dion/

      Waiting for response...
      Status : 200
      Reason : OK
      Response received
      File gathered successfully

      Downloading file

      Saving to disk

    :bold-underline:`VIN™ Node Response`

    .. code-block:: none

      19:53:41:893 http: URI: /download ; request from: 10.51.2.22:45544
      19:53:41:893 http: 'download' request received by server
      19:53:41:893 cr_: key: gather_flag could not be found
      19:53:41:894 root: Dec: ValidationDecoder EntanglementDecoder ConcurrentDecoder
      19:53:41:895 benc: 'gather' file: vin_test.txt size: 16
      Job Watchdog (110): Tasks (Processing 0, Pending 0)
      19:53:42:896 benc: 'gather' acquisition latency 0 min 1 sec 2 msec
      19:53:42:896 benc: 'gather' encoded data size: 4096  ( 1 chunks of 4096 bytes )
      19:53:42:897 root: Decoding
      19:53:42:903 benc: 'gather' decoding latency 0 min 0 sec 6 msec
      19:53:42:904 benc: 'gather' total latency 0 min 1 sec 10 msec

---------------------------

..
  UPDATE_PEER
  -----------

.. panels::
    :card: none

    **update_peer**
    ^^^^^^^^^^^^^^^^

    Add a receiver peer via its IP address, receipt port, to a fuse folder path to the ``fuse_peers.cfg`` file. Refer to :ref:`vin-install-fuse` for more information on using FUSE.

    :bold-underline:`Parameters`

    ``ip_add_rec`` *string*: The IP address of the receiver peer.

    ``recp_port_rec`` *string*: The receipt port of the receiver peer.

    ``folder_path`` *string*: The shared folder to be used by FUSE (e.g. ``share/``).

    :bold-underline:`Returns`

    None.

    ---

    :bold-underline:`VIN™ CLI Response`

    .. code-block:: none

      VIN@10.51.2.22:7070> update_peer 10.51.2.21 9090 share/
      Peer updated.

    :bold-underline:`VIN™ Node Response`

    .. code-block:: none

      19:59:47:012 http: URI: /UpdateFusePeer ; request from: 10.51.2.22:45546
      19:59:47:012 http: 'updateFusePeer' request received by server
      19:59:47:012 http: 'updateFusePeer' request with params:
      19:59:47:012 http: 'updateFusePeer' ip: 10.51.2.21
      19:59:47:012 http: 'updateFusePeer' port: 9090
      19:59:47:012 http: 'updateFusePeer' path: share/

---------------------------

..
  HEALTH_CHECK
  -------------

.. panels::
    :card: none

    **health_check**
    ^^^^^^^^^^^^^^^^^^

    :bold-underline:`Parameters`

    None.

    :bold-underline:`Returns`

    None.

    ---

    :bold-underline:`VIN™ CLI Response`

    .. code-block:: none

      VIN@10.51.2.22:7070> health_check

      Waiting for response...
      Status : 200
      Reason : OK
      Response received
      Health check succeeded

      dht-initialized: true
      receipt-server-connected: true
      stream-in-progress: false
      active-stream-id: NONE
      node-shutdown-event: false


    :bold-underline:`VIN™ Node Response`

    .. code-block:: none

      20:01:42:819 http: URI: /healthCheck ; request from: 10.51.2.22:45548
      20:01:42:819 http: 'healthCheck' request received

---------------------------

..
  RECEIPT_VALIDATION
  ------------------

  .. panels::
      :card: none

      **receipt_validation**
      ^^^^^^^^^^^^^^^^^^^^^

      :bold-underline:`Parameters`

      ``filepath`` *string*: The absolute path and name of the cryptographic receipt.

      :bold-underline:`Returns`

      None.

      ---

      :bold-underline:`VIN™ CLI Response`

      .. code-block:: none


      :bold-underline:`VIN™ Node Response`

      .. code-block:: none

  




..
  SHUTDOWN
  -----------------------

.. panels::
    :card: none

    **shutdown**
    ^^^^^^^^^^^^^

    To shutdown the particular node which the *VIN™ CLI* is currently connected to, run ``shutdown``.

    :bold-underline:`Parameters`
    
    None.

    :bold-underline:`Returns`
    
    None.

    ---

    :bold-underline:`VIN™ CLI Response`

    .. code-block:: none

      VIN@10.51.2.22:7070> shutdown
      <h1>Exit<h1>

    :bold-underline:`VIN™ Node Response`

    .. code-block:: none

      20:03:57:404 http: URI: /exit ; request from: 10.51.2.22:45558
      20:03:57:404 http: 'exit' request received
      20:03:57:404 http: HTTP server exit
      Uninitializing subsystem: Logging SubsystemFUSE: Handle end thread signal 10

      20:04:02:301 root: VIN exit

