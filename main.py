from search_functions import prod_search
from item_display_functions import product_disp, sort_display_order
from cart_functions import add_to_cart, search_restart
from checkout_functions import checkout, sub_total
from postage_functions import shipping, total_shipping_weight
from order_summary_functions import order_summary

restart = "restart"

while restart == "restart":
    sort_display_order(product_disp(prod_search()))
    add_to_cart()
    restart = search_restart()

checkout()

sub = sub_total()
ship = shipping(total_shipping_weight())

order_summary(sub, ship)

