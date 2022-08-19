from pkg import company, pl


def lambda_handler(event, context):
    """
    >>> lambda_handler({"queryStringParameters": {"name": "ベイカレント"}}, {})
    {}
    """
    name = event["queryStringParameters"]['name']

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
                    'attr': r.attr,
                    'price': r.price,
                }
                for r in p.data
            ]
        }


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
