class ReadOnlyMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fild in self.fields.values():
            fild.widget.atrs["readonly"] = True