from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from image.forms import ImageForm
from image.models import Image


@login_required(login_url="/account/login/")
@require_POST
@csrf_exempt
def upload_image(request):
    form = ImageForm(data=request.POST)
    if form.is_valid():
        try:
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return JsonResponse({'status': "1"})
        except:
            return JsonResponse({'status': "0"})


@login_required(login_url="/account/login/")
def list_images(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'image/list_image.html', {"images": images})
