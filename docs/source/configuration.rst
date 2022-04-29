.. _vin-configuration:

****************************
VIN™ Configuration Options
****************************

This section presents the configuration options available to the *VIN™* upon its installation. The following tables highlight each parameter in the configuration file as well as a description of the parameter, its default value, and any options that the value may be set to.

connections
===========

The configuration items listed below relate to connection information for the various components that comprise the *VIN™*.

.. csv-table:: Connection Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *version*, "The current version of the *VIN™*.", 0.1.0, "Do not modify."
    *config_name*, "The name of the *VIN™’s* configuration file.", default_config, "Default value or user-defined."
    *fuse_peers_name*, "The name of the fuse peers configuration file.", fuse_peers, "Default or user-defined."
    *bootstrap_ip*, The bootstrap node’s IP address., 0.0.0.0, "Default value or user-defined."
    *bootstrap_port*, The port for a node's node-to-bootstrap and bootstrap-to-node communications within the *VIN™*., 8000, "Default value or user-defined."
    *kademlia_port*, The port through which a *VIN™* node communicates bi-directionally with the Kademlia network., 8080, "Default value or user-defined."
    *receipt_port*, The port through which a node within the *VIN™* communicates its cryptographic receipt., 9090, "Default value or user-defined."
    *http_port*, The port utilized for HTTP messages by a node within the *VIN™*., 9980, "Default value or user-defined."
    *lvm_port*, The port through which a *VIN™* node communicates with the LVM., 60001, "Default value or user-defined."
    *redundancy*, The number of holograms that will be produced from the original data shards. All of these will be placed on the network., 5, "Default value or user-defined. Lower redundancy leads to higher transmission speeds but lower data reliability/integrity."
    *log_datasize*, Enables the logging/storing of the size of the file being stored on the network., true, "true: enables logging of the data size.
    
    false: disables logging of the data size."
    *parallel_mode*, Enables the sending/receiving of data in parallel., true,  "true: data will be sent/received in parallel.
    
    false: data will be sent/received serially."
    *reconnect*, "Specifies whether or not a *VIN™* node will attempt to reconnect to the network upon errors/failures.", true, "true: enables reconnection attempts.
    
    false: disables reconnection attempts."
    *reconnect_time*, "The time, in seconds, between *VIN™* node reconnection attempts.", 60, "Default value or user-defined but must be, at minimum, one second."


chunker
=======

The following options pertain to the configuration of the chunkers used by the *VIN™*.

.. csv-table:: Chunker Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *log*, "Enables the logging/storing of the shards for inspection/debug purposes.", true, "true: enables logging of shards.
    
    false: disables logging of shards."
    *default_size*, "Specifies the default size of the chunks (shards), in bytes, that a file will be divided into before being distributed throughout the network.", 1500, "The default value of the chunk size. This can be over-ridden by the system optimization which will dynamically determine chunk sizes."
    *chunks_per_receipt*, "The number of chunks that can be recorded in any single cryptographic receipt.", 200, "Any number between 1 and To Be Determined (TBD). The recommended value is 200."
    *max_size*, "The maximum chunk size in bytes.", 50000, "As the minimum transmission unit (MTU) for most networks is 65kB, ensure that this parameter is set below this value. Note: if using an encoder(s) that inflate(s) chunk size, be sure the inflated size does not exceed the MTU."
    *min_size*, "The minimum chunk size in bytes.", 100, "When attempting to dynamically determine chunk size, this value sets the minimum optimal size for chunks."
    *default_number*, "When attempting to dynamically determine chunk size, this is the starting value of the number of chunks that the file will initially be split into. Note: depending on *min_size* and *max_size*, the final number of chunks may be less than or greater than this number.", 6, "The options vary depending on the *max_size*, *min_size* and the size of the files that are expected to be handled by the *VIN™*. The default is recommended for most cases." 

================================================


flags (*Linux*)
===============

Any flags utilized by the *VIN™* for a *Linux* operating system are listed in the table below.

.. csv-table:: Flag (Linux) Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *bootstrap*, "Sets the current *VIN™* node as a bootstrap node for a *Linux* OS.", false,	"true: set the node as bootstrap. 
    
    false: do not set the node as bootstrap."


win_flags (*Windows*)
=====================

Any flags utilized by the *VIN™* for a *Windows* operating system are listed in the table below.

.. csv-table:: Win_flag (Windows) Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *bootstrap*, "Sets the current *VIN™* node as a bootstrap node for a *Windows* OS.", true, "true: set the node as bootstrap. 
    
    false: do not set the node as bootstrap."

