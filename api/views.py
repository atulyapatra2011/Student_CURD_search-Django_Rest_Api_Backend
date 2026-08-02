from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

@api_view(['GET', 'POST'])
def student(request):

    if request.method == 'GET':
        stu = Student.objects.all().order_by("id")
        paginator = PageNumberPagination()
        paginator.page_size = 3
        result_page = paginator.paginate_queryset(stu, request)
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def studentList(request, id):
    try:
        stu = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(stu, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def StudentSearchAPI(request):

    search = request.GET.get("search", "")

    students = Student.objects.all()

    if search:
        students = students.filter(
            Q(roll_number__icontains=search) |
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search) |
            Q(phone__icontains=search)
        )

    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)