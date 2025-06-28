from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Manager, Intern
from .serializers import ManagerSerializer, InternSerializer

class StaffRoleView(APIView):
    def get(self, request):
        roles = []
        for manager in Manager.objects.all():
            roles.append({
                'name': f"{manager.first_name} {manager.last_name}",
                'role': manager.get_role()
            })
        for intern in Intern.objects.all():
            roles.append({
                'name': f"{intern.first_name} {intern.last_name}",
                'role': intern.get_role()
            })
        return Response(roles)
