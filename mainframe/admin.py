from django.contrib import admin
from django.db.models.deletion import CASCADE

# Register your models here.
from mainframe.models import User, Tag, Role, Question, Answer, Comment, CommentAnswer, UpvoteA, UpvoteQ, DownvoteQ, Bookmark


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class RoleAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class CommentAnswerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class UpvoteAAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class UpvoteQAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class DownvoteQAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class BookmarkAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentAnswer, CommentAnswerAdmin)

admin.site.register(UpvoteQ, UpvoteQAdmin)
admin.site.register(DownvoteQ, DownvoteQAdmin)
admin.site.register(UpvoteA, UpvoteAAdmin)

admin.site.register(Bookmark, BookmarkAdmin)