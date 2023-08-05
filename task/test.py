
def process_lots(lot_ids):
    #
    stock_dict = {}
    quantity_list = []
    #
    stock_locations_object = self.env['stock.production.lot'].search([('id','in',lot_ids)])
    if stock_locations_object:
        stock_quants = self.env['stock.quant'].search([('lot_id','in',stock_locations_object.ids)])
        #
        for item in stock_quants:
            stock_dict = {
                item.location_id.name: item.qty_available
            }
            return stock_dict



