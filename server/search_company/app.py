from pkg import company


def lambda_handler(event, context):
    """
    >>> lambda_handler({"company_name": "ベイカレント"}, {})
    {'id': '6532', 'name': 'ベイカレント・コンサルティング'}
    """
    company_name = event['company_name']

    res = company.search(company_name)

    if res is None:
        return {}
    else:
        return res.as_dict()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
