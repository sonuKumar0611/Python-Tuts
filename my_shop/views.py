from django.shortcuts import render, redirect , HttpResponseRedirect
from my_shop.models import Product 
from my_shop.models import Category 

# Create your views here.
def show_my_shop(request):
    categories= Category.objects.all();
    categoryID = request.GET.get('category') 
    if categoryID: 
        products = Product.get_all_products_by_categoryid(categoryID) 
    else: 
        products = Product.get_all_products() 
  
    data={
        "categories":categories,
        "products":products
    }
    return render(request, "shop_home.html",data)

class Index(): 
    def post(self, request): 
        product = request.POST.get('product') 
        remove = request.POST.get('remove') 
        cart = request.session.get('cart') 
        if cart: 
            quantity = cart.get(product) 
            if quantity: 
                if remove: 
                    if quantity <= 1: 
                        cart.pop(product) 
                    else: 
                        cart[product] = quantity-1
                else: 
                    cart[product] = quantity+1
  
            else: 
                cart[product] = 1
        else: 
            cart = {} 
            cart[product] = 1
  
        request.session['cart'] = cart 
        print('cart', request.session['cart']) 
        return redirect('my_shop') 
  
    def get(self, request): 
        # print() 
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}') 
  
  
def store(request): 
    cart = request.session.get('cart') 
    if not cart: 
        request.session['cart'] = {} 
    products = None
    categories = Category.get_all_categories() 
    categoryID = request.GET.get('category') 
    if categoryID: 
        products = Product.get_all_products_by_categoryid(categoryID) 
    else: 
        products = Product.get_all_products() 
  
    data = {} 
    data['products'] = products 
    data['categories'] = categories 
  
    print('you are : ', request.session.get('email')) 
    return render(request, 'index.html', data)


def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    # Get products and add to cart_items
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total_price += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity
        })
    
    # Pass cart items and total price to the template
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    
    return render(request, 'shop_cart.html', context)

# This will handle both adding, updating, and removing from the cart
def update_cart(request):
    product_id = request.POST.get('product')
    remove = request.POST.get('remove')
    cart = request.session.get('cart', {})

    if product_id:
        quantity = cart.get(product_id, 0)
        if remove:
            if quantity > 1:
                cart[product_id] = quantity - 1
            else:
                cart.pop(product_id)
        else:
            cart[product_id] = quantity + 1
    
    request.session['cart'] = cart
    return redirect('cart') 