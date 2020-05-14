#! /usr/bin/env python

from pprint import pprint
from jinja2 import Environment, FileSystemLoader
from jnpr.junos import Device 
from jnpr.junos.utils.config import Config 
from jnpr.junos.factory.factory_loader import FactoryLoader
from lxml import etree
import yaml 
import time
from jnpr.junos.op.bgp import *
import sys
import threading
from datetime import datetime


dict1 = yaml.safe_load(open('template_vars.yml'))

def upload_template():
	
	#print(type(dict1))
	#print(dict1)

	baseline = ENV.get_template("bgp-template2.j2")
	config = baseline.render(dict1)
	f = open('updated-config.conf', 'w')
	f.write(config)
	
	print("\nBelow config is getting pushed....")
	print('~' * 100)
	print(config)
	print('~' * 100)
	f.close()

	try:
		cfg.load(path="updated-config.conf", format='set', merge=True)
	except Exception as e:
		print("Exception Raised while loading config")
		print(e)
		sys.exit()
	try:
		if cfg.commit_check():
			cfg.commit()
			print("\n>>>>>>>>Config is committed<<<<<<<<")
		else:
			print("Error while pushing config")
			a_device.close()
	except Excetion as e:
		print(e)
		print("Error while pushing config")
		a_device.close()

"""
get_conf = a_device.rpc.get_config(options={'format':'text'}, normalize=True)
print(etree.tostring(get_conf, encoding='unicode', pretty_print=True))
"""
def conf_backup(a_device):
	print("Taking Backup of Existing Router config(before change)....")
	datestring = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
	f = open('junos_backup_' + datestring + '.conf', 'w')
	config_bck = a_device.cli('show configuration | display set')
	f.write(config_bck)
	f.close()
	print(">>>>Backup is saved in your current directly\n")

"""
get_conf1 = a_device.rpc.get_config({'format':'text'})
print(get_conf1)
"""
#print(type(open('bgp.yml').read()))
"""
def bgp_status():
	print("\nTrying to fetch BGP Status.Please Wait......\n")
	time.sleep(6)
	globals().update(FactoryLoader().load(yaml.safe_load(open('bgp.yml').read())))
	bgp1=BGPNeighborTable(cfg)
	fields = bgp1.get()
	for field in fields:
		print('*' * 73)
		print("Adjacency with Neighbor {} is {}.\nPeer-type is {} and Peer-AS is {}".format(field.neighbor[:-4], field.state, field.type, field.peer_as))
		
	print('*' * 73)

"""	


def bgp_status(a_device):
##Below code does the same work as above. Hence, using one
	print("\nTrying to fetch BGP Status. Please Wait......\n")
	#time.sleep(6)
	bgp_sum = a_device.rpc.get_bgp_summary_information({'format':'json'}, instance=str(dict1['customer_vrf']), dev_timeout=55)
	#print(type(bgp_sum))
	#pprint(bgp_sum)
	bgp_scrapped = bgp_sum['bgp-information'][0]['bgp-peer']
	for i in range(len(bgp_scrapped)):
		print('*' * 75)
		pprint("BGP Peer Address is : {}".format(bgp_scrapped[i]['peer-address'][0]['data']))
		pprint("BGP Peer AS is : {}".format(bgp_scrapped[i]['peer-as'][0]['data']))
		pprint("BGP Peer Elapsed Time is : {}".format(bgp_scrapped[i]['elapsed-time'][0]['data']))
		time.sleep(0.9)
		pprint("BGP Peer State is : {}".format(a_device.rpc.get_bgp_summary_information({'format':'json'}, instance='vrf-test', dev_timeout=55)['bgp-information'][0]['bgp-peer'][i]['peer-state'][0]['data']))
		print('*' * 75)


