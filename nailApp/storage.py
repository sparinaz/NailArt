from django.core.files.storage import Storage
import cloudinary.uploader
from pathlib import Path
from cloudinary import api


class CloudinaryMediaStorage(Storage):

    def get_available_name(self, name, max_length=None):
        return name

    def _save(self, name, content):
        public_id = Path(name).with_suffix("").as_posix()
        result = cloudinary.uploader.upload(
            content,
            public_id=public_id,
            overwrite=True
    )



        return name

    def delete(self, name):
        public_id = Path(name).with_suffix("").as_posix()

        result = cloudinary.uploader.destroy(
            public_id=public_id
        )

        

    def exists(self, name):
        public_id = Path(name).with_suffix("").as_posix()

        try:
            api.resource(public_id)
            return True

        except cloudinary.exceptions.NotFound:
            return False

    def url(self, name):
        public_id = Path(name).with_suffix("").as_posix()
        format = Path(name).suffix.lstrip(".")
        image = cloudinary.CloudinaryImage(public_id)

        return image.build_url(secure=True,
                               format=format)