from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser

from .serializers import CSVUploadSerializer
from .services.csv_import_service import CSVImportService


class CSVUploadView(APIView):

    parser_classes = [MultiPartParser]
    serializer_class = CSVUploadSerializer

    def post(self, request):

        serializer = CSVUploadSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        result = CSVImportService.analyze(
            serializer.validated_data["file"]
        )

        return Response(
            {
                "import_job_id": result["job"].id,
                "rows_processed": len(result["rows"])
            },
            status=status.HTTP_200_OK
        )