from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

from rest_framework.decorators import action


class EmployeeUpdate:

    @action(detail=True, methods=['put'])
    def update_employee(self, request, *args, **kwargs):
        """
            Update employee details.

            Parameters:
            - request (rest_framework.request.Request): HTTP request object.
            - *args: Additional positional arguments.
            - **kwargs: Additional keyword arguments.
                - 'pk': Employee registration ID from the URL.

            Returns:
            rest_framework.response.Response: Response with update status.
                - Successful update: Success message.
                - No employee found: Message indicating no employee with the given regid.
                - Invalid body request: Message for an invalid request body.

            Raises:
            - HTTP_500_INTERNAL_SERVER_ERROR: If an unexpected error occurs during the update.
        """
        regid = kwargs.get('pk')  # Assuming 'pk' is the parameter for regid in the URL
        
        # Check if an employee with the given regid exists
        try:
            employee = Employee.objects.get(pk=regid)
        except Employee.DoesNotExist:
            return Response({'message': 'No employee found with this regid', 'success': False}, status=status.HTTP_200_OK)

        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'message': 'Employee details updated successfully', 'success': True}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': 'Employee updation failed', 'success': False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'message': 'Invalid body request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)
