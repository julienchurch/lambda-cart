from cart import *

i1 = make_item(1, {})
i2 = make_item(2, {})
i3 = make_item(3, { 'color' : 'blue' })
i4 = make_item(3, { 'color' : 'red' })

l1 = make_line(i1, 10)
l2 = make_line(i2, 5)
l3 = make_line(i3, 20)
l4 = make_line(i4, 2)
l5 = make_line(i4, 0)

c0 = make_cart(l1)
c1 = make_cart(l4, l1, l2, l3)
c2 = make_cart(l1, l4, l3, l2, l5)
