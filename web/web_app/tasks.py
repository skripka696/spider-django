def save_item_to_db(items):
    #TODO: here we save items to DB, using django get_or_create
    for item in items:
        pass


def choice_spider(spider, items=None):
    spider_action = {
        'new_york': save_item_to_db,
    }
    return spider_action[spider](items)
