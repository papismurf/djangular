import factory

from upload.models import Image


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Image

    name = factory.Sequence(lambda n: 'image_%d' % n)

    @factory.post_generation
    def images(self, create, extracted,**kwargs)
        if not create:
            return
        
        if extracted:
            for image in extracted:
                self.images.add(image)
