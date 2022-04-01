# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.contrib.sites.shortcuts import get_current_site
# from django.http import (
#     Http404,
#     HttpResponsePermanentRedirect,
#     HttpResponseRedirect,
# )
# from django.shortcuts import redirect
# from django.urls import reverse, reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.decorators.debug import sensitive_post_parameters
# from django.views.generic.base import TemplateResponseMixin, TemplateView, View
# from django.views.generic.edit import FormView
#
# from ..exceptions import ImmediateHttpResponse
# from ..utils import get_form_class, get_request_param
# from . import app_settings, signals
# from .adapter import get_adapter
# from .forms import (
#     AddEmailForm,
#     ChangePasswordForm,
#     LoginForm,
#     ResetPasswordForm,
#     ResetPasswordKeyForm,
#     SetPasswordForm,
#     SignupForm,
#     UserTokenForm,
# )
# from .models import EmailAddress, EmailConfirmation, EmailConfirmationHMAC
# from .utils import (
#     complete_signup,
#     get_login_redirect_url,
#     get_next_redirect_url,
#     logout_on_password_change,
#     passthrough_next_redirect_url,
#     perform_login,
#     sync_user_email_addresses,
#     url_str_to_user_pk,
# )
#
#
# INTERNAL_RESET_URL_KEY = "set-password"
# INTERNAL_RESET_SESSION_KEY = "_password_reset_key"
#
#
# sensitive_post_parameters_m = method_decorator(
#     sensitive_post_parameters('password', 'password1', 'password2'))
#
#
# class PasswordChangeView(AjaxCapableProcessFormViewMixin, FormView):
#     template_name = (
#         "account/password_change." + app_settings.TEMPLATE_EXTENSION)
#     form_class = ChangePasswordForm
#     success_url = "/MainPage/News"
#
#     def get_form_class(self):
#         return get_form_class(app_settings.FORMS,
#                               'change_password',
#                               self.form_class)
#
#     @sensitive_post_parameters_m
#     def dispatch(self, request, *args, **kwargs):
#         return super(PasswordChangeView, self).dispatch(
#             request, *args, **kwargs)
#
#     def render_to_response(self, context, **response_kwargs):
#         if not self.request.user.has_usable_password():
#             return HttpResponseRedirect(reverse('account_set_password'))
#         return super(PasswordChangeView, self).render_to_response(
#             context, **response_kwargs)
#
#     def get_form_kwargs(self):
#         kwargs = super(PasswordChangeView, self).get_form_kwargs()
#         kwargs["user"] = self.request.user
#         return kwargs
#
#     def form_valid(self, form):
#         form.save()
#         logout_on_password_change(self.request, form.user)
#         get_adapter(self.request).add_message(
#             self.request,
#             messages.SUCCESS,
#             'account/messages/password_changed.txt')
#         signals.password_changed.send(sender=self.request.user.__class__,
#                                       request=self.request,
#                                       user=self.request.user)
#         return super(PasswordChangeView, self).form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         ret = super(PasswordChangeView, self).get_context_data(**kwargs)
#         # NOTE: For backwards compatibility
#         ret['password_change_form'] = ret.get('form')
#         # (end NOTE)
#         return ret
#
#
# password_change = login_required(PasswordChangeView.as_view())
#
#
#
#
#
#
#
#














# class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):

# def testCustom(request):
#     return HttpResponse("Ha Ha Ha ")

    # success_url = "/MainPage/News"
    # def send_confirmation_mail(self, request, emailconfirmation, signup):
    #     current_site = get_current_site(request)
    #     activate_url = self.get_email_confirmation_url(request,emailconfirmation)
    #     ctx = {
    #         "user": emailconfirmation.email_address.user,
    #         "activate_url": activate_url,
    #         "current_site": current_site,
    #         "key": emailconfirmation.key,
    #     }
    #     if signup:
    #         email_template = 'account/email/email_confirmation_signup'
    #     else:
    #         email_template = 'account/email/email_confirmation'
    #     self.send_mail(email_template,
    #                    emailconfirmation.email_address.email,
    #                    ctx)
    #
    # def get_email_confirmation_url(self, request, emailconfirmation):
    #     pass
    #
    # def send_mail(self, template_prefix, email, context):
    #     msg = self.render_mail(template_prefix, email, context)
    #     msg.send()
    #
    # def confirm_email(self, request, email_address):
    #     """
    #     Marks the email address as confirmed on the db
    #     """
    #     email_address.verified = True
    #     email_address.set_as_primary(conditional=True)
    #     email_address.save()
    #
    # def render_mail(self, template_prefix, email, context):
    #     """
    #     Renders an e-mail to `email`.  `template_prefix` identifies the
    #     e-mail that is to be sent, e.g. "account/email/email_confirmation"
    #     """
    #     subject = render_to_string('{0}_subject.txt'.format(template_prefix),
    #                                context)
    #     # remove superfluous line breaks
    #     subject = " ".join(subject.splitlines()).strip()
    #     subject = self.format_email_subject(subject)
    #
    #     from_email = self.get_from_email()
    #
    #     bodies = {}
    #     for ext in ['html', 'txt']:
    #         try:
    #             template_name = '{0}_message.{1}'.format(template_prefix, ext)
    #             bodies[ext] = render_to_string(template_name,
    #                                            context).strip()
    #         except TemplateDoesNotExist:
    #             if ext == 'txt' and not bodies:
    #                 # We need at least one body
    #                 raise
    #     if 'txt' in bodies:
    #         msg = EmailMultiAlternatives(subject,
    #                                      bodies['txt'],
    #                                      from_email,
    #                                      [email])
    #         if 'html' in bodies:
    #             msg.attach_alternative(bodies['html'], 'text/html')
    #     else:
    #
    #         msg = EmailMessage(subject,
    #                            bodies['html'],
    #                            from_email,
    #                            [email])
    #         msg.content_subtype = 'html'  # Main content is now text/html
    #     return msg
    #
    # def format_email_subject(self, subject):
    #     pass
    #
    # def get_from_email(self):
    #     pass
