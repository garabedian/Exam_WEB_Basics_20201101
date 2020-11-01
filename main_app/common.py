class DisabledFormMixin:
    def __init__(self):
        # for (_, field) in self.fields.items():
        # noinspection PyUnresolvedReferences
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
