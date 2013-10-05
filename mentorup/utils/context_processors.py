from users.forms import NavMemberSearchForm


def get_navbar_search_form(request):
    return {'nav_member_search_form': NavMemberSearchForm()}
