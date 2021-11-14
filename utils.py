from datetime import datetime, timezone


def get_user_age_seconds(user_create_date):
    """
    This functions gets the user date creation (user['CreateDate'])
    and returns the total seconds the user is living
    :param user_create_date:
    :return:
    """
    return (datetime.now(timezone.utc) - user_create_date).total_seconds()


def compress(my_str):
    """
    Compress a string in the following way:
    gggttthhjyyy  ->  g3t3h2jy3
    abcdddddukkk  ->  abcd5uk3

    :param my_str: string a-z only
    :return: compressed string - sequences of the form XX...XXX transformed to XN
             where N in the length of the sequence
    """


def decompress(my_str):
    """
    Decompress a string:
    sdfg4jfg3   ->  sdfggggjfggg
    l5a2    ->  lllllaa

    :param my_str:
    :return:
    """
