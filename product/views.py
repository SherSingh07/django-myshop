from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import *
from django.views.decorators.csrf import csrf_exempt

from product.models import *

def home(request):
    """
    home page view for the website
    """
    categories = Category.objects.all()
    return show_category(request, categories[0].id)

def show_category(request, catid=None):
    """
    category list page view for the website
    """
    sub_categories = []
    try:
        if catid:
            category = Category.objects.get(id=catid)
            sub_categories = SubCategory.objects.filter(category=category)
    except:
        pass

    c = {'categories': Category.objects.all(), 'sub_categories': sub_categories}
    return render_to_response('index.html', c)

def show_products(request, subcatid=None):
    """
    products list page view for the website
    """
    products = []
    try:
        if subcatid:
            sub_category = SubCategory.objects.get(id=subcatid)
            products = Product.objects.filter(sub_category=sub_category)
            print "Got Products = ", len(products)
    except:
        pass

    c = {'products': products, 'brands': Brand.objects.all(), 'subcatid': subcatid}
    return render_to_response('products.html', c)

@csrf_exempt
def compare(request):
    """
    compare products page view for the website
    """
    products = []
    for product_id in request.POST.getlist('product_id'):
        products.append(Product.objects.get(id=product_id))

    c = {'products': products}
    return render_to_response('compare.html', c)

def overview(request):
    return HttpResponse('overview todo')

def best_tested(request):
    return HttpResponse('best tested todo')

def supply_demand(request):
    return HttpResponse('supply & demand todo')

def forum(request):
    return HttpResponse('forum todo')

def lake(request):
    return HttpResponse('lake todo')

def offers(request, product_id):
    """
    get offers for given product id
    and pass them onto the template
    """
    product = Product.objects.get(id=product_id)
    offers  = Offer.objects.filter(product=product)

    c = {"offers": offers, "product": product}

    return render_to_response('offer.html', c)
