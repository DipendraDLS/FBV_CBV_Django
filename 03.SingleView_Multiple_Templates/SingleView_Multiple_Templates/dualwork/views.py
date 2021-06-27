from django.shortcuts import render
from django.views import View

# Create your views here.

#Function Based View to render multiple templates.
def newsfun(request, template_name):
   template_name = template_name
   context ={'info':'This is the live telecast news from meronews.com'}
   return render(request, template_name, context)


#Class Based View to render multiple templates
class NewsClassView(View):
    template_name = ''  # Class Based View ma template lai jahele 'get' method vanda mathi rakheko better manincha.
                        # Yo 'template_name' blank raheko because yeta urls.py bata value auncha.
                        #If blank define garena vani undefined attribute error auncha.
                        
    def get(self, request): #Class Based View le automatic 'get'  method vanera lindaina so we need to specify here.
        context ={'info':'This is the live telecast news from meronews.com'}
        return render(request, self.template_name, context)     #As 'template_name' 'get' method vitra define chaina so we need 
                                                                #to use self.template_name.

