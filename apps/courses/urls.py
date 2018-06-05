from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView, CourseVideoView, VideoPlayView, CourseCommentView, AddCommentView



urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),  # 视频列表页
    url(r'^(?P<course_id>.*)/detail/$', CourseDetailView.as_view(), name='course_detail'),  # 课程详情
    url(r'^(?P<course_id>.*)/videos/$', CourseVideoView.as_view(), name='course_videos'),   # 课程视频列表
    url(r'^(?P<course_id>.*)/play_videos/(?P<video_id>.*)/$', VideoPlayView.as_view(), name='play_videos'), # 视频播放页面

    url(r'^(?P<course_id>.*)/comment/$', CourseCommentView.as_view(), name='course_comment'),  # 指定的课程评论列表页面
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),  # 评论当前课程

]

