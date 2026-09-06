def localize_obj(obj, lang, fields):
    """
    Return a dict with localized field values.
    If lang=='fa' and field_fa exists and is not empty, use it.
    Otherwise use the original field.
    """
    result = {}
    for field in fields:
        if lang == 'fa':
            fa_field = f'{field}_fa'
            fa_val = getattr(obj, fa_field, None)
            if fa_val:
                result[field] = fa_val
            else:
                result[field] = getattr(obj, field, '')
        else:
            result[field] = getattr(obj, field, '')
    return result


def localize_profile(profile, lang):
    if not profile:
        return None
    data = localize_obj(profile, lang, ['title', 'bio'])
    data['name'] = profile.name
    data['age'] = profile.age
    data['location'] = profile.location
    data['email'] = profile.email
    data['phone'] = profile.phone
    data['linkedin'] = profile.linkedin
    data['github'] = profile.github
    data['instagram'] = profile.instagram
    data['photo'] = profile.photo
    data['cv_file'] = profile.cv_file
    return data


def localize_categories(categories, lang):
    result = []
    for cat in categories:
        data = localize_obj(cat, lang, ['name'])
        data['skills'] = []
        for skill in cat.skills.all():
            s = localize_obj(skill, lang, ['name', 'description'])
            data['skills'].append(s)
        result.append(data)
    return result


def localize_education(items, lang):
    result = []
    for item in items:
        data = localize_obj(item, lang, ['title', 'institution', 'period', 'description'])
        result.append(data)
    return result


def localize_experience(items, lang):
    result = []
    for item in items:
        data = localize_obj(item, lang, ['title', 'period', 'description'])
        result.append(data)
    return result


def localize_project_categories(categories, lang):
    result = []
    for cat in categories:
        data = localize_obj(cat, lang, ['name'])
        result.append(data)
    return result


def localize_projects(projects, lang):
    result = []
    for p in projects:
        data = localize_obj(p, lang, ['title', 'description', 'technologies'])
        data['category'] = localize_obj(p.category, lang, ['name']) if p.category else None
        data['image'] = p.image
        data['github_url'] = p.github_url
        data['demo_url'] = p.demo_url
        data['live_url'] = p.live_url
        result.append(data)
    return result


def localize_programming_languages(items, lang):
    result = []
    for item in items:
        data = localize_obj(item, lang, ['name', 'technologies'])
        data['percentage'] = item.percentage
        result.append(data)
    return result


def localize_certificates(items, lang):
    result = []
    for item in items:
        data = localize_obj(item, lang, ['title', 'institution', 'level'])
        result.append(data)
    return result
