# OPC-OpenPlatformCommunication-UA
OPC UA set up server and client


WHAT IS OPC?
*******************

Open Platform Communications is a series of standards and specifications for industrial telecommunication.


INSTALLATION OF REQUIRED SOFTWARE
****************************************

first of all you have to install python 

With pip (note: the package was ealier called opcua)

pip install freeopcua

Ubuntu:

apt install python-opcua        # Library
apt install python-opcua-tools  # Command-line tools

Dependencies:

    Python > 3.4: cryptography, dateutil, lxml and pytz.
    Python 2.7 or pypy < 3: you also need to install enum34, trollius (asyncio), and futures (concurrent.futures), with pip for example.

Documentation

Client

What works:

    connection to server, opening channel, session
    browsing and reading attributes value
    getting nodes by path and nodeids
    creating subscriptions
    subscribing to items for data change
    subscribing to events
    adding nodes
    
Server

What works:

    creating channel and sessions
    read/set attributes and browse
    getting nodes by path and nodeids
    autogenerate address space from spec
    adding nodes to address space
    datachange events
    events
    methods
