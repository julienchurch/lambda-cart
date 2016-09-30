def make_item(uid, opt):
  return { 
      'uid' : uid
    , 'opt' : opt
    }

def make_line(item, qty):
  return {
      'item' : item
    , 'qty' : qty
    }

def make_cart(*lines):
  return [*lines]

def _lfilter(f, l):
  return list(filter(f, l))

def item_eq(i1, i2):
  return i1 == i2

def line_eq(l1, l2):
  return item_eq(li['item'], l2['item'])

# Cart functions
def get_cart(session):
  return session.get('cart', [])

def purge_empty(cart):
  purged = _lfilter(lambda l: l['qty'] >= 1, cart)
  return purged

def filter_by_uid(uid, cart):
  return _lfilter(lambda l: l['item']['uid'] == uid, cart)

def filter_by_not_uid(uid, cart):
  return _lfilter(lambda l: l['item']['uid'] != uid, cart)

def filter_by_item(item, cart):
  return _lfilter(lambda l: item_eq(l['item'], item), cart)

def filter_by_not_item(item, cart):
  return _lfilter(lambda l: not item_eq(l['item'], item), cart)

def sort_by_uid(cart, reverse=False):
  # I don't think it's necessary to sort by `item` because `sorted`
  # normalizes its output somehow (?) so two carts sorted by uid
  # should always compare correctly
  return sorted(cart, key=lambda l: l['item']['uid'], reverse=reverse)

def sort_by_qty(cart, reverse=False):
  return sorted(cart, key=lambda l: l['qty'], reverse=reverse)

def cart_eq(c1, c2):
  pc1, pc2 = purge_empty(c1), purge_empty(c2)
  return sort_by_uid(pc1) == sort_by_uid(pc2)

def get_line(item, cart):
  item_in_cart = filter_by_item(item, cart)
  if item_in_cart:
    return item_in_cart[0]
  return make_line(item, 0)

def update_line_qty(item, new_qty, cart):
  tmp_cart = filter_by_not_item(item, cart)
  if new_qty <= 0:
    return tmp_cart
  return tmp_cart + [make_line(item, new_qty)]

def add_to_line_qty(item, amt, cart):
  old_qty = get_line(item, cart)['qty']
  return update_line_qty(item, (amt + old_qty), cart)

def sub_from_line_qty(item, amt, cart):
  return add_to_line_qty(item, (-amt), cart)

def increment_line_qty(item, cart):
  return add_to_line_qty(item, 1, cart)

def decrememnt_line_qty(item, cart):
  return sub_from_line_qty(item, 1, cart)

def add_to_cart(item, cart, qty=1):
  return add_to_line_qty(item, qty, cart)

