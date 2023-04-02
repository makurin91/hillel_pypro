from django.utils.safestring import mark_safe


class ImageSnapshotAdminMixin:

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if isinstance(readonly_fields, (list, tuple)):
            readonly_fields += ('image_field',)
        else:
            readonly_fields = ('image_field',)
        return readonly_fields

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        if isinstance(list_display, (list, tuple)):
            list_display = ('image_field',) + list_display
        else:
            list_display = ('image_field',)
        return list_display

    def image_field(self, obj):
        if not obj.image:
            return 'No image'
        return mark_safe(
            f'<img src="{obj.image.url}" width="64" height="64"/>'
        )

    image_field.short_description = 'Image snapshot'
