# Juniper-vlab-BGP

Script renders the Junos BGP config file using Jinja2 template

Attempts to login multiple device

Takes the backup of existing config

Pushes the updated config

Fetches BGP Neighborship Status 

Prints the BGP Status and BGP Route table output

**Sample Output**

inbelnaveenk:bgp-testing rishabh.parihar$ python3 bgp-test-vlab.py
####################################################################################################
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Trying to access remote MX router.....
>>>>SSH Successful

Taking Backup of Existing Router config(before change)....
>>>>Backup is saved in your current directly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below config is getting pushed....

set routing-instances vrf-test instance-type virtual-router

set interfaces ge-0/0/0 unit 0 family inet address 10.100.24.2/24
set interfaces ge-0/0/3 unit 0 family inet address 10.100.46.1/24

set routing-instances vrf-test interface ge-0/0/0
set routing-instances vrf-test interface ge-0/0/3

set routing-instances vrf-test routing-options autonomous-system 64533
set routing-instances vrf-test protocols bgp group ebgp type external
set routing-instances vrf-test protocols bgp group ebgp neighbor 10.100.24.1 local-address 10.100.24.2
set routing-instances vrf-test protocols bgp group ebgp neighbor 10.100.24.1 peer-as 64522
set routing-instances vrf-test protocols bgp group ebgp neighbor 10.100.46.2 multihop ttl 2
set routing-instances vrf-test protocols bgp group ebgp neighbor 10.100.46.2 local-address 10.100.46.1
set routing-instances vrf-test protocols bgp group ebgp neighbor 10.100.46.2 peer-as 64544
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

>>>>>>>>Config is committed<<<<<<<<

Trying to fetch BGP Status. Please Wait......

***************************************************************************
'BGP Peer Address is : 10.100.24.1'
'BGP Peer AS is : 64522'
'BGP Peer Elapsed Time is : 1'
'BGP Peer State is : Established'
***************************************************************************
***************************************************************************
'BGP Peer Address is : 10.100.46.2'
'BGP Peer AS is : 64544'
'BGP Peer Elapsed Time is : 1'
'BGP Peer State is : Established'
***************************************************************************

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Route-Received AS-Path Next-Hop/Peer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
0.0.0.0/0 64522 I 10.100.24.1
10.100.13.0/24 64522 I 10.100.24.1
10.100.100.1/32 64522 I 10.100.24.1
10.100.100.3/32 64522 I 10.100.24.1
10.100.100.5/32 64544 I 10.100.46.2

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>>>To Neighbor: 10.100.24.1
Route-Advertised AS-Path Next-Hop/Peer
10.100.100.5/32 64544 I Self

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

>>>>To Neighbor: 10.100.46.2
Route-Advertised AS-Path Next-Hop/Peer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
0.0.0.0/0 64522 I Self
10.100.13.0/24 64522 I Self
10.100.100.1/32 64522 I Self
10.100.100.3/32 64522 I Self
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Total time taken is 20.253286838531494
