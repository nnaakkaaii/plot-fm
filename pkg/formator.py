from pkg.company import Company
from pkg.pl import PL, PLAttr


def company(c: Company):
    return {
        'data': [
            [
                c.id,
            ],
            [
                c.name,
            ],
        ],
        'index': [
            '企業ID',
            '企業名',
        ],
    }


PL_ROW_ORDER = {
    PLAttr.TotalRevenue: 0,
    PLAttr.CostOfRevenue: 1,
    PLAttr.GrossProfit: 2,
    PLAttr.OperatingIncome: 3,
    PLAttr.IncomeBeforeTax: 4,
    PLAttr.NetIncome: 5,
}


def pl(p: PL):
    fys = sorted(list(set([x.fy for x in p.data])))
    attrs = sorted(list(set([x.attr for x in p.data])),
                   key=lambda x: PL_ROW_ORDER[x])

    pl_dic = {}
    for row in p.data:
        pl_dic[(row.fy, row.attr)] = row.price

    return {
        'data': [
            [
                pl_dic.get((fy, attr)) for fy in fys
            ]
            for attr in attrs
        ],
        'header': fys,
        'index': [
            attr.value
            for attr in attrs
        ],
    }
