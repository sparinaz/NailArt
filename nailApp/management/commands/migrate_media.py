from pathlib import Path

from django.core.management.base import BaseCommand
from django.conf import settings
import cloudinary.uploader


class Command(BaseCommand):
    help = "Migrate local media files to Cloudinary"

    def handle(self, *args, **options):

        media_root = Path(settings.MEDIA_ROOT)

        files = files = media_root.rglob("*")

        for file_path in files:
            if file_path.is_file():
                relative_path = file_path.relative_to(media_root).as_posix()
                with open(file_path, "rb") as file:
                    public_id = Path(relative_path).with_suffix("").as_posix()
                    cloudinary.uploader.upload(
                        file,
                        public_id=public_id,
                        overwrite=True,
                    )
                self.stdout.write(str(relative_path)
                            )
                