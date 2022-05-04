.. _vin-install-fuse:

**************************************
Installing and using FUSE
**************************************

This document will provide instructions on testing *VIN™* nodes with *rvault*. It requires that *VIN™* be installed on a minimum of three nodes (one bootstrap and two peers). Before beginning with this procedure, please follow the instructions in :ref:`vin-install` and :ref:`running-the-vin-linux` (or :ref:`running-the-vin-windows`) to gain a better understanding of the *VIN™* and its functionality.


Installing the VIN™
====================

Note: if the :ref:`vin-install` section was followed, *VIN™* will already be installed and the steps in this subsection may be skipped. 

Building the project is a complex process requiring a number of dependency projects and libraries to be built. For this demo, a prebuilt ``DEB`` package is provided. Install the ``DEB`` file in a *Debian* system (tested in *Ubuntu*) using the following:

* Navigate to the folder containing the ``DEB`` file on the system and run:  

  * ``sudo dpkg -i <deb_name>.deb``, where ``<deb_name>`` is the name of the file (e.g., ``QToken-CPP_1.12.3-x86_64.deb``).

* Note: If installing the *VIN™* on a system with a previous installation, ``dpkg`` may produce errors regarding overwriting files. Make a backup of those files and then run the following command to do the upgrade:

  * ``sudo dpkg -i --force-overwrite <deb_name>.deb``, where ``<deb_name>`` is the name of the file (e.g., ``QToken-CPP_1.12.3-x86_64.deb``).

To ensure the *VIN™* is directed to the required libraries run:

* ``echo "export LD_LIBRARY_PATH=/usr/local/lib:/usr/lib" > ~/.profile``
* ``export LD_LIBRARY_PATH=/usr/local/lib:/usr/lib`` 

Note: You will need to merge configuration files manually. At this point in time the configuration file format does not update itself.


Setting up rvault
=================

The document requires that you unzip he provided *rvault* ``ZIP`` file under the ``~/Dev`` folder. The project can be placed in any location but the commands will need to be changed accordingly. To unzip the file with the recommended folder structure, complete the following:

* ``mkdir ~/Dev``
* ``unzip "dir" -d ~/Dev``, where ``"dir"`` is the file path (including file name) of the *rvault* ``ZIP`` file (e.g., ``/tmp/rvault-master.zip``).
* Install the appropriate development libraries by running:

  * ``sudo apt install -y libssl-dev libscrypt-dev libcurl3-dev libfuse-dev clang make pkg-config uuid-dev``
  * ``cd ~/Dev/rvault-master/src``
  * ``make``

* Be sure that the *rvault* executable has been created by running ``ls -l rvault``.
* Place *rvault* in ``/usr/local/bin`` using:

  * ``sudo cp rvault /usr/local/bin/rvault``
  * Run ``ls -la /usr/local/bin/rvault`` to validate the above command

* Validate that *rvault* is now in your path by running it with no options:

  * ``rvault`` should list options and commands available to *rvault*

* This should produce the ``help`` output from *rvault*. If it does not, ``/usr/local/bin`` must be added to the system path using the appropriate method for whichever shell is in use.
* Create an *rvault* folder (the folder name can be customized by user preference. The example below uses ``my_vault``).

  * ``export RVAULT_PATH=~/my_vault``
  * ``mkdir $RVAULT_PATH``

* Create the folder that you will mount *rvault* into (the folder name can be customized by user preference. The example below uses ``target``):

  * ``export TARGET_PATH=~/target``
  * ``mkdir $TARGET_PATH``

* Create the UUID unique to this *rvault*:

  * ``export UUID=`uuidgen```
  * ``echo $UUID > ~/rvault.uuid.txt``
  * Note: This is only done once at the creation of the *rvault* and is essentially a manner for initializing the vault.

* Mount *rvault* (using the unique UUID which was generated in the previous command):

  * ``rvault create -n $UUID``
  * Note: It will ask you for a passphrase. For the purpose of the demo, an empty passphrase will suffice (i.e. just hit **enter** twice).
  * To confirm the completion of the above command run ``ls -l $RVAULT_PATH``. THe ``rvault.error_log`` and ``rvault.metadata`` files should be listed.

* Mount the *rvault*:

  * ``rvault mount $TARGET_PATH``
  * If prompted for a passphrase, hit **enter** as no passphrase was set during the previous step.


Performing a SHARE with *rvault*
=======================================

This section details instructions to perform a ``SHARE`` using *rvault* with the *VIN™*. Three nodes will be required: a bootstrap, the sharing node and the receiving node.

* Ensure *VIN™* is aware of the location of the mounted *rvault* folder:

  * Update the *VIN™* configuration file at ``/etc/opt/VIN/defaults.cfg`` such that the path under ``files -> fuse_root`` is the absolute path of the mounted fuse folder (the default value is ``~/target/``). If you used the recommended setting this will be ``$TARGET_PATH`` but the full path must be explicitly specified in the configuration file.

  * Run ``echo $TARGET_PATH`` to output the full path (e.g., it should be similar to ``/home/<user_name>/target``)
  * Replace ``/home/user/target/`` under ``files -> fuse_root`` in the ``defaults.cfg`` file with the output from the above command.

* Create a folder for sharing files:

  * ``cd $TARGET_PATH``
  * ``mkdir share``