==========================================


files (*Linux*)
===============

The following options pertain to the locations of configuration and logs generated by the *VIN™* for a *Linux* operating system.

.. csv-table:: File (Linux) Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *base*, "The base location in the *VIN™* folder structure.", ``/opt/VIN/``, "Default value or user-defined."
    *config*, "The location of the configuration file is located here.", ``/etc/opt/VIN/``, "Default value or user-defined."
    *logs*, "The log files generated by the *VIN™* will be stored here.", ``/var/log/VIN/logs/``, "Default value or user-defined."
    *shards*, "The shards that are gathered are stored here.", ``/var/log/VIN/shards/``, "Default value or user-defined."
    *rebuilt*, "The storage location of the file that was rebuilt from the chunks (shards).", ``/opt/VIN/outputs/``, "Default value or user-defined."
    *kaddata*, "The location where *Kademlia* shards are stored if on-disk storage is enabled in the *VIN™*.", ``/opt/VIN/kademlia/data/``, "Default value or user-defined."
    *fuse_root*, "The mounted ``FUSE`` folder path. This directory must match directory where ``rvault`` is mounted.", ``/home/user/target/``, "Default or user-defined."


receipts (*Linux*)
------------------

The options below configure the location of the files/folders related to the cryptographic receipts utilized by the *VIN™* for a *Linux* operating system.

.. csv-table:: Receipt (Linux) Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *base*, "The base storage location of the cryptographic receipts used by the *VIN™*.", ``/opt/VIN/receipts/``, "Default value or user-defined."
    *received*, "The location of any received cryptographic receipts.", ``/opt/VIN/receipts/received/``, "Default value or user-defined."
    *sent*, "The location of any sent cryptographic receipts.", ``/opt/VIN/receipts/sent/``, "Default value or user-defined."


keys (*Linux*)
---------------

The configuration items below set the location of the files/folders associated with the public and private keys sent while using the *VIN™* for a *Linux* operating system.

.. csv-table:: Receipt (Linux) Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *base*, "The storage location for any public/private keys utilized by the *VIN™*.",	``/opt/VIN/keys/``, "Default value or user-defined."
    *crt*, "The location and name of the public key.", ``/opt/VIN/keys/self.crt``, "Default value or user-defined."
    *priv*, "The location and name of the private key.", ``/opt/VIN/keys/self.priv``, "Default value or user-defined."

======================================================


win_files (*Windows*)
=====================

The following options pertain to the locations of configuration and logs generated by the *VIN™* for a *Windows* operating system.

.. csv-table:: Win_file (Windows) Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *base*, "The base location in the *VIN™* folder structure.", "``\\VIN\\ (e.g., C:\ProgramData\VIN\)``", "Default value or user-defined."
    *config*, "The location of the configuration file is located here.", "``config\\ (e.g., C:\Program Files\Virgil\VIN\config\)``", "Default value or user-defined."
    *logs*, "The log files generated by the *VIN™* will be stored here.", "``logs\\ (e.g., C:\ProgramData\VIN\logs\)``", "Default value or user-defined."
    *shards*, "The shards that are gathered are stored here.", "``shards\\ (e.g., C:\ProgramData\VIN\shards\``", "Default value or user-defined."
    *rebuilt*, "The storage location of the file that was rebuilt from the chunks (shards).", "``outputs\\ (e.g., C:\ProgramData\VIN\outputs\)``", "Default value or user-defined."
    *kaddata*, "The location where *Kademlia* shards are stored if on-disk storage is enabled in the *VIN™*.", "``kademlia\\data\\ (e.g., C:\ProgramData\VIN\kademlia\data\)``", "Default value or user-defined."
    *fuse_root*, "The mounted ``FUSE`` folder path. This directory must match directory where ``rvault`` is mounted.", "``fuse\\ (e.g., C:\ProgramData\VIN\fuse\)``", "Default or user-defined."


receipts (*Windows*)
--------------------

The options below configure the location of the files/folders related to the cryptographic receipts utilized by the *VIN™* for a *Windows* operating system.

.. csv-table:: Receipt (Windows) Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *base*, "The base storage location of the cryptographic receipts used by the *VIN™*.", "``receipts\\ (e.g., C:\ProgramData\VIN\receipts\)``", "Default value or user-defined."
    *received*, "The location of any received cryptographic receipts.", "``receipts\\received\\ (e.g., C:\ProgramData\VIN\receipts\received\)``", "Default value or user-defined."
    *sent*, "The location of any sent cryptographic receipts.", "``receipts\\sent (e.g., C:\ProgramData\VIN\receipts\sent\)``", "Default value or user-defined."


