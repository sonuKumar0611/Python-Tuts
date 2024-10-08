from django.shortcuts import render, redirect, HttpResponseRedirect 
from django.contrib.auth.hashers import check_password 
from django.views import View 
  
  
class Login(): 
    return_url = None
  
    def post(self, request): 
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        customer = Customer.get_customer_by_email(email) 
        error_message = None
        if customer: 
            flag = check_password(password, customer.password) 
            if flag: 
                request.session['customer'] = customer.id
  
                if Login.return_url: 
                    return HttpResponseRedirect(Login.return_url) 
                else: 
                    Login.return_url = None
                    return redirect('my_shop') 
            else: 
                error_message = 'Invalid !!'
        else: 
            error_message = 'Invalid !!'
  
        print(email, password) 
        return render(request, 'login.html', {'error': error_message}) 
  
  
def logout(request): 
    request.session.clear() 
    return redirect('login')