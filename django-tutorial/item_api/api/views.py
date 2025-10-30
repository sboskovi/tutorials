from django.db.models import F
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ItemSerializer, EmployeeSerializer, CompanySerializer
from base.models import ItemModel, Employee, Company


# class ItemsView(APIView):
#     @staticmethod
#     def get(request):
#         order_by = request.GET.get("order_by", "created_at")
#         data = ItemModel.objects.order_by(order_by)
#         serializer = ItemSerializer(data, many=True)
#         return Response(serializer.data)


class ItemsView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.order_by("-created_at")
    serializer_class = ItemSerializer

    # def get(self, request, *args, **kwargs):
    @staticmethod
    def get(request):
        order_by = request.GET.get("order_by", "created_at")
        data = ItemModel.objects.order_by(order_by)
        serializer = ItemSerializer(data, many=True)
        return Response(data=serializer.data)


class ItemView(APIView):
    @staticmethod
    def get(_, pk):
        item = ItemModel.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        item = ItemModel.objects.get(pk=pk)
        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(_, pk):
        item = ItemModel.objects.get(pk=pk)
        item.delete()
        return Response(f"Item {pk} deleted successfully")


class AddItem(APIView):
    @staticmethod
    def post(request):
        item_serializer = ItemSerializer(data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response(item_serializer.data, status=status.HTTP_201_CREATED)
        return Response(item_serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class EmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @staticmethod
    def get(_):
        employees = Employee.objects.filter(company__chair_no__gt=F("company__employee_no"))
        # employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class CompanyView(APIView):
    @staticmethod
    def get(_):
        companies = Company.objects.order_by("pk")
        # ============================= DON'T DO: =============================
        # serializer = CompanySerializer(data=companies, many=True)
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