keys (*Windows*)
----------------

The configuration items below set the location of the files/folders associated with the public and private keys sent while using the *VIN™* for a *Windows* operating system.

.. csv-table:: Key (Windows) Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *base*, "The storage location for any public/private keys utilized by the *VIN™*.", "``keys (e.g., C:\ProgramData\VIN\keys\)``", "Default value or user-defined."
    *crt*, "The location and name of the public key.", "``keys\\self.crt (e.g., C:\ProgramData\VIN\keys\self.crt)``", "Default value or user-defined."
    *priv*, "The location and name of the private key.", "``keys\\self.priv (e.g., C:\ProgramData\VIN\keys\self.priv)``", "Default value or user-defined."

======================================================


timeouts
========

These options allow for the configuration of various timeouts used to ensure the correct functionality of the *VIN™*.

.. csv-table:: Timeout Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *dht*, "The time (milliseconds) to wait before the failure of a request to/from the distributed hash table is confirmed.", 2000, "Default value or user-defined."
    *receipt*, "The time (microseconds) to wait before a failure on the sending side of the cryptographic receipt transmission is confirmed.", 600000000, "Default value or user-defined. Note: this must be greater than the reactor timeout."
    *reactor*, "The time (microseconds) to wait before a failure on the recipient side of the cryptographic receipt transmission is confirmed.", 3000000, "Default value or user-defined if required. Note: this must be lower than the receipt timeout."

===============================================================



pipelines
=========

This is the default pipeline configuration to be used if no "overwrite" per transaction file is provided. All encoders and decoders MUST be in the proper execution order. Usually this configuration will only contain a set of most likely used coders.

encoders
--------

The following configuration items allow for the customization of the various encoders used by the *VIN™*. Note: by utilizing various encoders in the *VIN™*, performance may be impacted.

.. csv-table:: Concurrent Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", ConcurrentEncoder, "Default value."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."
    *cw_size_2_pow*, "Code word size. Take the number as a power of 2. E.g., 2 :superscript:`15`", 15, "Default or user-defined."
    *msg_len*, "The length of encoded message in bits. All messages are to be divisible by this number.", 1000, "Default or user-defined."
    *red_bits*, "The number redundancy bits per message.", 30, "Default or user-defined."
    *cw_density*, "The number of encoded messages per code word.", 0.33, "Default or user-defined."


.. csv-table:: Entanglement Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", EntanglementEncoder, "Default value."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Naming Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", NamingEncoder, "Default value."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Validation Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", ValidationEncoder, "Default value."
    *id*, "Errors related to this encoder will be stored under this id name.", "network_data", "Default or user-defined."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


channels
--------


decoders
--------

The following configuration items allow for the enabling/disabling and customization of the various decoders used by the *VIN™*.

.. csv-table:: Validation Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", ValidationDecoder, "Default value."
    *id*, "Errors related to this encoder will be stored under this id name.", "network_data", "Default or user-defined."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Entanglement Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", EntanglementDecoder, "Default value."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Concurrent Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", ConcurrentDecoder, "Default value."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


pipelines_full
==============

This section will contain the full pipeline configuration (all encoders and decoders available). All encoders and decoders MUST be in the proper execution order. This section is used during the pipeline validation step and is used also for unit tests. If any new coder is developed, it must be added in this section.

encoders
--------

The following configuration items allow for the customization of the various encoders used by the *VIN™*. Note: by utilizing various encoders in the *VIN™*, performance may be impacted.

.. csv-table:: Alpha-Entanglement Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", AlphaEntEncoder, "Default value."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Cipher Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", CipherEncoder, "Default value."
    *bits*, "The size of the key used by the cipher coder algorithm.", 256, "128, 192, or 256."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Pipeline Prep Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", PipelinePreEncoder, "Default value."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Concurrent Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", ConcurrentEncoder, "Default value."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."
    *cw_size_2_pow*, "Code word size. Take the the number as a power of 2. E.g., 2 :superscript:`15`", 15, "Default or user-defined."
    *msg_len*, "The length of encoded message in bits. All messages are to be divisible by this number.", 1000, "Default or user-defined."
    *red_bits*, "The number redundancy bits per message.", 30, "Default or user-defined."
    *cw_density*, "The number of encoded messages per code word.", 0.33, "Default or user-defined."


