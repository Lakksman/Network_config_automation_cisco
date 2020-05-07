# Network_config_automation_cisco
Code to connect to multiple switches and run multiple configuration files on Cisco L2,L3 Switches while checking for existing configurations.

Pyhton 3.5
The code checks file "devices" for ipaddresses of switches and establsishes connection to them in order. indivdual files with configuration such as ("configacl.cfg","ospf.cfg") could be created and referenced in file "filenames". 

While executing each configuration file will be read and checked for exisiting configurations, if no exisiting configurations are found configuration are written.


