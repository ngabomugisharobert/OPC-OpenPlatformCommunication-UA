# OPC-OpenPlatformCommunication-UA
OPC UA set up server and client

<h1>WHAT IS OPC?</h1>
*******************

Open Platform Communications is a series of standards and specifications for industrial telecommunication.


<h2>INSTALLATION OF REQUIRED SOFTWARE</h2>
****************************************

first of all you have to install python 

With pip (note: the package was ealier called opcua)
windows:

    pip install freeopcua       #make sure python is installed
    pip install cryptography       #make sure python is installed

Ubuntu:

    apt install python-opcua        # Library
    apt install python-opcua-tools  # Command-line tools

<h4>Dependencies:</h4>

    Python > 3.4: cryptography, dateutil, lxml and pytz.
    Python 2.7 or pypy < 3: you also need to install enum34, trollius (asyncio), and futures (concurrent.futures), with pip for example.


<h4>Client</h4>

What works:

    connection to server, opening channel, session
    browsing and reading attributes value
    getting nodes by path and nodeids
    creating subscriptions
    subscribing to items for data change
    subscribing to events
    adding nodes
    
<h4>Server</h4>

What works:

    creating channel and sessions
    read/set attributes and browse
    getting nodes by path and nodeids
    autogenerate address space from spec
    adding nodes to address space
    datachange events
    events
    methods
