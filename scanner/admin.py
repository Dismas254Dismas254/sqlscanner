from django.contrib import admin
from .models import Profile,Feedback

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # List display without payment fields for non-finance staff
    list_display = ('user', 'premium_status')  # Remove payment-related fields for general admins
    list_editable = ('premium_status',)
    search_fields = ('user__username',)
    
    # Only finance staff should be able to edit these fields
    readonly_fields = ('mpesa_code',)

    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Payment Details', {
            'fields': ('cash_pending', 'mpesa_code', 'mpesa_pending', 'premium_status'),
            'classes': ('collapse',),  # Hide these fields by default
        }),
    )

    # Restrict access based on user group
    def get_fields(self, request, obj=None):
        # Finance staff can see and edit payment fields, admins cannot
        if request.user.groups.filter(name='Finance').exists():
            return ['user', 'cash_pending', 'mpesa_code', 'mpesa_pending', 'premium_status']
        # Admins only see user-related fields (no payment-related fields)
        return ['user', 'premium_status']

    def get_readonly_fields(self, request, obj=None):
        # Allow finance staff to edit payment fields, make them readonly for others
        if request.user.groups.filter(name='Finance').exists():
            return self.readonly_fields
        return ['cash_pending', 'mpesa_code', 'mpesa_pending', 'premium_status']

    def has_change_permission(self, request, obj=None):
        # Only finance users can change payment fields
        if request.user.groups.filter(name='Finance').exists():
            return True
        # Admins do not have permission to edit payment-related fields
        return False

    def has_view_permission(self, request, obj=None):
        # Only finance users can view payment-related fields
        if request.user.groups.filter(name='Finance').exists():
            return True
        # Admins don't have permission to view payment-related fields
        return False


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'reply', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('text', 'reply', 'user__username')
    readonly_fields = ('user', 'text', 'created_at')  # prevent editing original feedback
    fields = ('user', 'text', 'reply', 'created_at')  # order of fields in form

    def has_add_permission(self, request):
        return False  # disable adding feedback manually from admin

    def has_change_permission(self, request, obj=None):
        return True  # allow changing (replying to) feedback

    def has_delete_permission(self, request, obj=None):
        return True  # optional: allow deleting feedback
