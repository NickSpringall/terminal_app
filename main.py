from search_functions import prod_search
from item_display_functions import product_disp, sort_display_order
from cart_functions import add_to_cart, search_restart
from checkout_functions import checkout, sub_total
from postage_functions import shipping, total_shipping_weight
from order_summary_functions import order_summary


sort_display_order(product_disp(prod_search()))

search_restart(add_to_cart())

checkout()

sub_total()

shipping(total_shipping_weight())