.. csv-table:: Entanglement Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", EntanglementEncoder, "Default value."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Naming Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", NamingEncoder, "Default value."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Polar Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", PolarEncoder, "Default value."
    *frames*, "The number of K-byte segments in the message to be encoded (is not currently implemented in the Polar Encoder).", "1", "Default or user-defined."
    "N", "The number encoded bits resulting form a portion of the message (K) being encoded.", "128", "Default or user-defined (powers of 2). It must adhere to the reliability sequence of the coder."
    "K", "A portion, in bits, of the message to be encoded.", "32", "Default or user-defined. It must be less than N."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Reed-Solomon Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", ReedSolomonEncoder, "Default value."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Reed-Solomon Block Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", RSBlockEncoder, "Default value."
    *perc_parity*, "The percentage of parity bytes created per data byte. Every two parity bytes can find and correct a single corrupted byte among a set of bytes. Note: Not every parity byte can correct every data byte. Each parity byte only 'covers' for a certain set of data bytes.", 100, "0 – 100; where a higher number improves data recovery. The default is recommended."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Validation Encoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the encoder.", ValidationEncoder, "Default value."
    *id*, "Errors related to this encoder will be stored under this id name.", "network_data", "Default or user-defined."
    *log*, "Enables/disables log generation for the output of the encoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


channels
--------

.. csv-table:: Binary Symmetric Channel (BSC) Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the channel.", BSCChannel, "Default value."
    *log*, "Enables/disables log generation for the output of the channel.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."
    *p*, "The percentage of bits that will be flipped during transmission.", 1.0, "Any number between 0 and 100."
    *symbol_size*, "The symbol size of either bits (1) or bytes (8), which is affected by the 'bsc_p.' For example, if 'bsc_p' is 1.0 and 'bsc_sym_size' is set to 1, 1% of bits will be flipped. If 'bsc_sym_size' is 8, 1% of bytes will be flipped.", 8, "1 or 8." 


.. csv-table:: Jammer Channel Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the channel.", JammerChannel, "Default value."
    *log*, "Enables/disables log generation for the output of the channel.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."
    *p*, "The percentage of bits that will be flipped during transmission.", 1.0, "Any number between 0 and 100."
    *symbol_size*, "The symbol size of either bits (1) or bytes (8), which is affected by the 'bsc_p.' For example, if 'bsc_p' is 1.0 and 'bsc_sym_size' is set to 1, 1% of bits will be flipped. If 'bsc_sym_size' is 8, 1% of bytes will be flipped.", 8, "1 or 8." 


decoders
--------

The following configuration items allow for the customization of the various decoders used by the *VIN™*. Note: be sure that the decoder parameters match the encoder parameters; otherwise the *VIN™* will not function as expected.

.. csv-table:: Validation Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", ValidationDecoder, "Default value."
    *id*, "Errors related to this encoder will be stored under this id name.", "network_data", "Default or user-defined."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Reed-Solomon Block Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", RSBlockDecoder, "Default value."
    *perc_parity*, "The percentage of parity bytes created per data byte. Every two parity bytes can find and correct a single corrupted byte among a set of bytes. Note: Not every parity byte can correct every data byte. Each parity byte only 'covers' for a certain set of data bytes.", 100, "0 – 100; where a higher number improves data recovery. The default is recommended."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Reed-Solomon Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", ReedSolomonDecoder, "Default value."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Polar Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", PolarDecoder, "Default value."
    *frames*, "The number of K-byte segments in the message to be encoded (is not currently implemented in the Polar Encoder)", "1", "Default or user-defined."
    "N", "The number encoded bits resulting form a portion of the message (K) being encoded.", "128", "Default or user-defined (powers of 2). It must adhere to the reliability sequence of the coder."
    "K", "A portion, in bits, of the message to be encoded.", "32", "Default or user-defined. It must be less than N."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Entanglement Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", EntanglementDecoder, "Default value."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Concurrent Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", ConcurrentDecoder, "Default value."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Pipeline Prep Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", PipelinePreDecoder, "Default value."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


.. csv-table:: Cipher Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", CipherDecoder, "Default value."
    *bits*, "The size of the key used by the cipher coder algorithm.", 256, "128, 192, or 256."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."    


.. csv-table:: Alpha-Entanglement Decoder Parameters
    :header: Parameter, Description, Default, Options 
    :widths: 15 40 15 30
    :width: 100%

    *name*, "The name of the decoder.", AlphaEntDecoder, "Default value."
    *log*, "Enables/disables log generation for the output of the decoder.", false, "true: enables logging of the output. 
    
    false: enables logging of the output."


