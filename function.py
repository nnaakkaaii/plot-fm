from pkg import company, pl, response


def lambda_handler(event, context):
    """
    >>> lambda_handler({"queryStringParameters": {"name": "ベイカレント"}}, {})
    {}
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
    else:
        return response.serialize({
            'id': p.company_id,
            'name': p.company_name,
            'data': [
                {
                    'fy': r.fy,
                    'attr': r.attr.value,
                    'price': r.price,
                }
                for r in p.data
            ]
        })


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
