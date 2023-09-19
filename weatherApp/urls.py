
from django.urls import path

from weatherApp import views

urlpatterns = [
    path('',views.home,name='home'),
]


# <form action="" method="post" class="col-md-6 col-md-offset-3">
#     {% csrf_token %}
#     <div class="input-group">
#       <input type="text" class="form-control" name="city" placeholder="Search">
#       <div class="input-group-btn">
#         <button class="btn btn-default" type="submit">
#             <span class="input-group-text border fw-bold" id="search-addon">Check!</span>
#         </button>
#       </div>
#       <form>