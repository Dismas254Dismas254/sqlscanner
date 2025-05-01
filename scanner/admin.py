from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Profile, Feedback

# --- Disable deleting users in the admin panel ---
admin.site.unregister(User)

class CustomUserAdmin(DefaultUserAdmin):
    def has_delete_permission(self, request, obj=None):
        return False  # disable delete button for user

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']  # remove "delete selected" action
        return actions

admin.site.register(User, CustomUserAdmin)

# --- Profile admin ---
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'premium_status')
    list_editable = ('premium_status',)
    search_fields = ('user__username',)
    readonly_fields = ('mpesa_code',)

    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Payment Details', {
            'fields': ('cash_pending', 'mpesa_code', 'mpesa_pending', 'premium_status'),
            'classes': ('collapse',),
        }),
    )

    def get_fields(self, request, obj=None):
        if request.user.groups.filter(name='Finance').exists():
            return ['user', 'cash_pending', 'mpesa_code', 'mpesa_pending', 'premium_status']
        return ['user', 'premium_status']

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Finance').exists():
            return self.readonly_fields
        return ['cash_pending', 'mpesa_code', 'mpesa_pending', 'premium_status']

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name='Finance').exists():
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if request.user.groups.filter(name='Finance').exists():
            return True
        return False

# --- Feedback admin ---
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'reply', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('text', 'reply', 'user__username')
    readonly_fields = ('user', 'text', 'created_at')
    fields = ('user', 'text', 'reply', 'created_at')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True  # optional: adjust as needed
