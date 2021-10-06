import math


# Нахождение факториала
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


# Случай M/M/n/0
def mmn0(**kargs):
    print("\tНахождение вероятности того, что в системе не находится заявка...")
    p0 = (1 + sum([(kargs["alph"] ** k) / fac(k) for k in range(1, kargs["n"] + 1)])) ** (-1)
    print(f"\tВероятность того, что в системе находится заявка: {p0}")
    pk = [((kargs["alph"] ** k) / fac(k)) * p0 for k in range(1, kargs["n"] + 1)]
    print(f"\tВероятности того, что в системе находится k заявок: {pk}")

    print("\tПроверка суммы вероятностей... ")
    print(f"\tСумма вероятностей равна: {sum(pk) + p0}")
    p_otkl = pk[-1]
    print(f"\tВероятность отказа в обслуживании: {p_otkl}")
    q = kargs["lb"] * (1 - p_otkl)
    print(f"\tПропускная способность: {q}")
    n_ = kargs["alph"] * (1 - p_otkl)
    print(f"\tСреднее число занятых приборов: {n_}")
    t_c = n_ / kargs["lb"]
    print(f"\tСреднее время нахождения заявки в системе: {t_c}")
    k_n = (n_ / n) * 100
    print(f"\tПроцент занятости приборов: {k_n}")
    print("\tРасчёт окончен!\n")

    return ["M/M/n/0", 0, p_otkl, q, n_, k_n, t_c]


# Случай M/M/n/inf
def mmninf(**kargs):
    print("\tНахождение вероятности того, что в системе не находится заявка...")
    p0 = (1 + \
          sum([(kargs["alph"] ** k) / fac(k) for k in range(1, kargs["n"] + 1)]) + \
          (kargs["alph"] ** (kargs["n"] + 1)) / (fac(kargs["n"]) * (kargs["n"] - kargs["alph"]))
          ) ** (-1)
    print(f"\tВероятность того, что в системе находится заявка: {p0}")
    pk = [((kargs["alph"] ** k) / fac(k)) * p0 for k in range(1, kargs["n"] + 1)]
    print(f"\tВероятности того, что в системе находится k заявок: {pk}")
    print("\tПроверка суммы вероятностей... ")
    print(f"\tСумма вероятностей равна: {sum(pk) + p0}")
    q = kargs["lb"]
    print(f"\tПропускная способность: {q}")
    n_ = kargs["alph"]
    print(f"\tСреднее число занятых приборов: {n_}")
    p_och = 1 - sum([pk[k] for k in range(0, kargs["n"] - 1)])
    print(f"\tВероятность отказа в обслуживании: {p_och}")
    m_ = (kargs["alph"] * p_och) / (kargs["n"] - kargs["alph"])
    print(f"\tСреднее число заявок в очереди: {m_}")
    N_ = n_ + m_
    print(f"\tСреднее число заявок в системе: {N_}")
    t_c = N_ / kargs["lb"]
    print(f"\tСреднее время нахождения заявки в системе: {t_c}")
    k_n = (n_ / n) * 100
    print(f"\tПроцент занятости приборов: {k_n}")
    t_och = m_ / kargs["lb"]
    print(f"\tСреднее время нахождения заявки в очереди: {t_och}")
    print("\tРасчёт окончен!\n")

    return ["M/M/n/inf", "inf", 0, q, n_, k_n, t_c]


def p_n_plus_s(p0, alph, n, s):
    pns = ((alph ** n) / fac(n)) * ((alph / n) ** s) * p0
    return pns


