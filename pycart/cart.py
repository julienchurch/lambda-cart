def _lfilter(f, i):
  return list(filter(f, i))

def get_cart(session):
  return session.get('cart', [])

def filter_by_pid(pid, cart):
  return _lfilter(lambda l: l['pid'] == pid, cart)

def filter_by_not_pid(pid, cart):
  return _lfilter(lambda l: l['pid'] != pid, cart)

def purge_empty(cart):
  purged = _lfilter(lambda l: l['qty'] >= 1, cart)
  return purged

def sort_by_pid(cart, reverse=False):
  return sorted(cart, key=lambda l: l['pid'], reverse=reverse)

def sort_by_qty(cart, reverse=False):
  return sorted(cart, key=lambda l: l['qty'], reverse=reverse)

def cart_eq(c1, c2):
  return sort_by_pid(c2) == sort_by_pid(c2)

def item_eq(l1, l2):
  is_pid_same = l1['pid'] == l2['pid']
  is_opt_same = l2['opt'] == l2['opt']
  return is_pid_same and is_opt_same

def make_line(pid, qty, opt):
  return { 'pid' : pid
         , 'qty' : qty
         , 'opt' : opt
         }

def update_line_qty(pid, new_qty, cart):
  tmp_cart = filter_by_not_pid(pid, cart)
  if new_qty <= 0:
    return tmp_cart
  ol = filter_by_pid(pid, cart)
  if ol:
    opt = ol[0].get('opt', [])
  return tmp_cart + [make_line(pid, new_qty, opt)]

def add_to_line_qty(pid, amt, cart):
  ol = filter_by_pid(pid, cart)
  if ol:
    oq = ol[0]['qty'] 
  else:
    oq = 0
  return update_line_qty(pid, (amt + oq), cart)

def sub_from_line_qty(pid, amt, cart):
  return add_to_line_qty(pid, (-amt), cart)

def increment_line_qty(pid, cart):
  return add_to_line_qty(pid, 1, cart)

def decrement_line_qty(pid, cart):
  return sub_from_line_qty(pid, 1, cart)

def get_line(pid, opt, cart):
  filtered = filter_by_pid(pid, cart)
  if filtered:
    is_same_pid = filtered[0]['pid'] == pid
    is_same_opt = filtered[0]['opt'] == opt
    if is_same_pid and is_same_opt:
      return filtered[0]
  return make_line(pid, 0, opt)

def merge_lines(l1, l2):
  if not item_eq(l1, l2):
    raise Exception
  qty_sum = l1['qty'] + l2['qty']
  return make_line(l1['pid'], qty_sum, l1['opt'])


def add_to_cart(line, cart):
  pid, qty, opt = nl['pid'], nl['qty'], nl['opt']

  ol = filter_by_pid(pid, cart)
  if ol:

  return cart + [line]






