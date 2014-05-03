from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext



def index(request, templates="CustomerManagementApp.html"):
    template_var={}
    return render_to_response(templates, template_var, context_instance=RequestContext(request))


