import subprocess
import argparse

def add_loss(interface, percentage):
    subprocess.run(["tc", "qdisc", "add", "dev", interface, "root", "netem", "loss", str(percentage) + "%"])

def add_delay(interface, delay_time):
    subprocess.run(["tc", "qdisc", "add", "dev", interface, "root", "netem", "delay", str(delay_time) + "ms"])


###
# python simulation.py -i eth0 -m loss -v 30
##
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simulate network conditions using tc')
    parser.add_argument('-i', '--interface', required=True, help='Network interface')
    parser.add_argument('-m', '--mode', required=True, choices=['loss', 'delay'], help='Simulation mode')
    parser.add_argument('-v', '--value', required=True, help='Value for the simulation')
    args = parser.parse_args()

    if args.mode == 'loss':
        add_loss(args.interface, args.value)
    elif args.mode == 'delay':
        add_delay(args.interface, args.value)

