
from django.http.response import HttpResponse
from django.views.generic import TemplateView

# functionBasedView
def function(request):
    obj = HttpResponse('hello')
    return obj

# classBasedView
class HelloClass(TemplateView):
    # このクラスを呼び出した時に、持ってくるHTMLファイルを指定
    template_name = 'hello.html'