from .models import Choices


def context(request):
    """context for layout page"""
    return {
        "category_choices": Choices
    }
