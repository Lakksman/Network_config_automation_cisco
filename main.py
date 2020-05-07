from napalm import get_network_driver
from getpass import getpass

with open ("devices") as iplist:
	for ip in iplist:
		ip=ip.strip()

		username=input("Username :")
		password=getpass("Password :")

		connect=get_network_driver(ios)
		switch=connect(ip,username,password)
		print("Establishing connection to "+str(ip))
		switch.open()
		print("Connected to "+str(ip))

		with open ("filenames") as filelist:
			for file in filelist:
				file=file.strip()
				print("loading "+file)
				switch.load_merge_candidate(file)
				compare=switch.compare_config()
				if len(compare) > 0:
					print("Configuration required")
					switch.commit_config()
				else:
					print("Configuration not required")
					switch.discard_config()
		switch.close()
