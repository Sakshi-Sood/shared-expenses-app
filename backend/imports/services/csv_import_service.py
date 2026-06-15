import csv

from imports.models import ImportJob


class CSVImportService:

    @staticmethod
    def analyze(file):

        reader = csv.DictReader(
            file.read().decode("utf-8").splitlines()
        )

        rows = list(reader)

        job = ImportJob.objects.create(
            filename=file.name,
            status="analyzed"
        )

        return {
            "job": job,
            "rows": rows
        }