##Receive Route Table
def rx_bgp_rt(a_device):
	bgp_route = a_device.rpc.get_route_information({'format':'json'}, receive_protocol_name='bgp', table=str(dict1['customer_vrf']+".inet.0"), active_path=True)
	#pprint(bgp_route)
	bgp_route_scrapped = bgp_route['route-information'][0]['route-table'][0]['rt']
	#pprint(bgp_route_scrapped)
	print("\n")
	print('~' * 62)
	print("{: >20} {: >20} {: >20}".format("Route-Received", "AS-Path", "Next-Hop/Peer"))
	print('~' * 62)
	for i in range(len(bgp_route_scrapped)):
		print("{: >20} {: >20} {: >20}".format(bgp_route_scrapped[i]['rt-destination'][0]['data'], bgp_route_scrapped[i]['rt-entry'][0]['as-path'][0]['data'], bgp_route_scrapped[i]['rt-entry'][0]['nh'][0]['to'][0]['data']))

##Advertise Route 
"""
temp_list = []
temp_list.append(dict1['remote_a'])
temp_list.append(dict1['remote_b'])
for i in temp_list:
	bgp_route = a_device.rpc.get_route_information({'format':'json'}, advertising_protocol_name='bgp', table=str(dict1['customer_vrf']+".inet.0"), neighbor=str(i), active_path=True)
	#pprint(bgp_route)
	bgp_route_scrapped = bgp_route['route-information'][0]['route-table'][0]['rt']
	#pprint(bgp_route_scrapped)
	print("\n")
	print('~' * 60)
	print(">>>>To Neighbor: {}".format(i))
	print("{: >20} {: >20} {: >20}".format("Route-Advertised", "AS-Path", "Next-Hop/Peer"))
	print('~' * 60)
	for i in range(len(bgp_route_scrapped)):
		print("{: >20} {: >20} {: >20}".format(bgp_route_scrapped[i]['rt-destination'][0]['data'], bgp_route_scrapped[i]['rt-entry'][0]['as-path'][0]['data'], bgp_route_scrapped[i]['rt-entry'][0]['nh'][0]['to'][0]['data']))
"""


def tx_bgp_rt(i):
	bgp_route = a_device.rpc.get_route_information({'format':'json'}, advertising_protocol_name='bgp', table=str(dict1['customer_vrf']+".inet.0"), neighbor=str(i), active_path=True)
	#pprint(bgp_route)
	bgp_route_scrapped = bgp_route['route-information'][0]['route-table'][0]['rt']
	#pprint(bgp_route_scrapped)
	print("\n")
	print('~' * 62)
	print(">>>>To Neighbor: {}".format(i))
	print("{: >20} {: >20} {: >20}".format("Route-Advertised", "AS-Path", "Next-Hop/Peer"))
	print('~' * 62)
	for i in range(len(bgp_route_scrapped)):
		print("{: >20} {: >20} {: >20}".format(bgp_route_scrapped[i]['rt-destination'][0]['data'], bgp_route_scrapped[i]['rt-entry'][0]['as-path'][0]['data'], bgp_route_scrapped[i]['rt-entry'][0]['nh'][0]['to'][0]['data']))




if __name__ == "__main__":
	t = time.time()
	ENV = Environment(loader=FileSystemLoader('.'))
	print('#' * 100)
	print("Trying to access remote MX router.....")
	try:
		a_device = Device(host="66.129.235.12", user="aryaka", password="aryaka@123", port="32012", timeout=5)
		a_device.open(normalize=True)
		cfg = Config(a_device)
		print(">>>>SSH Successful\n")
	#except ConnectError as err:
	#	print("Cannot connect to device {}".format(err))
	#	sys.exit()
	except Exception as e:
		print(e)
		sys.exit("Exception raised while initiating SSH connection.")


	conf_backup(a_device)

	upload_template()

	bgp_status(a_device)
		
	rx_bgp_rt(a_device)

	thread1 = threading.Thread(target=tx_bgp_rt, args=(dict1['remote_a'],))
	thread1.start()
	thread2 = threading.Thread(target=tx_bgp_rt, args=(dict1['remote_b'],))
	thread2.start()
	thread1.join()
	thread2.join()
	print("\nTotal time taken is {}".format(time.time()-t))
	a_device.close()

