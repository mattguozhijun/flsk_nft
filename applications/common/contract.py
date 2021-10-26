# -*- coding: utf-8 -*-
# @Time : 2021/10/21 4:34 下午
# @Author : HL
# @Email : 1277078753@qq.com
# @Describe :
from applications.extensions import db
from applications.models import Trade
from web3 import Web3
from applications.common.nft.scripts.jy import nft_trade


def validate_trade(trade_address, item):
    if item == 'nft':
      return validate_trade_nft(trade_address, item)
    else:
        return False


def validate_trade_nft(trade_hx, item):
    # tudo 没写合约判断
    url = "https://rinkeby.infura.io/v3/aa33ee17500941999256cec7124c5bf4"
    w3 = Web3(Web3.HTTPProvider(url))
    tx0 = w3.eth.getTransactionReceipt(trade_hx)
    tx = w3.eth.getTransaction(trade_hx)
    our_address = tx0["to"]
    succ = tx0["status"]
    trade_address = tx0["from"]
    trade_number = tx["value"]/1000000000000000000
    if our_address=="我们地址" and trade_number == "数量" and succ == 1:
        hx = nft_trade(trade_address)
        if hx == 0:
            return "合约地址为空值,NFT铸造或交易失败！"
        else:
            trade = Trade(
                trade_address=trade_address,
                item=item
            )
            r = db.session.add(trade)
            db.session.commit()
            return hx


def toChecksumAddress(s: str):
    try:
        return Web3.toChecksumAddress(s)
    except:
        return None
