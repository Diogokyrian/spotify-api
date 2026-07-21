# Filtering

singer_filter_fields = {
    "name": ["exact", "icontains"],
    "description": ["exact", "icontains"],
    "created_at": ["exact", "lt", "gt"],
    "updated_at": ["exact", "lt", "gt"],
}

album_filter_fields = {
    "title": ["exact", "icontains"],
    "release_date": ["exact", "lt", "gt"],
    "singer": ["exact"],
    "singer__name": ["exact", "icontains"],
    "created_at": ["exact", "lt", "gt"],
    "updated_at": ["exact", "lt", "gt"],
}
