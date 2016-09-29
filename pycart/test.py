from cart import *

sample_line1 = { 
    'pid' : 1
  , 'qty' : 2
  , 'opt' : [{ 'color' : 'blue' }]
  }

sample_line2 = {
    'pid' : 2
  , 'qty' : 8
  , 'opt' : []
  }

sample_line3 = {
    'pid' : 3
  , 'qty' : 5
  , 'opt' : []
  }

sample_line4 = {
    'pid' : 4
  , 'qty' : 0
  , 'opt' : []
  }

sample_cart = [
    sample_line1
  , sample_line2
  , sample_line3
  , sample_line4
  ]

def test_get_cart_empty():
 session = {}
 assert get_cart(session) == []

def test_get_cart_nonempty():
  ''' 
  Here we go with the duck typing 👌 
  '''
  session = { 'cart' : ['dummy'] }
  assert get_cart(session) == ['dummy']

def test_purge_empty():
  purged = purge_empty(sample_cart)
  assert purged == sample_cart[:-1]

#  def test_add_to_line_qty():
  #  sc2 = add_to_line_qty(1, 2, sample_cart)
  #  new_sl1 = { 
      #  'pid' : 1 
    #  , 'qty' : 4
    #  , 'opt' : []
    #  }
  #  assert sc2 == []
