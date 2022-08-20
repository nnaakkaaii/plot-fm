from typing import Dict

from pkg.pl import PL, PLAttr


SELL_ADMIN_EXPENSE_CUT_RATE = 0.15


def simulate(p: PL):
    fys = sorted(list(set([x.fy for x in p.data])))
    header = ['DX前純利益', 'DX後純利益', 'DX前販管費', 'DX後販管費', '販管費削減率']

    pl_dic: Dict[(int, PLAttr), float] = {}
    for row in p.data:
        pl_dic[(row.fy, row.attr)] = row.price

    data = []
    for fy in fys:
        before_dx_net_income = pl_dic.get((fy, PLAttr.NetIncome))
        if before_dx_net_income is None:
            continue
        gross_profit = pl_dic.get((fy, PLAttr.GrossProfit))
        if gross_profit is None:
            continue
        operating_income = pl_dic.get((fy, PLAttr.OperatingIncome))
        if operating_income is None:
            continue
        sell_admin_expense = gross_profit - operating_income
        sell_admin_expense_cut = SELL_ADMIN_EXPENSE_CUT_RATE * sell_admin_expense
        after_dx_net_income = before_dx_net_income + sell_admin_expense_cut
        data.append([before_dx_net_income,
                     after_dx_net_income,
                     sell_admin_expense,
                     sell_admin_expense - sell_admin_expense_cut,
                     SELL_ADMIN_EXPENSE_CUT_RATE])
    return {
        'data': data,
        'header': header,
        'index': fys,
    }
