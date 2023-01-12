import csv

def accessOrders(path_to_file):
    if path_to_file.endswith(".csv"):
        try:
            with open(path_to_file, newline="") as filePath:
                odersColumns = ['client', 'requests', 'day']
                return list(csv.DictReader(filePath, fieldnames=odersColumns))
        except:
            raise FileNotFoundError(f"Arquivo inexistente:  '{path_to_file}'")
    raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

def mostRequestedByMaria(resultOrders, nameClient):
    resMaria = [eachLine['requests'] for eachLine in resultOrders if eachLine['client'] == nameClient]

    mostRequested = {}
    for element in resMaria:
        if element not in mostRequested:
            mostRequested[element] = 1
        mostRequested[element] += 1

    checkLargerOrder = max(mostRequested, key=mostRequested.get)
    return checkLargerOrder
            
def amountOfHamburgerByArnaldo(resultOrders, nameClient, nameRequest):
    amountOfHamburger = []
    for each_line in resultOrders:
        if each_line['client'] == nameClient and each_line['requests'] == nameRequest:
            amountOfHamburger.append(each_line)
            # print('', len(amountOfHamburger))
    return len(amountOfHamburger)   

def orderNotPlaced(resultOrders, keyOfOrders, nameClient):
    clientOfOrdersComplete = set([line[keyOfOrders] for line in resultOrders ])
    clientOfOrders = set([line[keyOfOrders] for line in resultOrders if line['client'] == nameClient])

    return clientOfOrdersComplete - clientOfOrders


def analyze_log(path_to_file):
    resultOrders = accessOrders(path_to_file)
    #Qual o prato mais pedido por 'maria'?
    resultOrderMaria = mostRequestedByMaria(resultOrders, "maria")
    #Quantas vezes 'arnaldo' pediu 'hamburguer'?
    resultAmountArnaldo = amountOfHamburgerByArnaldo(resultOrders, 'arnaldo', 'hamburguer')
    #Quais pratos 'joao' nunca pediu?
    resultRequestsOrderNotPlaced = orderNotPlaced(resultOrders, 'requests', 'joao')
    #Quais dias 'joao' nunca foi à lanchonete?
    resultDayOrderNotPlaced = orderNotPlaced(resultOrders, 'day', 'joao')

    with open("data/mkt_campaign.txt", "w") as file:
                    file.write(
                        f"{resultOrderMaria}\n"
                        f"{resultAmountArnaldo}\n"
                        f"{resultRequestsOrderNotPlaced}\n"
                        f"{resultDayOrderNotPlaced}\n"
                        )

if __name__ == "__main__":
    analyze_log("data/orders_1.csv")