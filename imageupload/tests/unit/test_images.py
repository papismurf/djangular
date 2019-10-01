import pytest

from upload.tests.factories import ImageFactory


class TestImages:
    
    @pytest.mark.django_db
    def test_image_uploaders(self):
        """Tests that we can obtain all images and at least one exists."""
        image = ImageFactory()
