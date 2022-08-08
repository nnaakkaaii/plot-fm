def lambda_handler(event, context):
    """
    >>> lambda_handler({}, {})
    '{}'
    """
    return {}


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
