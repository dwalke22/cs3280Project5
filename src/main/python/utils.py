#!/usr/bin/env python3
"""
Provides utility method for bitwises-Add
"""
import re


def verify_ipv6(ip_address):
    """Verifies that the ip is a valid IPv6 address"""
    ip_regex = re.compile(r"""^(?:[A-F0-9]{1,4}:){6}(?:[A-F0-9]{1,4}:
            [A-F0-9]{1,4}|(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)
            {3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))$""", re.X)
    return ip_regex.match(ip_address)


def verify_ipv4(ip_address):
    """Verifies that the ip is a vaild IPv4 address"""
    ip_regex = re.compile(r"""^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
            (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$""", re.X)
    return ip_regex.match(ip_address)


def verify_netmask(net_mask):
    """Verifies that the net mask is vaild"""
    net_regex = re.compile(r"""(?:^(0?[1-9]|[12][0-9]|3[0-2])$)
            |^(?:(?:255\.)(?:0|128|192|224|240|248|252|254|255\.)
            (?:0|128|192|224|240|248|252|254|255)\.)
            (?:0|128|192|224|240|248|252|254|255)$""", re.X)
    return net_regex.search(net_mask)


def convert_netmask(net_mask):
    """Converts a net mask to IPv4"""
    ones = int(net_mask)
    zeros = 32 - ones
    mask = ("1" * ones) + ("0" * zeros)
    bits = [mask[i:i+8] for i in range(0, len(mask), 8)]
    n_mask = ""
    for bit in bits:
        if n_mask.count(".") == 3:
            n_mask += str(int(bit, 2))
        else:
            n_mask += str(int(bit, 2)) + "."
    return n_mask


def calculate_ipv4_subnet(ip_address, net_mask):
    """Calculates the subnet of an IPv4 address"""
    ip_bits = ip_address.split(".")
    net_bits = net_mask.split(".")
    subnet = ""
    for bit in range(4):
        ip_bit = int(ip_bits[bit])
        net_bit = int(net_bits[bit])
        subnet_bit = ip_bit & net_bit
        if subnet.count(".") == 3:
            subnet += str(subnet_bit)
        else:
            subnet += str(subnet_bit) + "."
    return subnet
