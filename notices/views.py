from django.shortcuts import render, get_object_or_404, redirect
from .models import Notice, Category
from .forms import NoticeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q  # <- fixed: import Q for queries

def index(request):
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    notices = Notice.objects.order_by('-created_at')

    # filter expired
    today = timezone.localdate()
    notices = notices.filter(Q(expiry_date__isnull=True) | Q(expiry_date__gte=today))

    if q:
        notices = notices.filter(Q(title__icontains=q) | Q(content__icontains=q))
    if cat:
        notices = notices.filter(category__id=cat)

    categories = Category.objects.all()
    return render(request, 'notices/index.html', {'notices': notices, 'categories': categories})

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'notices/notice_detail.html', {'notice': notice})

@login_required
def add_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            n = form.save(commit=False)
            n.posted_by = request.user
            n.save()
            messages.success(request, 'Notice added successfully')
            return redirect('notices:index')
    else:
        form = NoticeForm()
    return render(request, 'notices/add_notice.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('notices:index')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'notices/login.html')

def user_logout(request):
    logout(request)
    return redirect('notices:index')
