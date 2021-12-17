from datetime import datetime, timezone


def get_user_age_seconds(user_create_date):
    """
    This functions gets the user date creation (user['CreateDate'])
    and returns the total seconds the user is living
    :param user_create_date:
    :return:
    """
    return (datetime.now(timezone.utc) - user_create_date).total_seconds()


def most_frequent_char(my_str):
    """
    returns the most frequent character in a string. If there are more than 1 frequent chars, return one of them
    'abcdddddukkk'  ->  'd' repeats 5 times
    'One day you said to me'  ->  ' ' repeats 5 times
    'aabb' -> 'a' or 'b' are both valid returned values
    """
    for i in range(100):
        print(i)

