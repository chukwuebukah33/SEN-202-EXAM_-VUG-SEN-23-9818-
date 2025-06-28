from rest_framework import generics
from .models import Manager, Intern, Address
from .serializers import ManagerSerializer, InternSerializer
from .models import Manager, Intern
from rest_framework.views import APIView
from rest_framework.response import Response


class StaffRoleView(APIView):
    def get(self, request):
        roles = []
        for manager in Manager.objects.all():
            roles.append({
                "name": f"{manager.first_name} {manager.last_name}",
                "role": manager.get_role()
            })
        for intern in Intern.objects.all():
            roles.append({
                "name": f"{intern.first_name} {intern.last_name}",
                "role": intern.get_role()
            })
        return Response(roles)


class ManagerListCreateView(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class InternListCreateView(generics.ListCreateAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

class InternRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
