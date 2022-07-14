import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, Categorie


@method_decorator(csrf_exempt, name="dispatch")
class AdsView(View):
    def get(self, request):
        ads = Ads.objects.all()
        result = []
        for a in ads:
            result.append({
                'id': a.id,
                'name': a.name,
                'author': a.author,
                'price': a.price,

            })
        return JsonResponse(result, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        ads = Ads()

        ads.name = data['name']
        ads.author = data['author']
        ads.price = data['price']
        ads.description = data['description']
        ads.address = data['address']
        ads.is_published = data['is_published']
        ads.save()

        return JsonResponse({
            'id': ads.id,
            'name': ads.name,
            'author': ads.author,
            'price': ads.price,
            'description': ads.description,
            'address': ads.address,
            'is_published': ads.is_published,

        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):
    def get(self, request):
        category = Categorie.objects.all()
        result = []
        for cat in category:
            result.append({
                'id': cat.id,
                'name': cat.name,

            })

        return JsonResponse(result, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        category = Categorie.objects.create(name=data['name'])

        return JsonResponse({
            'id': category.id,
            'name': category.name,
        })


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()
        return JsonResponse({
            'id': ads.id,
            'name': ads.name,
            'author': ads.author,
            'price': ads.price,
            'description': ads.description,
            'address': ads.address,
            'is_published': ads.is_published,

        })


class CategoryDetailView(DetailView):
    model = Categorie

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            'id': category.id,
            'name': category.name,
        })
