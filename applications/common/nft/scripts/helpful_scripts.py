import web3
from web3 import Web3
import json
url = "https://rinkeby.infura.io/v3/aa33ee17500941999256cec7124c5bf4"
trade_hx = "0xd007326cfbd0698b462bb18d3f899ee41d785f7c20f5e480163bbd7a33af89a4"
w3 = Web3(Web3.HTTPProvider(url))
chain_id = 4


tx0 = w3.eth.getTransactionReceipt(trade_hx)
tx = w3.eth.getTransaction(trade_hx)
our_address = tx0["to"]
trade_address = tx0["from"]
trade_number = tx["value"] / 1000000000000000000


{'blockHash': HexBytes('0xdd9e4327b8acc417332251f0314c2b120012bfbb2437811dac7991db01b1bb0e'),
'blockNumber': 9526341,
'contractAddress': None,
'cumulativeGasUsed': 28862972,
'effectiveGasPrice': 1000414655,
'from': '0x533e4bA458292b82EE3B85d313390C6571401774',
'gasUsed': 94581,
'logs': [AttributeDict({'address': '0x04C21F8aED84D5C359d447C5f500E41f0Eb3D042',
                        'blockHash': HexBytes('0xdd9e4327b8acc417332251f0314c2b120012bfbb2437811dac7991db01b1bb0e'),
                        'blockNumber': 9526341,
                        'data': '0x',
                        'logIndex': 147,
                        'removed': False,
                        'topics': [HexBytes('0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'),
                                   HexBytes('0x000000000000000000000000533e4ba458292b82ee3b85d313390c6571401774'),
                                   HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'),
                                   HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000')],
'transactionHash': HexBytes('0xf242677a93b605d7a9a57468a3b77f2a9795d06354950c064d44c4c556beacd9'), 'transactionIndex': 32}),
         AttributeDict({'address': '0x04C21F8aED84D5C359d447C5f500E41f0Eb3D042',
                        'blockHash': HexBytes('0xdd9e4327b8acc417332251f0314c2b120012bfbb2437811dac7991db01b1bb0e'),
                        'blockNumber': 9526341,
                        'data': '0x',
                        'logIndex': 148,
                        'removed': False,
                        'topics': [HexBytes('0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'),
                                   HexBytes('0x000000000000000000000000533e4ba458292b82ee3b85d313390c6571401774'),
                                   HexBytes('0x00000000000000000000000050c26b597b6b1fd4844c1083234f5f70ca6136ff'),
                                   HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000')],
                        'transactionHash': HexBytes('0xf242677a93b605d7a9a57468a3b77f2a9795d06354950c064d44c4c556beacd9'),
                        'transactionIndex': 32})],
 'logsBloom': HexBytes('0x00000400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200010000000000000000000000008000000000000000000000000000000000000000000000000020802000000002000000800000000000000000000000010002000000000000001000000000000000000000000000000000000000200000000000000020000000000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000001020000010000000000000000000000000000000000000000000000000000000000000'),
 'status': 1,
 'to': '0x04C21F8aED84D5C359d447C5f500E41f0Eb3D042',
 'transactionHash': HexBytes('0xf242677a93b605d7a9a57468a3b77f2a9795d06354950c064d44c4c556beacd9'),
 'transactionIndex': 32,
 'type': '0x0'}






