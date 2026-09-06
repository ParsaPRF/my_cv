def language_context(request):
    lang = request.COOKIES.get('lang', 'en')
    return {'lang': lang}
