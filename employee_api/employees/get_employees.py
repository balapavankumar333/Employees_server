from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Employee  # Replace with your actual Employee model
from .serializers import EmployeeSerializer 


class GetEmployees:

    @action(detail=False, methods=['get'])
    def get_employee_list(self, request, *args, **kwargs):
        """
        Get employee details.

        Parameters:
        - request (rest_framework.request.Request): HTTP request object.

        Returns:
        rest_framework.response.Response: Response with employee details.
            - Successful: JSON with employee details and success message.
            - Employee not found: Message indicating no employee with the given ID.
            - Error during retrieval: Error message.

        Usage:
        - Retrieve details of a specific employee by providing their ID as 'regid' query parameter.
        - Retrieve details of all employees by making a request without 'regid'.

        Examples:
        - GET /api/employees/?regid=123: Details of employee with ID 123.
        - GET /api/employees/: Details of all employees.

        Raises:
        - HTTP_500_INTERNAL_SERVER_ERROR: If an unexpected error occurs.
        """
        
        try:
            employee_id = request.query_params.get("regid")

            if employee_id:
                # Single employee request
                employee = Employee.objects.filter(id=employee_id).first()

                if not employee:
                    return Response({"message": f"No employee found with ID {employee_id}", "success": False, "employees": []}, status=status.HTTP_200_OK)

                serializer = EmployeeSerializer(employee)
                return Response({"message": "Employee details found", "success": True, "employees": [serializer.data]}, status=status.HTTP_200_OK)
            else:
                # All employee request
                employees = Employee.objects.all()
                serializer = EmployeeSerializer(employees, many=True)
                return Response({"message": "Employee details found", "success": True, "employees": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": "Error retrieving employee details", "success": False, "employees": []}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
