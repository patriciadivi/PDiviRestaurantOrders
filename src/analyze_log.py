import csv


def accessOrders(path_to_file):
    if path_to_file.endswith(".csv"):
        try:
            with open(path_to_file, newline="") as filePath:
                odersColumns = ['client', 'requests', 'day']
                return list(csv.DictReader(filePath, fieldnames=odersColumns))
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente:  '{path_to_file}'")
    raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")


def mostRequestedByMaria(orders, client):
    orders = [line['requests'] for line in orders if line['client'] == client]

    mostRequested = {}
    for element in orders:
        if element not in mostRequested:
            mostRequested[element] = 1
        mostRequested[element] += 1

    checkLargerOrder = max(mostRequested, key=mostRequested.get)
    return checkLargerOrder


def amountOfHamburger(resultOrders, nameClient, nameRequest):
    amountOfHamburger = []
    for line in resultOrders:
        if line['client'] == nameClient and line['requests'] == nameRequest:
            amountOfHamburger.append(line)
            # print('', len(amountOfHamburger))
    return len(amountOfHamburger)


def orderNotPlaced(orders, key, nameCli):
    cliOrdersComplete = set([line[key] for line in orders])
    ordersC = set([line[key] for line in orders if line['client'] == nameCli])

    return cliOrdersComplete - ordersC


def analyze_log(path_to_file):
    resultOrders = accessOrders(path_to_file)
    resultOrderMaria = mostRequestedByMaria(resultOrders, "maria")
    resultAmount = amountOfHamburger(resultOrders, 'arnaldo', 'hamburguer')
    resultRequests = orderNotPlaced(resultOrders, 'requests', 'joao')
    resultDay = orderNotPlaced(resultOrders, 'day', 'joao')

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
                    f"{resultOrderMaria}\n"
                    f"{resultAmount}\n"
                    f"{resultRequests}\n"
                    f"{resultDay}\n"
                    )


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
