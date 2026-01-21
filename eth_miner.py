import time
import random
import hashlib

WALLET_ADDRESS = "0xF7cd6FbD50CfFDA17409cabfd607133f3A2558ee"
MINING_POOL = "eth.pool.example:4444"

HASHRATE_TARGET = 120_000
DIFFICULTY = 5_000_000


class EthereumMiner:
    def __init__(self, wallet_address: str):
        if not wallet_address:
            exit(1)

        self.wallet_address = wallet_address
        self.running = False
        self.hashes_computed = 0

    def connect_to_pool(self):
        print(f"[*] Connecting to mining pool {MINING_POOL}...")
        time.sleep(1)
        print("[+] Connected")

    def generate_block_header(self) -> bytes:
        seed = str(random.random()).encode()
        return hashlib.sha256(seed).digest()

    def hash(self, data: bytes) -> str:
        self.hashes_computed += 1
        return hashlib.sha256(data).hexdigest()

    def start_mining(self):
        self.running = True
        self.connect_to_pool()

        print("[*] Mining started...")
        while self.running:
            header = self.generate_block_header()
            result = self.hash(header)

            if result.startswith("0000"):
                print("[+] Share accepted by pool")

            time.sleep(0.05)

    def stop(self):
        self.running = False
        print("[*] Mining stopped")


if __name__ == "__main__":
    miner = EthereumMiner(WALLET_ADDRESS)

    try:
        miner.start_mining()
    except KeyboardInterrupt:
        miner.stop()
