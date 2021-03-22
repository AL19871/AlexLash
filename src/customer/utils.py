
def update_customer(user_customer_to_update, customer_items_to_update):

    user_customer_to_update.country = customer_items_to_update.get('country')
    user_customer_to_update.city = customer_items_to_update.get('city')
    user_customer_to_update.postcode = customer_items_to_update.get('postcode')
    user_customer_to_update.phone = customer_items_to_update.get('phone')
    user_customer_to_update.address1 = customer_items_to_update.get('address1')
    user_customer_to_update.address2 = customer_items_to_update.get('address2')
    user_customer_to_update.description = customer_items_to_update.get('description')
    user_customer_to_update.save()
    
    return