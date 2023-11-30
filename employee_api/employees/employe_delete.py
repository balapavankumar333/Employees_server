from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

from rest_framework.decorators import action
class EmployeeDelete:

    @action(detail=False, methods=['delete'])
    def delete_employee(self, request, *args, **kwargs):
        """
            Delete an employee.

            Parameters:
            - request (rest_framework.request.Request): HTTP request object.

            Returns:
            rest_framework.response.Response: Response with deletion status.
                - Successful deletion: Success message.
                - Invalid body request: Message for missing or invalid 'regid' in the request body.
                - Employee not found: Message indicating no employee with the given regid.

            Raises:
            - HTTP_500_INTERNAL_SERVER_ERROR: If an unexpected error occurs during deletion.
        """
        try:
            regid = request.data.get("regid")


            if not regid:
                return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)

            # Assuming Employee is your actual model
            employee = Employee.objects.get(pk=regid)
            print(" employee",employee)

            if not employee:
                return Response({"message": f"No employee found with regid {regid}", "success": False}, status=status.HTTP_200_OK)

            employee.delete()

            return Response({"message": "Employee deleted successfully", "success": True}, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({"message": "Employee deletion failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
