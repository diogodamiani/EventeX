# coding=utf-8

from django.core.urlresolvers import reverse
from django.http              import HttpResponse, HttpResponseRedirect
from django.shortcuts         import render_to_response, get_object_or_404
from django.template          import RequestContext

from forms                    import SubscriptionForm
from models                   import Subscription
from utils                    import send_subscription_email

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    form = SubscriptionForm()

    context = RequestContext(request, {'form': form})
    return render_to_response('subscriptions/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscriptions/new.html', context)

    # Não salva o objeto imediatamente para verificar se o email esta com string vazia
    # Antes: subscription = form.save()
    subscription = form.save(commit=False)
    
    # Atribui o valor do form ou None, caso venha uma string vazia.
    subscription.email = form.cleaned_data['email'] or None
    
    # Salva definitivamente o objeto no banco
    subscription.save()

    # Envia email de confirmação
    send_subscription_email(subscription)

    return HttpResponseRedirect(
        reverse('subscriptions:success', args=[ subscription.pk ]))

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscriptions/success.html', context)
    