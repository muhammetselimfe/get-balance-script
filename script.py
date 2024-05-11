import requests

infura_mainnet = "https://mainnet.infura.io/v3/00ad0af36ebd412a8de46130ccdabc7a"
infura_holesky = "https://holesky.infura.io/v3/00ad0af36ebd412a8de46130ccdabc7a"
infura_sepolia = "https://sepolia.infura.io/v3/00ad0af36ebd412a8de46130ccdabc7a"

ADDRESS = "0xB07626Bc2fF18d680ec886c3109e9BF6ee05E6b7"

# get balance 
def get_balance(url, address):
    data = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }
    response = requests.post(url, json=data)
    balance_hex = response.json().get("result")
    if balance_hex is not None:
        balance_dec = int(balance_hex, 16) / 10**18  # Convert from wei to Ether
        return balance_dec
    else:
        return None

# get the latest block
def get_latest_block_number(url):
    data = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "eth_blockNumber"
    }
    response = requests.post(url, json=data)
    result = response.json().get("result")
    if result is not None:
        block_number_hex = result
        block_number_dec = int(block_number_hex, 16)
        return block_number_dec
    return None

def check_balance(network, infura_url):
    print("Network:", network)
    balance_dec = get_balance(infura_url, ADDRESS)
    latest_block_number = get_latest_block_number(infura_url)
    if balance_dec is not None:
        print("ETH balance at latest block on", network + ":", balance_dec, "ETH")
        print("Latest block number:", latest_block_number)
    else:
        print("Failed to retrieve balance on", network)

# Check account balance for each network
check_balance("Mainnet", infura_mainnet )
check_balance("Holesky", infura_holesky) 
check_balance("Sepolia", infura_sepolia)
