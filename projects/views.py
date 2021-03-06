from django.shortcuts import render
from . import models
import projects
from django.core.paginator import Paginator
from users import mixins as user_mixins
from django.views.generic import ListView, DetailView, View, UpdateView, FormView, DeleteView
from . import models, forms
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def home_projects(request):
    all_project = models.Project.objects.all()[:1]
    second_project = models.Project.objects.all()[1:2]
    return render(request, "home.html", context={"potato": all_project, "second": second_project})


def all_projects(request):
    page = request.GET.get("page")
    all_projects = models.Project.objects.all()
    paginator = Paginator(all_projects, 6)
    projects = paginator.get_page(page)

    fav_projects = models.Project.objects.filter(views="1")
    pages = Paginator(fav_projects, 6)
    fav_projects_all = pages.get_page(page)


    return render(request, "projects/project_list.html", context={"potato": projects, "fav": fav_projects_all})



class CreateProjectView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateProjectForm
    template_name = "projects/project_create.html"
    def form_valid(self, form):
        project = form.save()
        project.user = self.request.user
        project.save()
        # project.success(self.request, "Photo Uploaded")
        return redirect(reverse("core:project_list"))


class ProjectDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Project

class EditProjectView(UpdateView):

    model = models.Project
    template_name = "projects/project_edit.html"
    fields = (
        "title",
        "desc",
        "thumnail_img",
        "tag",
        "git",
    )
    def get_success_url(self):
        return reverse("core:project_list")


class DeleteProjectView(DeleteView):

    model = models.Project
    template_name = "projects/project_delete.html"
    def get_success_url(self):
        return reverse("core:project_list")





