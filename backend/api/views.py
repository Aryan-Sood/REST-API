from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):

    # instance = Product.objects.all().order_by("?").first()
    data = request.data
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        data = serializer.save()
        print(data)
        return Response(serializer.data)

    # if request.method != "POST":
    #     return Response({"detail":"GET Not Allowed"},status=400)


    # if instance:
        # data = model_to_dict(model_data, fields=['id','title','price','sale_price'])
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # data['sale_price'] = model_data.sale_price
        # print("data: "+ str(data))
        # data = ProductSerializer(instance).data
   
        # json_data_str = json.dumps(data)
        # return HttpResponse(json_data_str, headers = {"content-type":"application/json"})