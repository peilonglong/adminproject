from django.conf.urls import url

from x_admin import views
from x_admin.views import *

app_name = "x_admin"

urlpatterns = [
    # url(r'register', Register.as_view(), name="register"),
    url(r'login', Login.as_view(), name="login"),
    url(r'viplist', Viplist.as_view(), name="viplist"),
    url(r'vipedit', Vipedit.as_view(), name="vipedit"),
    url(r'vipdel', Vipdel.as_view(), name="Vipdel"),
    url(r'adminlist', Adminlist.as_view(), name="adminlist"),
    url(r'adminadd', Adminadd.as_view(), name="adminadd"),
    url(r'adminedit', Adminedit.as_view(), name="adminedit"),
    url(r'admindel', Admindel.as_view(), name="admindel"),
    url(r'logout', Logout.as_view(), name="logout"),
    url(r'', Index.as_view(), name="index")
]
handler404=views.page_not_found