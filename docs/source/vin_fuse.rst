
**************************************
Installing and using FUSE
**************************************

\1\. Building the project is a complex process requiring a number of dependency projects and libraries to be built. For this demo, a prebuilt ``DEB`` package is provided. Install the ``DEB`` file in a *Debian* system (tested in *Ubuntu*).


\2\. Unzip the provided *rvault* ``ZIP`` file. The document requires that you unzip under the ``$HOME/Dev/rvault`` folder so the root of the project is in that location. The project can be placed in any other place but the commands will need to be changed accordingly.

* Review the ``README.md`` document in the *rvault* project for complete information on how to setup/configure *rvault*. It should be noted that this is the *rvault* documentation and various things will differ from our implementation/enhancements of *rvault* which are tied to the *VIN™*.
* Make sure that the appropriate development libraries are installed:

  * ``sudo apt install -y libssl-dev``
  * ``sudo apt install -y libscrypt-dev``
  * ``sudo apt install -y libcurl3-dev``
  * ``sudo apt install -y libfuse-dev``
  * ``sudo apt install clang``
  * ``sudo apt install make``

  * If this is for use with *AWS* you will need to install the following as well:
    
    * ``sudo apt install pkg-config``

  * ``cd rvault/src``
  * ``make``

* Make sure that the *rvault* executable has been created (``ls -la``).
* Put *rvault* in ``/usr/local/bin`` using:

  * ``sudo ln -s $HOME/Dev/rvault/src/rvault /usr/local/bin/rvault``  (if ``$HOME`` is not supported use ``/home/<user>``)
  * ``ls -la /usr/local/bin/rvault``

* Validate that *rvault* is now in your path by running it with no options:

  * ``rvault``

* This should produce the help output from *rvault*. If it does not, you need to add ``/usr/local/bin`` to your path using the appropriate method for whatever shell you use.
* Make sure you have the UUID library:

  * ``sudo apt install -y uuid-dev``

* Create an *rvault* folder (folder name can be customized to suit). From your home folder:

  * ``mkdir my_vault``
  * ``export RVAULT_PATH=$HOME/my_vault``

* Create the folder that you will mount *rvault* into (folder name can be customized to suit):

  * ``mkdir target``

* Create the UUID unique to this *rvault*:

  * ``export UUID="uuidgen"``
  * An example of a valid looking ``"uuidgen"`` is ``0224f0cf-f453-43e1-b16e-124b15e4a64a``
  * NOTE: This is only done once at the creation of the *rvault* and is essentially a manner for initializing the vault.

* Mount the *rvault* (using the unique UUID which was generated in the previous command):

  * ``rvault create -n $UUID``
  * NOTE: It will ask you for a passphrase. For the purpose of the demo, etc., I have been using an empty passphrase (i.e. just hit **<enter>** twice)
  * You can look in the *rvault* folder (not to be confused with the target folder, to see that a few files have been created (e.g. ``rvault.error_log`` and ``rvault.metadata``)

* Mount the *rvault*:

  * ``rvault mount target``


\3\. Performing a Share with *rvault*:

* Ensure *VIN™* knows the location of your mounted *rvault* folder

  * Update the *VIN™* configuration file at ``/etc/opt/VIN/defaults.cfg`` such that the path under ``files -> fuse_root`` is the absolute path of your mounted fuse folder (default value is ``/home/user/target/``). If you used recommended example this will be ``home/<user>/target`` (change ``<user>`` with the actual user).

* Create a folder for sharing files:

  * ``cd target``
  * ``mkdir share``

* Start the *VIN™*  to be used with the *rvault*:

  * Only files copied into the share folder or a subfolder of share will trigger a *VIN™* share
  * Adding a peer to a folder can be done in two ways:

    * The *VIN CLI™* ``update_peer`` command adds a peer to a folder:

      * ``update_peer 192.0.2.0 9090 share/``

    * Alternatively the ``fuse_peers.cfg`` configuration file adds peers to folders on startup:

      * ``fuse_peers.cfg`` is a *JSON* file found in ``/etc/opt/VIN/`` 
      * The following ``fuse_peers.cfg`` is equivalent to running the *VIN CLI™* command ``update_peer 192.0.2.0 9090 share/``

      .. code-block:: json

        {
          "share": {
            "peers": ["192.0.2.0:9090"]
          }
        }

 
      * The default is (for ``VIN -a <bootstrap> -h 7071 -p 8081 -r 9091``):

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

* Copying a file, either through the *Navigator* interface or via standard commands (``cp``) into the target/share folder should start a share in the *VIN™* to the peer ``192.0.2.0:9090``. On a successful share the received file is saved on the peer machine (defaults location: ``/opt/VIN/outputs)``.

  * Example copy: ``cp somefile.txt /home/<user>/target/share``

\4\. Additional Features

* ``fuse_peers.cfg`` supports multiple peers per folder and creates folders on startup. For example:

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

* The above ``fuse_peers.cfg`` *JSON* is equal to executing the below console and *VIN CLI™* commands on startup:

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

\5\. Common Issues

* On non graceful exit of the *VIN™* the named semaphore ``sem.VIN_Fuse_Sem`` will sometimes not close properly. When copying a file to target/share this bug will cause the *VIN™* to produce no logging output when we would otherwise expect to see the *VIN™* perform a share. Shutting down the *VIN™* node and deleting the semaphore (``rm /dev/shm/sem.VIN_Fuse_Sem``) will resolve the issue.


..
  \6\. *VIN™* UI Demo

  * Unzip the provided *rvault* ``ZIP`` file. The document requires that you unzip under the ``$HOME/Dev/vin_demo_draft``.

  * Terminal 1

    * ``cd $HOME/Dev/vin_demo_draft``
    * ``sudo apt install -y npm``
    * ``npm i``
      
      * NOTE: If this fails to do an inability to get the issuer certificate locally, you can run the command:

        * ``npm config set strict-ssl false`` before retrying the previous command (``npm -i``).

      * NOTE: "npm ERR! The unauthenticated git protocol on port 9418 is no longer supported." will sometimes appear and can be fixed by modifying the url of the git repository. Try the command ``git config --global url."https://".insteadOf git://`` or, ``git config url."https://".insteadOf git://``.  

    * ``npm start``
    * This will enable you to access the demo at the URL: ``http://localhost:3000/dashboard``

  * Terminal 2

    * ``npx serve /opt/VIN/outputs -p 5000``
    * This will enable you to access the list of files available (from ``/opt/VIN/outputs``) at the URL: ``http://localhost:5000/``