# Случай M/M/n/m
def mmnm(**kargs):
    print("\tНахождение вероятности того, что в системе не находится заявка...")
    p0 = (1 + \
          sum([(kargs["alph"] ** k) / fac(k) for k in range(1, kargs["n"] + 1)]) + \
          ((kargs["alph"] ** kargs["n"]) / fac(kargs["n"])) * sum(
                [(kargs["alph"] / kargs["n"]) ** s for s in range(1, kargs["m"] + 1)])
          ) ** (-1)
    print(f"\tВероятность того, что в системе находится заявка: {p0}")
    pk = [((kargs["alph"] ** k) / fac(k)) * p0 for k in range(1, kargs["n"] + 1)]
    print(f"\tВероятности того, что в системе находится k заявок: {pk}")
    p_n_plus_s_ = [p_n_plus_s(p0, kargs["alph"], kargs["n"], s) for s in range(1, kargs["m"] + 1)]
    print(f"\tВероятности того, что в системе находится n+s заявок: {p_n_plus_s_}")
    print("\tПроверка суммы вероятностей... ")
    print(f"\tСумма вероятностей равна: {sum(pk) + p0 + sum(p_n_plus_s_)}")

    p_otkl = p_n_plus_s(p0, kargs["alph"], kargs["n"], kargs["m"])
    print(f"\tВероятность отказа в обслуживании: {p_otkl}")
    n_ = kargs["alph"] * (1 - p_otkl)
    print(f"\tСреднее число занятых приборов: {n_}")
    q = kargs["mu"] * n_
    print(f"\tПропускная способность: {q}")
    m_ = sum([s * p_n_plus_s(p0, kargs["alph"], kargs["n"], s) for s in range(1, kargs["m"] + 1)])
    print(f"\tСреднее число заявок в очереди: {m_}")
    N_ = n_ + m_
    print(f"\tСреднее число заявок в системе: {N_}")
    t_och = m_ / kargs["lb"]
    print(f"\tСреднее время нахождения заявки в очереди: {t_och}")
    t_c = N_ / kargs["lb"]
    print(f"\tСреднее время нахождения заявки в системе: {t_c}")
    k_n = (n_ / n) * 100
    print(f"\tПроцент занятости приборов: {k_n}")
    print("\tРасчёт окончен!\n")

    return ["M/M/n/m", kargs["m"], p_otkl, q, n_, k_n, t_c]


def print_table(lst_data):
    cols = {"1": 14,
            "2": 7,
            "3": 14,
            "4": 14,
            "5": 14,
            "6": 14,
            "7": 14}
    head = ["Случай", "m", "Pотк", "Q", "n_", "kn", "t_c"]

    print(f"+", "-" * cols["1"], "+", "-" * cols["2"], "+", "-" * cols["3"], "+", "-" * cols["4"], "+", "-" * cols["5"],
          "+", "-" * cols["6"], "+", "-" * cols["7"], "+", sep="")

    row = ""
    for i, col_name in enumerate(head):
        start = math.floor((cols[str(i + 1)] - len(col_name)) / 2)
        end = math.ceil((cols[str(i + 1)] - len(col_name)) / 2)
        row += "|" + f" " * start + f"{col_name}" + f" " * end
    row += "|"
    print(row)

    print(f"+", "-" * cols["1"], "+", "-" * cols["2"], "+", "-" * cols["3"], "+", "-" * cols["4"], "+", "-" * cols["5"],
          "+", "-" * cols["6"], "+", "-" * cols["7"], "+", sep="")

    for data in lst_data:
        row = ""
        for i, elem in enumerate(data):
            if len(str(elem)) >= cols[str(i + 1)]:
                elem = "%.6f" % elem
                start = math.floor((cols[str(i + 1)] - len(str(elem))) / 2)
                end = math.ceil((cols[str(i + 1)] - len(str(elem))) / 2)
                row += "|" + f" " * start + f"{elem}" + f" " * end
            else:
                start = math.floor((cols[str(i + 1)] - len(str(elem))) / 2)
                end = math.ceil((cols[str(i + 1)] - len(str(elem))) / 2)
                row += "|" + f" " * start + f"{elem}" + f" " * end
        row += "|"
        print(row)
        print(f"+", "-" * cols["1"], "+", "-" * cols["2"], "+", "-" * cols["3"], "+", "-" * cols["4"], "+",
              "-" * cols["5"], "+", "-" * cols["6"], "+", "-" * cols["7"], "+", sep="")


if __name__ == "__main__":
    lb = 2.1
    mu = 1
    n = 3
    m = 2
    alph = lb / mu

    data = []
    # Расчитываем случай M/M/n/0
    print("\nРассчитываем случай M/M/n/0: ")
    res_mmn0 = mmn0(lb=lb, mu=mu, n=n, alph=alph)
    data.append(res_mmn0)

    # Расчитываем случай M/M/n/inf
    print("Рассчитываем случай M/M/n/inf: ")
    res_mmninf = mmninf(lb=lb, mu=mu, n=n, alph=alph)
    data.append(res_mmninf)

    # Расчитываем случай M/M/n/m
    print("Рассчитываем случай M/M/n/m: ")
    res_mmnm = mmnm(lb=lb, mu=mu, n=n, m=m, alph=alph)
    data.append(res_mmnm)

    print("Вывод сводной таблицы: ")
    print_table(data)
