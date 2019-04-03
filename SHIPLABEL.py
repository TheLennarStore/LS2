##initialize the call for products
products = ', '.join([str(i.item_id) for i in order.items])

if order:
  site = order.site
  if order.ship_costs:
    ship_cost = '$%.2f' % (order.ship_costs(site) or 0)

JobNumber = DWIMBLOCK([
  LEFT, F7, "THE LENNAR STORE", SPACER(250), 'NEEDED: ', IFSET(ship_needby, ship_needby, 'n/a'), 
  NEWLINE,
  LEFT, F7, order.token, '-', str(item.item_id), F1, ' of ', products, 
  NEWLINE, F2, '*', order.token, '*', SPACER(150), F2, '*', order.token + '-' + str(item.item_id), '*', SPACER(100), F7, ship_method, ' to ', ship_state, 
  NEWLINE, ' ', NEWLINE,
  LEFT, F3, 'Requester: ', F1, login_name_first, ' ', login_name_last, SPACER(50), F3, "Phone: ", F1, ship_phone, SPACER(50), F3, "Acct: ", F1, ship_account, 
  NEWLINE, ' ', NEWLINE,
  LEFT, F3, item.tag, SPACER(250), item.longname, 
  NEWLINE,
  LEFT, TABLE(
    [(F3, CENTER, 'Name', 'Size', 'Paper', 'Pages', 'Quantity', 'Ink/Sides', 'Product Code')] + 
    [(F1, CENTER, IFSET(str(name), str(name), str(item.longname)), IFSET(str(size), str(size), " "), IFSET(str(paper), str(paper), " "), 
      IFSET(num_pages, num_pages, " "), IFSET(item.qty, item.qty, " "), 
      IFSET(str(ink), str(ink), " ") + IFSET(str(sides), str(sides), " "), IFSET(str(item.prodcode), str(item.prodcode), " "))], 
    min_widths=[200,50,50,50,50,50,50], border=1, padding=8), 
  NEWLINE, 
  LEFT, wrap, [(F3, IFSET(comments, ['Customer Job Comments: ', F1, LINEWRAP(newline_indent=SPACER(10)), comments, NEWLINE],))], 
  NEWLINE,
  LEFT, wrap, [(F3, IFSET(jobComments, ['Customer Item Comments: ', F1, LINEWRAP(newline_indent=SPACER(10)), jobComments, NEWLINE],))], 
  NEWLINE,
  LEFT, wrap, F3,'Finishing: ', F1, COL, finishing, 
  NEWLINE,

], (18,330), (LEFT, TOP_BASELINE), (540,0), layer=1)

taxamount = taxrate = confprices = handling = ship_cost = total_price = ''

if order:
  site = order.site
  if item.price:
    confprices = '$%.2f' % (item.price() or 0)
  if order.ship_costs:
    ship_cost = '$%.2f' % (order.ship_costs(site) or 0)
  if order.handling_costs:
    handling = '$%.2f' % (order.handling_costs(site) or 0)
  if order.taxamount:
    taxamount = '$%.2f' % (order.taxamount(site) or 0)
  if order.taxinfo:
    if callable(order.taxinfo.taxrate):
      taxrate = '%.2f%%' % (order.taxinfo.taxrate() or 0)
    else:
      taxrate = '%.2f%%' % (order.taxinfo.taxrate or 0)
  if order.total_price:
    total_price = '$%.2f' % (order.total_price(site) or 0)


price = DWIMBLOCK([
  RIGHT,          
  F1, 'Item Price: ', F1, confprices, NEWLINE,
  F1, 'Order Ship Cost: ', F1, ship_cost, NEWLINE,
  F1, 'Handling: ', F1, handling, NEWLINE, 
  F1, 'Tax Rate: ', F1, taxrate, ' @ ', F1, taxamount, NEWLINE, 
  F7, '---------------------', NEWLINE, 
  F1, 'Order Total Price: ', F1, total_price
], (430,60), (LEFT, BOTTOM_BASELINE), (540,0), layer=1)