* The test will require the instantiation of three separate nodes (one bootstrap and two *VIN™* nodes). To accomplish this, please refer to the instructions listed in :ref:`running-the-vin-linux` (or :ref:`running-the-vin-windows`) for the required operating system and be sure to record which nodes are bootstrap, sharing and receiving. Note: the method described in these documents sets up the bootstrap node on the same host as a *VIN™* node. If required, the bootstrap may be run on a node separate from the *VIN™* node.
* To add a peer to a shareable folder, in another terminal window, start the *VIN™ CLI* and connect it to the node that will be sharing the file by running:
  
  * ``VIN_CLI <ip_addr_share> <http_port_share>``, where ``<ip_addr_share>`` and ``<http_port_share>`` are the IP address and HTTP port of the sharing node, respectively. If running the VIN with default settings ``<http_port_share>`` will be ``7070``.

* In the *VIN™ CLI* terminal, run: 

  * ``update_peer <ip_add_rec> <recp_port_rec> share/``, where ``<ip_add_rec>`` and ``<recp_port_rec>`` are the IP address and Receipt port of the receiving node, respectively. If running the *VIN™* with default settings, ``<recp_port_rec>`` will be ``9090``.
  * Note: only files copied into the ``share/`` folder or a subfolder of ``share/`` will trigger a *VIN™* ``SHARE``.

* Alternatively, adding a peer to a shareable folder may be accomplished by modifying ``fuse_peers.cfg`` before running the sharing *VIN™* and is detailed below:

  * Navigate to the ``fuse_peers.cfg`` folder location (by default it is ``/etc/opt/VIN/``) and open ``fuse_peers.cfg``. By default it will contain the following:

  .. code-block:: json

    {
      "share": {
          "peers": [],

            "localhost-9091": {
              "peers": [
                "127.0.0.1:9091"
              ]
          }
      }
    }
    
  * Modify it to look as follows:

  .. code-block:: json

    {
      "share": {
        "peers": ["<ip_add_rec>:<recp_port_rec>"]
      }
    }

  * Where ``<ip_add_rec>`` and ``<recp_port_rec>`` are the IP address and Receipt port of the receiving node, respectively. If running the *VIN™* with default settings, ``<recp_port_rec>`` will be ``9090``.
  * The result is the same as running ``update_peer <ip_add_rec> <recp_port_rec> share/`` within *VIN™ CLI*.


* Copying a file, either through the *Navigator* interface or via standard commands (e.g., ``cp <test_file.txt> $TARGET_PATH/share``) into the ``$TARGET_PATH/share`` folder will start a share from the sharing *VIN™* node to the receiving node. 
* On a successful share, the received file is saved on the receiving node system (the default location is ``/opt/VIN/outputs``).


Fuse Peers Configuration File
==============================

* ``fuse_peers.cfg`` supports multiple receiving peers per folder and creates the shared folders when starting a *VIN™* node. 
* As an example, a ``fuse_peers.cfg`` file containing the following:

.. code-block:: json

  {
    "share": {
        "peers": ["192.0.2.0:9090"],

        "local_peers": {
          "peers": [
              "127.0.0.1:9091"
          ]
        },

        "virgil_peers": {
          "canada": {
              "peers": [
                "203.0.113.0:9090",
                "203.0.113.255:9090"
              ]
          },

          "usa": {
              "peers": [
                "192.0.2.255:9090"
              ]
          }
        }
    }
  }

* Would be the same as running *VIN CLI™* commands listed below:

* Folder creation:

  * ``mkdir target/share/local_peers``
  * ``mkdir target/share/virgil_peers``
  * ``mkdir target/share/virgil_peers/canada``
  * ``mkdir target/share/virgil_peers/usa``

* *VIN CLI™*:

  * ``update_peer 192.0.2.0 9090 share/``
  * ``update_peer 127.0.0.1 9091 share/local_peers``
  * ``update_peer 203.0.113.0 9090 share/virgil_peers/canada``
  * ``update_peer 203.0.113.255 9090 share/virgil_peers/canada``
  * ``update_peer 192.0.2.255 9090 share/virgil_peers/usa``


Common Issues
===============

* On non graceful exit of the *VIN™* the named semaphore ``sem.VIN_Fuse_Sem`` will sometimes not close properly. When copying a file to target/share this bug will cause the *VIN™* to produce no logging output when we would otherwise expect to see the *VIN™* perform a share. Shutting down the *VIN™* node and deleting the semaphore (``rm /dev/shm/sem.VIN_Fuse_Sem``) will resolve the issue.


..
  \6\. *VIN™* UI Demo

  * Unzip the provided *rvault* ``ZIP`` file. The document requires that you unzip under the ``~/Dev/vin_demo_draft``.

  * Terminal 1

    * ``cd ~/Dev/vin_demo_draft``
    * ``sudo apt install -y npm``
    * ``npm i``
      
      * Note: If this fails to do an inability to get the issuer certificate locally, you can run the command:

        * ``npm config set strict-ssl false`` before retrying the previous command (``npm -i``).

      * Note: "npm ERR! The unauthenticated git protocol on port 9418 is no longer supported." will sometimes appear and can be fixed by modifying the url of the git repository. Try the command ``git config --global url."https://".insteadOf git://`` or, ``git config url."https://".insteadOf git://``.  

    * ``npm start``
    * This will enable you to access the demo at the URL: ``http://localhost:3000/dashboard``

  * Terminal 2

    * ``npx serve /opt/VIN/outputs -p 5000``
    * This will enable you to access the list of files available (from ``/opt/VIN/outputs``) at the URL: ``http://localhost:5000/``
