from pkg import company, pl


def lambda_handler(event, context):
    """
    >>> lambda_handler({"queryStringParameters": {"name": "ベイカレント"}}, {})
    {}
    """
    param = event["queryStringParameters"]

    if 'name' not in param:
        return {'message': 'パラメータ`name`を指定してください'}

    name = param['name']

    c = company.search(name)
    if c is None:
        return {}

    p = pl.list(c.id, c.name)

    if p is None:
        return {}
    else:
        return {
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
        }


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
