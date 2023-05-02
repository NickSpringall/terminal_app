from search_functions import prod_search
from item_display_functions import product_disp, sort_display_order
from cart_functions import add_to_cart, search_restart
from checkout_functions import checkout, sub_total
from postage_functions import shipping, total_shipping_weight
from order_summary_functions import order_summary

restart = "restart"
prod_list = []

while restart == "restart":
    sort_display_order(product_disp(prod_search(prod_list)))
    add_to_cart()
    cart_loop = search_restart()
    restart = cart_loop[0]
    prod_list = cart_loop[1]

checkout()

sub = sub_total()
ship = shipping(total_shipping_weight())

order_summary(sub, ship)

