import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pms.settings')

import django
django.setup()

from api.models import Permission

permissions = [
    Permission(name='Create Role', code_name='role_create', module_name='Role', description='User can create role'),
    Permission(name='Read Role', code_name='role_read', module_name='Role', description='User can read role'),
    Permission(name='Update Role', code_name='role_update', module_name='Role', description='User can update role'),
    Permission(name='Delete Role', code_name='role_delete', module_name='Role', description='User can delete role'),
    Permission(name='Show Role', code_name='role_show', module_name='Role', description='User can show user'),
    Permission(name='Read User', code_name='user_read', module_name='User', description='User can read user'),
    Permission(name='Update User', code_name='user_update', module_name='User', description='User can update user'),
    Permission(name='Show User', code_name='user_show', module_name='User', description='User can show user'),
    Permission(name='Read Organization', code_name='organization_read', module_name='Organization', description='User can read organization'),
    Permission(name='Show Organization', code_name='organization_show', module_name='Organization', description='User can show organization'),
    Permission(name='Update Organization', code_name='organization_update', module_name='Organization', description='User can update organization'),
    Permission(name='Create Petition', code_name='petition_create', module_name='Petition', description='User can create petition'),
    Permission(name='Read Petition', code_name='petition_read', module_name='Petition', description='User can read petition'),
    Permission(name='Update Petition', code_name='petition_update', module_name='Petition', description='User can update petition'),
    Permission(name='Delete Petition', code_name='petition_delete', module_name='Petition', description='User can delete petition'),
    Permission(name='NFA Petition', code_name='petition_nfa', module_name='Petition', description='User can delete petition'),
    Permission(name='Show Petition', code_name='petition_show', module_name='Petition', description='User can show petition'),
    Permission(name='Show Marked Petition', code_name='marked_petition_show', module_name='Petition', description='User can show marked petition'),
    Permission(name='Show Dashboard', code_name='dashboard_show', module_name='Dashboard', description='User can show dashboard'),
    Permission(name='Close Petition', code_name='petition_close', module_name='Petition', description='User can close petition'),
    Permission(name='Update Petition Detail', code_name='petition_detail_update', module_name='Petition Detail', description='User can update petition detail'),
    Permission(name='Call Petition', code_name='petition_call', module_name='Petition', description='User can call petition'),
    Permission(name='Show All Petition', code_name='all_petition_show', module_name='Petition', description='User can show all petition'),
    Permission(name='Show Daily Report', code_name='daily_report_show', module_name='Daily', description='User can show daily report'),
    Permission(name='Show Overall Report', code_name='overall_report_show', module_name='Overall', description='User can show overall report'),
    Permission(name='Create Suggestion', code_name='suggestion_create', module_name='Suggestion', description='User can create suggestion'),
    Permission(name='Read Suggestion', code_name='suggestion_read', module_name='Suggestion', description='User can read suggestion'),
    Permission(name='Update Suggestion', code_name='suggestion_update', module_name='Suggestion', description='User can update suggestion'),
    Permission(name='Delete Suggestion', code_name='suggestion_delete', module_name='Suggestion', description='User can delete suggestion'),
    Permission(name='Show Suggestion', code_name='suggestion_show', module_name='Suggestion', description='User can show suggestion'),
    Permission(name='Create Petition Type', code_name='petition_type_create', module_name='Petition Type', description='User can create petition type'),
    Permission(name='Read Petition Type', code_name='petition_type_read', module_name='Petition Type', description='User can read petition type'),
    Permission(name='Update Petition Type', code_name='petition_type_update', module_name='Petition Type', description='User can update petition type'),
    Permission(name='Delete Petition Type', code_name='petition_type_delete', module_name='Petition Type', description='User can delete petition type'),
    Permission(name='Show Petition Type', code_name='petition_type_show', module_name='Petition Type', description='User can show petition type'),
    Permission(name='Create Petition Detail Type', code_name='petition_detail_type_create', module_name='Petition Detail Type', description='User can create petition detail type'),
    Permission(name='Read Petition Detail Type', code_name='petition_detail_type_read', module_name='Petition Detail Type', description='User can read petition detail type'),
    Permission(name='Update Petition Detail Type', code_name='petition_detail_type_update', module_name='Petition Detail Type', description='User can update petition detail type'),
    Permission(name='Delete Petition Detail Type', code_name='petition_detail_type_delete', module_name='Petition Detail Type', description='User can delete petition type'),
    Permission(name='Show Petition Detail Type', code_name='petition_detail_type_show', module_name='Petition Detail Type', description='User can show petition detail type'),
    Permission(name='Create Petition Detail Status', code_name='petition_detail_status_create', module_name='Petition Detail Status', description='User can create petition detail status'),
    Permission(name='Read Petition Detail Status', code_name='petition_detail_status_read', module_name='Petition Detail Status', description='User can read petition detail status'),
    Permission(name='Update Petition Detail Status', code_name='petition_detail_status_update', module_name='Petition Detail Status', description='User can update petition detail status'),
    Permission(name='Delete Petition Detail Status', code_name='petition_detail_status_delete', module_name='Petition Detail Status', description='User can delete petition status'),
    Permission(name='Show Petition Detail Status', code_name='petition_detail_status_show', module_name='Petition Detail Status', description='User can show petition detail status'),
    Permission(name='Create Rank Type', code_name='rank_type_create', module_name='Rank Type', description='User can create rank type'),
    Permission(name='Read Rank Type', code_name='rank_type_read', module_name='Rank Type', description='User can read rank type'),
    Permission(name='Update Rank Type', code_name='rank_type_update', module_name='Rank Type', description='User can update rank type'),
    Permission(name='Delete Rank Type', code_name='rank_type_delete', module_name='Rank Type', description='User can delete rank type'),
    Permission(name='Show Rank Type', code_name='rank_type_show', module_name='Rank Type', description='User can show rank type'),
    Permission(name='Create Prefix', code_name='prefix_create', module_name='Prefix', description='User can create prefix'),
    Permission(name='Read Prefix', code_name='prefix_read', module_name='Prefix', description='User can read prefix'),
    Permission(name='Update Prefix', code_name='prefix_update', module_name='Prefix', description='User can update prefix'),
    Permission(name='Delete Prefix', code_name='prefix_delete', module_name='Prefix', description='User can delete prefix'),
    Permission(name='Show Prefix', code_name='prefix_show', module_name='Prefix', description='User can show prefix'),
    Permission(name='Create Priority', code_name='priority_create', module_name='Priority', description='User can create priority'),
    Permission(name='Read Priority', code_name='priority_read', module_name='Priority', description='User can read priority'),
    Permission(name='Update Priority', code_name='priority_update', module_name='Priority', description='User can update priority'),
    Permission(name='Delete Priority', code_name='priority_delete', module_name='Priority', description='User can delete priority'),
    Permission(name='Show Priority', code_name='priority_show', module_name='Priority', description='User can show priority'),
    Permission(name='Create Category', code_name='category_create', module_name='Category', description='User can create category'),
    Permission(name='Read Category', code_name='category_read', module_name='Category', description='User can read category'),
    Permission(name='Update Category', code_name='category_update', module_name='Category', description='User can update category'),
    Permission(name='Delete Category', code_name='category_delete', module_name='Category', description='User can delete category'),
    Permission(name='Show Category', code_name='category_show', module_name='Category', description='User can show category'),

    Permission(name='Create Document', code_name='document_create', module_name='Document', description='User can create document'),
    Permission(name='Read Document', code_name='document_read', module_name='Document', description='User can read document'),
    Permission(name='Update Document', code_name='document_update', module_name='Document', description='User can update document'),
    Permission(name='Delete Document', code_name='document_delete', module_name='Document', description='User can delete document'),
    Permission(name='Show Document', code_name='document_show', module_name='Document', description='User can show document'),

    Permission(name='Can Approve', code_name='approve_can', module_name='Approve', description='User can approve petitions'),
    Permission(name='Auto Approve', code_name='approve_auto', module_name='Approve', description='User can auto approve petitions'),

    Permission(name='Create Petition Link', code_name='petition_link_create', module_name='Petition Link', description='User can create petition link'),
    Permission(name='Read Petition Link', code_name='petition_link_read', module_name='Petition Link', description='User can read petition link'),
    Permission(name='Update Petition Link', code_name='petition_link_update', module_name='Petition Link', description='User can update petition link'),
    Permission(name='Delete Petition Link', code_name='petition_link_delete', module_name='Petition Link', description='User can delete petition link'),
    Permission(name='Show Petition Link', code_name='petition_link_show', module_name='Petition Link', description='User can show petition link'),

    Permission(name='Can Approve Link', code_name='approve_link_can', module_name='Approve Link', description='User can approve link petitions'),
    Permission(name='Auto Approve Link', code_name='approve_link_auto', module_name='Approve Link', description='User can auto approve link petitions'),

    Permission(name='Can Petition Search', code_name='petition_can_search', module_name='Petition', description='User can search petitions'),

    Permission(name='Petition Summary', code_name='petition_summary', module_name='Petition', description='User can see petition summary'),

    Permission(name='Create Organization Child', code_name='organization_child_create', module_name='Organization Child', description='User can create organization child'),
    Permission(name='Read Organization Child', code_name='organization_child_read', module_name='Organization Child', description='User can read organization child'),
    Permission(name='Update Organization Child', code_name='organization_child_update', module_name='Organization Child', description='User can update organization child'),
    Permission(name='Delete Organization Child', code_name='organization_child_delete', module_name='Organization Child', description='User can delete organization child'),
    Permission(name='Show Organization Child', code_name='organization_child_show', module_name='Organization Child', description='User can show organization child'),

    Permission(name='Final Approval', code_name='final_approval', module_name='Final Approval', description='User can give final approval'),

    Permission(name='AG Approved Petition', code_name='petition_ag_approved', module_name='Petition', description='User can see ag approved petitions'),
    Permission(name='AG Rejected Petition', code_name='petition_ag_rejected', module_name='Petition', description='User can see ag rejected petitions'),

    Permission(name='Petition Update Sponsor Organization', code_name='petition_update_sponsor_organization', module_name='Petition', description='User can update petition sponsor organization'),

    Permission(name='Closed Petition', code_name='petition_closed', module_name='Petition', description='User can see closed petitions'),

    Permission(name='Create Message', code_name='message_create', module_name='Message', description='User can create message'),
    Permission(name='Read Message', code_name='message_read', module_name='Message', description='User can read message'),
    Permission(name='Update Message', code_name='message_update', module_name='Message', description='User can update message'),
    Permission(name='Delete Message', code_name='message_delete', module_name='Message', description='User can delete message'),
    Permission(name='Show Message', code_name='message_show', module_name='Message', description='User can show message'),

    Permission(name='Create Favorite User', code_name='favorite_user_create', module_name='Favorite User', description='User can create favorite user'),
    Permission(name='Read Favorite User', code_name='favorite_user_read', module_name='Favorite User', description='User can read favorite user'),
    Permission(name='Update Favorite User', code_name='favorite_user_update', module_name='Favorite User', description='User can update favorite user'),
    Permission(name='Delete Favorite User', code_name='favorite_user_delete', module_name='Favorite User', description='User can delete favorite user'),
    Permission(name='Show Favorite User', code_name='favorite_user_show', module_name='Favorite User', description='User can show favorite user'),
]


def add_permission():
    for permission in permissions:
        try:
            Permission.objects.get(code_name=permission.code_name)
        except Permission.DoesNotExist:
            permission.save()


if __name__ == '__main__':
    print("Adding permissions to PMS...")
    add_permission()
