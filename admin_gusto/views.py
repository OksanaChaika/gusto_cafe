from django.shortcuts import render, redirect
from main_gusto.forms import Message

# Create your views here.
def list_of_messages(request):
    messages = Message.objects.filter(is_processed=False).order_by('pub_date')
    return render(request, 'messages.html', context ={"messages": messages})

def update_message(request, pk):
    Message.objects.filter(pk=pk).update(is_processed=True)
    return redirect('/admin-panel/messages/')

