from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer,BogieChecksheetSerializer
from django.db.models import Q

class WheelSpecificationAPIView(APIView):
    """
    GET and POST /api/forms/wheel-specifications/
    """

    def get(self, request):
        try:
            form_number = request.query_params.get('formNumber')
            submitted_by = request.query_params.get('submittedBy')
            submitted_date = request.query_params.get('submittedDate')

            filters = Q()
            if form_number:
                filters &= Q(form_number=form_number)
            if submitted_by:
                filters &= Q(submitted_by=submitted_by)
            if submitted_date:
                filters &= Q(submitted_date=submitted_date)

            queryset = WheelSpecification.objects.filter(filters)

            response_data = []
            for obj in queryset:
                item = {
                    "formNumber": obj.form_number,
                    "submittedBy": obj.submitted_by,
                    "submittedDate": str(obj.submitted_date),
                    "fields": {
                        "treadDiameterNew": obj.tread_diameter_new,
                        "lastShopIssueSize": obj.last_shop_issue_size,
                        "condemningDia": obj.condemning_dia,
                        "wheelGauge": obj.wheel_gauge
                    }
                }
                response_data.append(item)

            return Response({
                "success": True,
                "message": "Filtered wheel specification forms fetched successfully.",
                "data": response_data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "success": False,
                "message": "An unexpected error occurred while fetching wheel specifications.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            data = request.data
            form_number = data.get('formNumber')
            submitted_by = data.get('submittedBy')
            submitted_date = data.get('submittedDate')
            fields = data.get('fields', {})

            serializer_data = {
                'form_number': form_number,
                'submitted_by': submitted_by,
                'submitted_date': submitted_date,
                'tread_diameter_new': fields.get('treadDiameterNew'),
                'last_shop_issue_size': fields.get('lastShopIssueSize'),
                'condemning_dia': fields.get('condemningDia'),
                'wheel_gauge': fields.get('wheelGauge'),
                'variation_same_axle': fields.get('variationSameAxle'),
                'variation_same_bogie': fields.get('variationSameBogie'),
                'variation_same_coach': fields.get('variationSameCoach'),
                'wheel_profile': fields.get('wheelProfile'),
                'intermediate_wwp': fields.get('intermediateWWP'),
                'bearing_seat_diameter': fields.get('bearingSeatDiameter'),
                'roller_bearing_outer_dia': fields.get('rollerBearingOuterDia'),
                'roller_bearing_bore_dia': fields.get('rollerBearingBoreDia'),
                'roller_bearing_width': fields.get('rollerBearingWidth'),
                'axle_box_housing_bore_dia': fields.get('axleBoxHousingBoreDia'),
                'wheel_disc_width': fields.get('wheelDiscWidth'),
            }

            serializer = WheelSpecificationSerializer(data=serializer_data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True,
                    "message": "Wheel specification submitted successfully.",
                    "data": {
                        "formNumber": form_number,
                        "submittedBy": submitted_by,
                        "submittedDate": submitted_date,
                        "status": "Saved"
                    }
                }, status=status.HTTP_201_CREATED)

            else:
                return Response({
                    "success": False,
                    "message": "Validation failed.",
                    "errors": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "success": False,
                "message": "An unexpected error occurred while submitting wheel specification.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class BogieChecksheetAPIView(APIView):
    """
    POST /api/forms/bogie-checksheet
    """

    def post(self, request):
        try:
            data = request.data
            form_number = data.get('formNumber')
            inspection_by = data.get('inspectionBy')
            inspection_date = data.get('inspectionDate')

            bogie_details = data.get('bogieDetails', {})
            bogie_checksheet = data.get('bogieChecksheet', {})
            bmbc_checksheet = data.get('bmbcChecksheet', {})

            serializer_data = {
                'form_number': form_number,
                'inspection_by': inspection_by,
                'inspection_date': inspection_date,

                'bogie_no': bogie_details.get('bogieNo'),
                'maker_year_built': bogie_details.get('makerYearBuilt'),
                'incoming_div_and_date': bogie_details.get('incomingDivAndDate'),
                'deficit_components': bogie_details.get('deficitComponents'),
                'date_of_ioh': bogie_details.get('dateOfIOH'),

                'bogie_frame_condition': bogie_checksheet.get('bogieFrameCondition'),
                'bolster': bogie_checksheet.get('bolster'),
                'bolster_suspension_bracket': bogie_checksheet.get('bolsterSuspensionBracket'),
                'lower_spring_seat': bogie_checksheet.get('lowerSpringSeat'),
                'axle_guide': bogie_checksheet.get('axleGuide'),
                'cylinder_body': bmbc_checksheet.get('cylinderBody'),
                'piston_trunnion': bmbc_checksheet.get('pistonTrunnion'),
                'adjusting_tube': bmbc_checksheet.get('adjustingTube'),
                'plunger_spring': bmbc_checksheet.get('plungerSpring'),
            }

            serializer = BogieChecksheetSerializer(data=serializer_data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "success": True,
                    "message": "Bogie checksheet submitted successfully.",
                    "data": {
                        "formNumber": form_number,
                        "inspectionBy": inspection_by,
                        "inspectionDate": inspection_date,
                        "status": "Saved"
                    }
                }, status=status.HTTP_201_CREATED)

            else:
                return Response({
                    "success": False,
                    "message": "Validation failed.",
                    "errors": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "success": False,
                "message": "An unexpected error occurred.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)