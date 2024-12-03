from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GSTCalculator(APIView):
    def post(self, request):
        try:
            base_amount = request.data.get('base_amount')
            total_amount = request.data.get('total_amount')
            gst_rate = request.data.get('gst_rate')
            
            if gst_rate is None:
                return Response({"error": "GST rate is required"}, status=status.HTTP_400_BAD_REQUEST)

            gst_rate = float(gst_rate)
            results = {}

            # Exclusive GST Calculation
            if base_amount is not None:
                base_amount = float(base_amount)
                gst_exclusive = base_amount * (gst_rate / 100)
                total_exclusive = base_amount + gst_exclusive
                
                results['exclusive'] = {
                    'gst': round(gst_exclusive, 2),
                    'total_amount': round(total_exclusive, 2)
                }
            print ('gst one is' ,'gst')
            print('total_amount one is','total_amount')

            # Inclusive GST Calculation
            if total_amount is not None:
                total_amount = float(total_amount)
                base_inclusive = total_amount / (1 + gst_rate / 100)
                gst_inclusive = total_amount - base_inclusive
                
                results['inclusive'] = {
                    'gst': round(gst_inclusive, 2),
                    'base_amount': round(base_inclusive, 2),
                    'total_amount': round(total_amount, 2)
                }
            print ('gst two is' ,'gst')
            print('total_amount two is','total_amount')

            return Response(results, status=status.HTTP_200_OK)

        except ValueError:
            return Response({"error": "Base amount and total amount must be valid numbers"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)