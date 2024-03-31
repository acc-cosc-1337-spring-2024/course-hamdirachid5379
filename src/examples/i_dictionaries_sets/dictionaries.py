def test_config():
    return True

def add_inventory(widget_name, quantity, widgets):
    if widget_name in widgets:
        widgets[widget_name] = quantity
        print(quantity)
    else:
        widgets[widget_name] += quantity
        print([widget_name], quantity)

def remove_inventory_widget(widget_name, widgets):
    if widget_name in widgets:
        del widgets[widget_name]
        return 'Record deleted'
    
    else:
        return 'Item not found'


