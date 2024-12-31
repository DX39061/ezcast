#!/usr/bin/env python3

import os
class Config:
    def __init__(self):
        self.RPC_URL = None
        self.PRIVATE_KEY = None
        self.GAS_PRICE = None
        self.PRIORITY_GAS_PRICE = None
        self.TARGET = None
        self.CALLDATA = None
        self.CALLVALUE = None

    def save(self):
        path = __file__.replace("config.py", "ezcast.txt")
        with open(path, "w") as f:
            f.write(f"rpc {self.RPC_URL}\n")
            f.write(f"private-key {self.PRIVATE_KEY}\n")
            f.write(f"gas-price {self.GAS_PRICE}\n")
            f.write(f"priority-gas-price {self.PRIORITY_GAS_PRICE}\n")
            f.write(f"target {self.TARGET}\n")
            f.write(f"calldata {self.CALLDATA}\n")
            f.write(f"callvalue {self.CALLVALUE}\n")
    
    def load(self):
        try:
            path = __file__.replace("config.py", "ezcast.txt")
            with open(path, "r") as f:
                lines = f.readlines()
                for line in lines:
                    cmd = line.split(" ")
                    if len(cmd) < 2 or cmd[1] == "None":
                        continue
                    else:
                        cmd[-1] = cmd[-1].replace("\n", "")
                    if cmd[0] == "rpc":
                        self.RPC_URL = cmd[1]
                    elif cmd[0] == "private-key":
                        self.PRIVATE_KEY = cmd[1]
                    elif cmd[0] == "gas-price":
                        self.GAS_PRICE = eval(cmd[1])
                    elif cmd[0] == "priority-gas-price":
                        self.PRIORITY_GAS_PRICE = eval(cmd[1])
                    elif cmd[0] == "target":
                        self.TARGET = cmd[1]
                    elif cmd[0] == "calldata":
                        self.CALLDATA = " ".join(cmd[i] for i in range(1, len(cmd)))
                    elif cmd[0] == "callvalue":
                        self.CALLVALUE = eval(cmd[1])
        except FileNotFoundError:
            pass
