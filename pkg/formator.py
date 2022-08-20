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
    PLAttr.GrossProfit: 1,
    PLAttr.OperatingIncome: 2,
    PLAttr.IncomeBeforeTax: 3,
    PLAttr.NetIncome: 4,
}


def pl(p: PL):
    fys = sorted(list(set([x.fy for x in p.data])))
    attrs = sorted(list(set([x.attr for x in p.data if x.attr in PL_ROW_ORDER])),
                   key=lambda x: PL_ROW_ORDER[x])

    pl_dic = {}
    for row in p.data:
        pl_dic[(row.fy, row.attr)] = row.price

    # 差分表示する
    data = []
    header = []
    for fy in fys:
        header = []
        last_attr = ''
        last_price = 0
        record = []
        for attr in attrs:
            if last_price == 0 and last_attr == '':
                last_attr = attr.value
                last_price = pl_dic.get((fy, attr))
                continue
            price = pl_dic.get((fy, attr))
            header.append(f'{last_attr} - {attr.value}')
            record.append(last_price - price)
            last_attr = attr.value
            last_price = price
        header.append(last_attr)
        record.append(last_price)
        data.append(record[::-1])

    return {
        'data': data,
        'header': header[::-1],
        'index': fys,
    }
