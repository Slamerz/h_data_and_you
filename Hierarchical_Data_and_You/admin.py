from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from Hierarchical_Data_and_You import models


admin.site.register(
    models.File,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
