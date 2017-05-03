import requests

from django.shortcuts import render, redirect
from django.conf import settings

from shopify_install.models import Token

SHOPIFY_APP_HOST = settings.SHOPIFY_APP_HOST
SHOPIFY_APP_URL = settings.SHOPIFY_APP_URL
SHOPIFY_API_KEY = settings.SHOPIFY_API_KEY
SHOPIFY_API_SECRET = settings.SHOPIFY_API_SECRET

def install(request):
    """
    Link merchanges will be sent to to install this App in their store
    """
    shop = request.GET['shop']
    scopes = "read_customers,read_products,read_orders"
    install_url = "http://%(shop)s/admin/oauth/authorize?client_id=%(key)s&scope=%(scopes)s&redirect_uri=%(app_url)s/shopify_install/callback/" % {
        'shop': shop,
        'key': SHOPIFY_API_KEY,
        'app_url': SHOPIFY_APP_URL,
        'scopes': scopes,
    }
    return redirect(install_url)

def callback(request):
    """
    After 'install' the merchant grants permissions and Shopify redirects back
    to this URL

    Get access token from Shopify and save
    """
    shop = request.GET['shop']
    code = request.GET['code']
    hmac = request.GET['hmac']

    resp = requests.post("https://%s/admin/oauth/access_token"%shop, data={
        'client_id': SHOPIFY_API_KEY,
        'client_secret': SHOPIFY_API_SECRET,
        'code': code,
    })
    resp.raise_for_status()

    data = resp.json()
    Token.objects.create(shop=shop, token=data['access_token'])

    return redirect('/')
