from django.http import HttpResponse

def index(request):
    return HttpResponse(f"Hello USER", status=200)

def articles(reques):
    return HttpResponse('Maqolalar', status=200)

def special_case_2003(request):
    html = """
    <html>
    <head>
    MAQOLALAR
    <body>
    <strong><br>2003-yildagi eng mashxur</strong><br>
    ("Sariq dev", 1994)<br>
    ("Shayanat", 1998)<br>
    ("Bolaligim", 1994)<br>
    ("Urushning so'ngi qurboni", 2000)<br>
    ("Xamsa", 1483)<br>
    ("Ikki eshik orasi", 1996)<br>
    ("O'tgan kunlar", 1916)<br>
    ("Otamdan qolgan dalalar", 1968)<br>
    </body>
    </html>
    """
    return HttpResponse(html)
