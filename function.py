from pkg import company, dx, formator, pl, response, sheet


def lambda_handler(event, context):
    """
    >>> lambda_handler({"queryStringParameters": {"name": "あ"}}, {})
    '{"message": "企業が一意に特定されません"}'
    """
    if 'queryStringParameters' not in event:
        return response.serialize({'message': 'パラメータ`name`を指定してください'})

    param = event["queryStringParameters"]

    if 'name' not in param:
        return response.serialize({'message': 'パラメータ`name`を指定してください'})

    name = param['name']

    c = company.search(name)
    if c is None:
        return response.serialize({'message': '企業が一意に特定されません'})

    p = pl.list(c.id, c.name)

    if p is None:
        return response.serialize({'message': '企業は見つかりましたが財務情報が見つかりません'})

    wb = sheet.create()
    ws1 = wb.create_sheet('このシートについて')
    ws1.write(**formator.company(c))

    ws2 = wb.create_sheet('財務諸表(PL)')
    ws2.write(**formator.pl(p))
    ws2.set_col_width()
    ws2.cumulative_bar_chart(title='PLの経年推移')

    ws3 = wb.create_sheet('DX純利益シミュレータ')
    ws3.write(**dx.simulate_profit(p))
    ws3.set_col_width(width=13)
    ws3.line_chart(title='DXの有無による純利益の比較結果', max_cols=2)

    ws4 = wb.create_sheet('DX累積効果シミュレータ')
    ws4.write(**dx.simulate_cost_cut(p))
    ws4.set_col_width(width=13)
    ws4.bar_chart(title='DXの有無による累積コストカットの比較結果', max_cols=1)

    wb.save(c.name)

    if wb.path is None:
        return response.serialize({'message': '不明なエラーによりExcelファイルを作成できません'})

    return response.encode(open(wb.path, 'rb').read(), c.id, content_type=response.ContentType.xlsx)


if __name__ == '__main__':
    import base64
    res = lambda_handler({'queryStringParameters': {'name': 'ベイカレント'}}, {})
    with open('tmp/test.xlsx', 'wb') as f:
        f.write(base64.b64decode(res['body']))
