from django.db import IntegrityError
from django.db.models.fields.related import OneToOneField
from django.db.models.fields.related_descriptors import ReverseOneToOneDescriptor


class AutoRelatedObjectDescriptor(ReverseOneToOneDescriptor):
    def __get__(self, instance, owner=None):
        try:
            return super(AutoRelatedObjectDescriptor, self).__get__(instance, owner)
        except self.related.model.DoesNotExist:
            kwargs = {
                self.related.field.name: instance,
            }
            rel_obj = self.related.model.default_manager.create(**kwargs)
            setattr(instance, self.related.get_cache_name(), rel_obj)
            return rel_obj


class AutoOnetoOneField(OneToOneField):
    related_accessor_class = AutoRelatedObjectDescriptor
