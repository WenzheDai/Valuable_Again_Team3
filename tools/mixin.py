from django.contrib.auth.decorators import login_required

"""use the login_required---for multiple pages"""
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        # call the as_view of father class
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)