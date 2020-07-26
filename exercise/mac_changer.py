
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) =  parser.parse_args()
    if not options.interface:
        # code to handle error
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify an interface, use --help for more info.")
        # code to handle error
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC adddress for " + interface + " to " + new_mac)

    # Set interface down
    subprocess.call(["ifconfig", interface, "down"])

    # change mac address
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    # Set interface up
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output (["ifconfig", interface])
    mac_address_search_result = re.search(rb'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Couldn't read mac address \n")


options = get_arguments()

old_mac = get_current_mac(options.interface)

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if old_mac == current_mac:
    print("[+] MAC address was successfully changed to " + str(current_mac))
else:
    print("[-] MAC address did not get changed.")
