from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, CommentEditView,ProfileView,ProfileEditView,AddFollower,RemoveFollower,\
AddLike,Dislike,UserSearch,ListFollowers,AddCommentLike,CommentDislike, CommentReplyView,PostNotification,FollowNotification, RemoveNotification,\
CreateThread,ListThreads, ThreadView, CreateMessage,ThreadNotification,SharedPostView,Explore

urlpatterns = [
    path("feed",PostListView.as_view(), name="post-list"),
    path("explore/tags",Explore.as_view(),name="explore"),
    path("post/id:<int:pk>/view",PostDetailView.as_view(),name="post-detail"),
    path("post/id:<int:pk>/edit",PostEditView.as_view(),name="post-edit"),
    path("post/id:<int:pk>/delete",PostDeleteView.as_view(),name="post-delete"),
    path("post/id:<int:post_pk>/comment/id:<int:pk>/delete",CommentDeleteView.as_view(),name="comment-delete"),
    path("post/id:<int:post_pk>/comment/id:<int:pk>/edit",CommentEditView.as_view(),name="comment-edit"),
    path("post/id:<int:post_pk>/comment/id:<int:pk>/like",AddCommentLike.as_view(),name="comment-like"),
    path("post/id:<int:post_pk>/comment/id:<int:pk>/dislike",CommentDislike.as_view(),name="comment-dislike"),
    path("post/id:<int:post_pk>/comment/id:<int:pk>/reply",CommentReplyView.as_view(),name="comment-reply"),
    path("post/id:<int:pk>/like",AddLike.as_view(),name="like"),
    path("post/id:<int:pk>/dislike",Dislike.as_view(),name="dislike"),
    path("post/id:<int:pk>/share",SharedPostView.as_view(),name="share"),
    path("profile/id:<int:pk>/view",ProfileView.as_view(),name="profile"),
    path("profile/id:<int:pk>/edit",ProfileEditView.as_view(),name="profile-edit"),
    path("profile/id:<int:pk>/followers/add",AddFollower.as_view(),name="add-follower"),
    path("profile/id:<int:pk>/followers/remove",RemoveFollower.as_view(),name="remove-follower"),
    path("profile/id:<int:pk>/followers/list",ListFollowers.as_view(),name="list-followers"),
    path("search/user",UserSearch.as_view(),name="profile-search"),
    path("notification/id:<int:notification_pk>/post/id:<int:post_pk>/redirect",PostNotification.as_view(),name="post-notification"),
    path("notification/id:<int:notification_pk>/profile/id:<int:profile_pk>/redirect",FollowNotification.as_view(),name="follow-notification"),
    path("notification/id:<int:notification_pk>/thread/id:<int:object_pk>/redirect",ThreadNotification.as_view(),name="thread-notification"),
    path("notification/id:<int:notification_pk>/delete",RemoveNotification.as_view(),name="notification-delete"),
    path("inbox/list",ListThreads.as_view(),name="inbox"),
    path("inbox/create-thread",CreateThread.as_view(),name="create-thread"),
    path("inbox/thread/id:<int:pk>/view",ThreadView.as_view(),name="thread"),
    path("inbox/thread/id:<int:pk>/create-message",CreateMessage.as_view(),name="create-message"),
]