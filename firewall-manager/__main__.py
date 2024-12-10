import subprocess

IPTABLES = 'iptables'


def _run_ip_tables(rule: str):
    subprocess.run(IPTABLES + ' ' + rule, shell=True)


def _rule_exists(iptables_rule: str) -> bool:
    command = 'iptables -S'
    rules = subprocess.check_output(command, shell=True, text=True)
    return iptables_rule in rules


def block_address(addr: str):
    """
    Add iptables rule, which drops all requests from given address.
    addr: str - valid ipv4 address (eg. 192.168.1.10)
    """
    rule = f'-A INPUT -s {addr}/32 -j DROP'

    if _rule_exists(rule):
        return

    _run_ip_tables(rule)


def unblock_address(addr: str):
    """
    Remove iptables rule, which drops all requests from given address.
    addr: str - valid ipv4 address (eg. 192.168.1.10)
    """
    rule = f'-D INPUT -s {addr}/32 -j DROP'

    if _rule_exists(rule):
        _run_ip_tables(rule)
