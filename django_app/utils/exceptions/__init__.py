class PriceDoesNotExist(Exception):
    def __init__(self, obj):
        self.obj = obj
        self.message = "(pk: {}, class: {}, title: {}) does not have pricing information".format(
            self.obj.pk,
            self.obj.__class__.__name__,
            self.obj.title
        )

    def __str__(self):
        return self.message


class NotAllowedSelfPrice(Exception):
    def __init__(self, obj):
        self.obj = obj
        self.message = "(pk: {}, class: {}, title: {}) is not allowed to have its own price".format(
            self.obj.pk,
            self.obj.__class__.__name__,
            self.obj.title
        )

    def __str__(self):
        return self.message


class PriceError(Exception):
    def __init__(self, obj, exception):
        self.obj = obj
        self.exception = exception
        self.message = "An error occurred while retrieving (pk: {}, class: {}, title: {})'s price. detail: {}".format(
            self.obj.pk,
            self.obj.__class__.__name__,
            self.obj.title,
            self.exception
        )

    def __str__(self):
        return self.message
