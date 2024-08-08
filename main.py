import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
(user_input, arguments) = parse_object.parse_args()

user_interface = user_input.interface
user_mac_address = user_input.mac_address

print("Mac Changer Started!")

subprocess.call(["ifconfig", user_interface, "down"])
subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
subprocess.call(["ifconfig", user_interface, "up"])

print("Mac Changer Finished!!!")

#You need to type "python main.py" in the terminal and then write your connection name "--interface",
# for "--mac" you need to write the mac address you want to change.
# It is stated below as an example.
#You can copy the code for your terminal.
#####      python main.py --interface eth0 --mac 00:11:22:33:44:55     #####
#Thanks!!!#