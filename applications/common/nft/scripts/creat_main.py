import os
import re


def subString(template):
    rule = r'SimpleCollectibledeployedat:(.*?)Transactionsent:' # 正则规则
    print(template.replace(" ","").replace("\n",""))
    slotList = re.findall(rule, template.replace(" ","").replace("\n",""))
    if slotList == []:
        return []
    else:
        return slotList[0]

a = os.popen("brownie run scripts/creat.py --network rinkeby")



contract_address =subString(a.read())
print(contract_address)
