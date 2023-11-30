


from employees.employe_delete import EmployeeDelete
from employees.employee_update import EmployeeUpdate
from employees.get_employees import GetEmployees
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response





from rest_framework import viewsets, status
class Employeeviewset(GetEmployees,EmployeeUpdate,EmployeeDelete,viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        """
        override the list method
        """
        self.include_only = self.request.query_params.get("include_only")
        return super().list(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        """
            Create a new employee.

            Parameters:
            - request (rest_framework.request.Request): HTTP request object.
            - *args: Additional positional arguments.
            - **kwargs: Additional keyword arguments.

            Returns:
            rest_framework.response.Response: Response with creation status.
                - Successful creation: Success message and the registration ID of the created employee.
                - Employee with the same email exists: Message indicating an employee with the given email already exists.
                - Invalid body request: Message for an invalid request body.

            Raises:
            - HTTP_500_INTERNAL_SERVER_ERROR: If an unexpected error occurs during the creation.
        """
        email = request.data.get('email', None)

        try:
        
            # Check if an employee with the given email already exists
            if email and Employee.objects.filter(email=email).exists():
                return Response({'message': 'Employee with this email already exists', 'success': False}, status=status.HTTP_200_OK)

            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                try: 
                    employee = serializer.save()
                    response_data = {
                        'message': 'Employee created successfully',
                        'regid': employee.id,  # Assuming 'id' is the primary key field
                        'success': True
                    }
                    return Response(response_data, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({'message': 'Employee creation failed', 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'message': 'Invalid body request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(e)

