# context processors

def platform_info(request):
    """

    """
    return {
        "platform_info": request.platform
            }
