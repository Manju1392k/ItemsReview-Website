from django.shortcuts import redirect, render

from .forms import ReviewForm

from django.contrib import messages

from .models import Review

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Reviewpage(request):
    itemsreviews = Review.objects.all()
    return render(request, 'review.html', {'itemsreviews':itemsreviews})

def WriteReview(request):
    form = ReviewForm
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Review has been added successfully')
            return redirect('Write')
    return render(request, 'writereview.html', {'form':form})