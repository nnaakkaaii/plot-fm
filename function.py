from pkg import pl


def lambda_handler(event, context):
    """
    >>> lambda_handler({"company_id": "0", "company_name": ""}, {})
    {}
    """
    company_id = event['company_id']
    company_name = event['company_name']

    res = pl.list(company_id, company_name)

    if res is None:
        return {}
    else:
        return res.as_dict()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
