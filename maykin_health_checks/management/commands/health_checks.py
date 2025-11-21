from django.core.management.base import BaseCommand
from django.utils.module_loading import import_string

from msgspec import UNSET

from ...runner import HealthChecksRunner


class Command(BaseCommand):
    help = "Run all health checks"

    def add_arguments(self, parser):
        parser.add_argument(
            "--checks-collector",
            help="Import path to the collector callable.",
            required=True,
        )
        parser.add_argument(
            "--include-success",
            action="store_true",
            help="Whether to only show health checks that failed.",
            default=False,
        )

    def handle(self, *args, **options):
        checks_collector_fn = import_string(options["checks_collector"])
        include_success = options.get("include_success", False)
        runner = HealthChecksRunner(
            checks_collector=checks_collector_fn, include_success=include_success
        )
        results = runner.run_checks()

        for result in results:
            if include_success and result.success:
                self.stdout.write(
                    self.style.SUCCESS(f"Correctly configured: {result.identifier}")
                )
                continue

            self.stdout.write(
                self.style.ERROR(f"Error {result.identifier}: {result.message}")
            )
            if hasattr(result, "extra") and result.extra != UNSET:
                self.stdout.write(self.style.ERROR(str(result.extra)))
