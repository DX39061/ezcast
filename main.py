#!/usr/bin/env python3

import os
from config import Config

def get_call_cmd(params, TRACE = True):
    cmd = f'cast call {params.TARGET} {params.CALLDATA}'
    cmd += f' --rpc-url {params.RPC_URL}'
    if params.CALLVALUE != None:
        cmd += f' --value {params.CALLVALUE}'
    if params.PRIVATE_KEY != None:
        cmd += f' --private-key {params.PRIVATE_KEY}'
    if TRACE:
        cmd += ' --trace'
    print("\033[92m" + cmd + "\033[0m")
    return cmd
    
def get_send_cmd(params):
    cmd = f'cast send {params.TARGET} {params.CALLDATA}'
    cmd += f' --rpc-url {params.RPC_URL}'
    if params.CALLVALUE != None:
        cmd += f' --value {params.CALLVALUE}'
    if params.GAS_PRICE != None:
        cmd += f' --gas-price {params.GAS_PRICE}'
    if params.PRIORITY_GAS_PRICE != None:
        cmd += f' --priority-gas-price {params.PRIORITY_GAS_PRICE}'
    if params.PRIVATE_KEY != None:
        cmd += f' --private-key {params.PRIVATE_KEY}'
    print("\033[92m" + cmd + "\033[0m")
    return cmd

def print_error(msg):
    # print with red color
    print("\033[91m")
    print(msg)
    print("\033[0m")

def print_help():
    # print with green color
    print("\033[92m")
    print("rpc <url> - set RPC URL")
    print("priv <key> - set private key")
    print("gas-price <price> - set gas price")
    print("priority-gas-price <price> - set priority gas price")
    print("target <address> - set target address")
    print("calldata <data> - set calldata")
    print("callvalue <value> - set call value") 
    print("show - show current config")
    print("call - make a call transaction")
    print("send - make a send transaction")
    print("help - show this help")
    print("\033[0m")

def print_params(params):
    # print with yellow color
    print("\033[93m")
    print("RPC URL:", params.RPC_URL)
    print("Private key:", params.PRIVATE_KEY)
    print("Target address:", params.TARGET)
    print("Calldata:", params.CALLDATA)
    print("Callvalue:", params.CALLVALUE)
    if params.GAS_PRICE == None:
        print("Gas price:", params.GAS_PRICE)
    if params.PRIORITY_GAS_PRICE == None:
        print("Priority gas price:", params.PRIORITY_GAS_PRICE)
    print("\033[0m")

def main(params):
    while True:
        cmd = input("> ").split(" ")
        try:
            if cmd[0] == "rpc":
                params.RPC_URL = cmd[1]
            elif cmd[0] == "priv":
                params.PRIVATE_KEY = cmd[1]
            elif cmd[0] == "gas-price":
                params.GAS_PRICE = eval(cmd[1])
            elif cmd[0] == "priority-gas-price":
                params.PRIORITY_GAS_PRICE = eval(cmd[1])
            elif cmd[0] == "target":
                params.TARGET = cmd[1]
            elif cmd[0] == "calldata":
                params.CALLDATA = " ".join(cmd[i] for i in range(1, len(cmd)))
            elif cmd[0] == "callvalue":
                params.CALLVALUE = int(cmd[1])
            elif cmd[0] == "show":
                print_params(params)
            elif cmd[0] == "call":
                if params.TARGET == None:
                    print_error("Target address not set")
                    continue
                if params.CALLDATA == None:
                    print_error("Calldata not set")
                    continue
                call_cmd = get_call_cmd(params)
                os.system(call_cmd)
            elif cmd[0] == "send":
                if params.TARGET == None:
                    print_error("Target address not set")
                    continue
                if params.CALLDATA == None:
                    print_error("Calldata not set")
                    continue
                if params.PRIVATE_KEY == None:
                    print_error("Account private key not set")
                    continue
                send_cmd = get_send_cmd(params)
                print(send_cmd)
                os.system(send_cmd)
            elif cmd[0] == "help":
                print_help()
            else:
                print_error("nop")
                continue
        except IndexError:
            print_error("Invalid command")
            continue

if __name__ == '__main__':
    try:
        params = Config()
        params.load()
        main(params)
    except KeyboardInterrupt:
        params.save()
        print("\nBye")
        exit()
