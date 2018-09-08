from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from src.models import Classroom
from src.serializers import ClassroomSerializer

@csrf_exempt
def classroom_list(request):
    """
    List all code classrooms, or create a new classroom.
    """
    if request.method == 'GET':
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClassroomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def classroom_detail(request, pk):
    """
    Retrieve, update or delete a code classroom.
    """
    try:
        classroom = Classroom.objects.get(pk=pk)
    except Classroom.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClassroomSerializer(classroom)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClassroomSerializer(classroom, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        classroom.delete()
        return HttpResponse(status=204)