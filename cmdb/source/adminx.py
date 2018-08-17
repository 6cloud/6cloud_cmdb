import xadmin

from source.models import Business, Application, SystemUser, Colony, IDC, Cabinet, Host


class BusinessAdmin:
    list_display = ('name', 'leader', 'desc', 'create_time', 'update_time')
    search_fields = ('name', 'leader', 'desc', 'create_time', 'update_time')
    list_filter = ('name', 'leader', 'desc', 'create_time', 'update_time')


class ApplicationAdmin:
    list_display = ('name', 'business', 'ops', 'dev', 'qa', 'cs', 'desc', 'create_time', 'update_time')
    search_fields = ('name', 'business', 'ops', 'dev', 'qa', 'cs',  'desc', 'create_time', 'update_time')
    list_filter = ('name', 'business', 'ops', 'dev', 'qa', 'cs', 'desc', 'create_time', 'update_time')


class SystemUserAdmin:
    list_display = ('name', 'username', 'password', 'private_key', 'public_key', 'create_time', 'update_time')
    search_fields = ('name', 'username', 'password', 'private_key', 'public_key', 'create_time', 'update_time')
    list_filter = ('name', 'username', 'password', 'private_key', 'public_key', 'create_time', 'update_time')


class ColonyAdmin:
    list_display = ('name', 'application', 'desc', 'create_time', 'update_time')
    search_fields = ('name', 'application', 'desc', 'create_time', 'update_time')
    list_filter = ('name', 'application', 'desc', 'create_time', 'update_time')


class IDCAdmin:
    list_display = ('name', 'address', 'phone', 'manage_user', 'desc', 'create_time', 'update_time')
    search_fields = ('name', 'address', 'phone', 'manage_user', 'desc', 'create_time', 'update_time')
    list_filter = ('name', 'address', 'phone', 'manage_user', 'desc', 'create_time', 'update_time')


class CabinetAdmin:
    list_display = ('idc', 'address', 'unum', 'hosts', 'desc', 'create_time', 'update_time')
    search_fields = ('idc', 'address', 'unum', 'hosts', 'desc', 'create_time', 'update_time')
    list_filter = ('idc', 'address', 'unum', 'hosts', 'desc', 'create_time', 'update_time')


class HostAdmin:
    list_display = ('hostname', 'intranet_ipaddress', 'macaddress', 'sn', 'os_type', 'colony', 'desc', 'create_time')
    search_fields = ('hostname', 'intranet_ipaddress', 'macaddress', 'sn', 'os_type', 'colony',  'desc', 'create_time')
    list_filter = ('hostname', 'intranet_ipaddress', 'macaddress', 'sn', 'os_type', 'colony',  'desc', 'create_time')


xadmin.site.register(Business, BusinessAdmin)
xadmin.site.register(Application, ApplicationAdmin)
xadmin.site.register(SystemUser, SystemUserAdmin)
xadmin.site.register(Colony, ColonyAdmin)
xadmin.site.register(IDC, IDCAdmin)
xadmin.site.register(Cabinet, CabinetAdmin)
xadmin.site.register(Host, HostAdmin)
