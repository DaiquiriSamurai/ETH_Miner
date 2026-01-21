# eth-miner

Experimental Ethereum mining software (WIP)

⚠️ **This project is a prototype and is NOT production ready**  
⚠️ **Use at your own risk**

---

## Overview

`eth-miner` is an experimental Ethereum mining project written in Python.  
The goal of this repository is to explore how mining pools work and how block
hashing behaves under different difficulty constraints.

This project is still in early development and many features are incomplete
or missing.

---

## Features (planned)

- Connection to Ethereum mining pools
- Block header generation
- Hash computation and share submission
- Configurable difficulty
- Lightweight and portable (Python-based)
- Cross-platform (Linux / Windows)

---

## Current status

🚧 **Work in progress**

At the moment, the miner:
- Pool connection
- Generates block headers
- Performs basic hash computations
- Detects potential valid shares (experimental)

Performance optimizations and real network support are planned for later stages.

---

## Configuration

Edit the following variables in `eth_miner.py`:

```python
WALLET_ADDRESS = ""
MINING_POOL = "eth.pool.example:4444"
