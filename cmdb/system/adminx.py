import xadmin

from system.models import User, Role


class RoleAdmin:
    list_display = ['id', 'name', 'permission', 'create_time', 'update_time']
    search_fields = ('id', 'name', 'permission', 'create_time', 'update_time')
    list_filter = ('id', 'name', 'permission', 'create_time', 'update_time')
    style_fields = {'permission': 'm2m_transfer'}


class UserAdmin:
    list_display = ['id', 'username', 'email', 'role', 'is_active', 'is_superuser', 'user_permissions']
    search_fields = ('id', 'username', 'email', 'role', 'is_active', 'is_superuser', 'user_permissions')
    list_filter = ('id', 'username', 'email', 'role', 'is_active', 'is_superuser', 'user_permissions')
    style_fields = {'role': 'm2m_transfer', 'user_permissions': 'm2m_transfer'}


xadmin.site.unregister(User)
xadmin.site.register(Role, RoleAdmin)
xadmin.site.register(User, UserAdmin)
