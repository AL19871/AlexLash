def update_order(current_order, order_address, order_phone, order_submit, delete_order=False):
    
    if current_order:
        if order_submit == 'submit':
                
            current_order.status = 'Submitted'
            current_order.address = order_address
            current_order.phone = order_phone
            current_order.save()
        elif delete_order:
            current_order.delete()
        else:
            current_order.status = 'Canceled'
            current_order.address = order_address
            current_order.phone = order_phone
            current_order.save()
    return