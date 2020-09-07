from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, PersonalInfoForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import PersonalInfo, Order, Message, Requisition

@login_required
def dashboard(request):
    user = request.user
    if user.first_name or user.last_name:
        name = user.first_name + ' ' + user.last_name
        name = name[1:] if name[0] == ' ' else name[:len(name)-1] if name[len(name)-1] == ' ' else name
    else:
        name = user.username
    try:
        user_groups = user.groups.get()
    except:
        raise Http404
    group = Group.objects.get(id=user_groups.id)
    if group.id == 1:
        return render(request, 'Cabinet/dashboard.html', {'section': 'dashboard', 'name': name})
    elif group.id == 2:
        return render(request, 'Cabinet/dashboard_employee.html', {'section': 'dashboard', 'name': name, 'group': group})
    elif group.id == 3:
        return HttpResponse('Страница руководства')
    elif group.id == 4:
        return HttpResponseRedirect('/admin/')
    else:
        raise Http404

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            group = Group.objects.get(name='Клиент')
            new_user.groups.add(group)
            personal_data = PersonalInfo(user_id=new_user.id)
            personal_data.save()
            return render(request, 'Cabinet/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'Cabinet/register.html', {'user_form': user_form})

@login_required
def personal_info(request):
    user = request.user
    personal_data = PersonalInfo.objects.get(user_id=user.id)
    if request.method == 'POST':
        user_form = PersonalInfoForm(request.POST, request.FILES)
        if user_form.is_valid():
            personal_data.phone = user_form.cleaned_data['phone']
            personal_data.juristical_address = user_form.cleaned_data['juristical_address']
            personal_data.agent_company = user_form.cleaned_data['agent_company']
            personal_data.docs_client = user_form.cleaned_data['docs_client']
            personal_data.save()
            return HttpResponseRedirect('/cabinet')
    else:
        data = {'phone': personal_data.phone, 'juristical_address': personal_data.juristical_address,
                'agent_company': personal_data.agent_company, 'docs_client': personal_data.docs_client}
        user_form = PersonalInfoForm(initial=data)
    return render(request, 'Cabinet/personal.html', {'user': user, 'personal_data': personal_data, 'user_form': user_form})

@login_required
def all_orders(request):
    user = request.user
    orders = Order.objects.filter(client_id=user.id)
    return render(request, 'Cabinet/all_orders.html', {'orders': orders})

@login_required
def current_orders(request):
    user = request.user
    orders = Order.objects.filter(client_id=user.id, status_bool=False)
    return render(request, 'Cabinet/current_orders.html', {'orders': orders})

@login_required
def new_orders(request):
    new_orders = Order.objects.filter(status_getting=False)
    return render(request, 'Cabinet/new_orders.html', {'new_orders': new_orders})

@login_required
def made_req(request):
    user = request.user
    made_reqs = Requisition.objects.filter(employee_id=user.id, status_bool=True)
    return render(request, 'Cabinet/made_req.html', {'made_reqs': made_reqs})

@login_required
def curr_req(request):
    user = request.user
    curr_reqs = Requisition.objects.filter(employee_id=user.id, status_bool=False)
    return render(request, 'Cabinet/curr_req.html', {'curr_reqs': curr_reqs})

@login_required
def get_new_orders(request, pk):
    user = request.user
    order = Order.objects.get(id=pk)
    req = Requisition(employee_id=user.id, order_id=order.id)
    req.save()
    order.status_getting = True
    order.save()
    return HttpResponseRedirect('/cabinet/')

@login_required
def message_page(request):
    user = request.user
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            new_message = Message(user_id=user.id, subject=message_form.cleaned_data['subject'], message=message_form.cleaned_data['message'])
            new_message.save()
            return HttpResponseRedirect('/cabinet')
    else:
        message_form = MessageForm()
    return render(request, 'Cabinet/message.html', {'message_form': message_form})