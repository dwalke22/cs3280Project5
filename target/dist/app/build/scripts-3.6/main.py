#!python
"""
Script for calculating the subnet for an IP and mask

Subnet Calculation
Given an IP address (IPv4 or IPv6) and mask
a bitwise-And calculation will be performed.
"""
import re
import utils

__author__ = "David Walker"
__version__ = "Fall 2020"

def calculate_subnet_ipv4(ip_address, net_mask):
    """Calculates the subnet for an IPv4 address"""
    subnet_message = ""
    if utils.verify_netmask(net_mask):
        if not "." in net_mask:
            mask = utils.convert_netmask(net_mask)
            subnet = utils.calculate_ipv4_subnet(ip_address, mask)
            subnet = "Subnet for IP: %s with netmask: %s is: %s" % (ip_address, mask, subnet)
        else:
            subnet = utils.calculate_ipv4_subnet(ip_address, net_mask)
            message_list = (ip_address, net_mask, subnet)
            subnet_message = """Subnet for IP: %s with netmask: %s is: %s""" % message_list
    else:
        subnet_message = "Net Mask is not Real"
    return subnet_message

def calculate_subnet_ipv6(ip_address, net_mask):
    """Calculates the subnet for an IPv6 address"""
    subnet = ""
    if utils.verify_netmask(net_mask):
        subnet = "Calculating with ip " + ip_address
    else:
        subnet = "Net Mask is not Real"
    return subnet

def main(ip_address, net_mask):
    """Main entry point of prgram."""
    letter_regex = re.compile(r'[a-zA-Z:]')
    if ip_address is None:
        raise ValueError('IP Adress cannot be None.')
    if net_mask is None:
        raise ValueError('Net Mask cannot be None.')
    if letter_regex.search(ip_address):
        if utils.verify_ipv6(ip_address):
            return calculate_subnet_ipv6(ip_address, net_mask)
        return "s% is not a Valid IP" % ip_address
    if utils.verify_ipv4(ip_address):
        return calculate_subnet_ipv4(ip_address, net_mask)
    return "%s Not Valid IP" % ip_address

if __name__ == "__main__":
    exec(open('service.py').read())
