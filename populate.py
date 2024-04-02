import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pms.settings')

import django

django.setup()

from django.utils import timezone

from api.models import User, Role, Permission, Organization, PetitionType, RankType, Prefix, Priority, Category, \
    PetitionDetailType, PetitionDetailStatus

organizations = [
    {
        'id': 1, 'name': 'AG Branch', 'description': 'GHQ', 'parent': None, 'organization_type': 'Root',
        'is_delete': 'No',
        'insert_date': timezone.now(), 'insert_by': 'System', 'update_date': timezone.now(), 'update_by': 'System',
        'location': 'Rawalpindi', 'datacenter_id': 1, 'username_prefix': '', 'signal_center_id': 1, 'arm_type': 1,
        'ams_type': 1, 'online_status': 'Online', 'org_code': 1, 'org_status': 'System', 'city_code': 1,
    },
    {
        'id': 2, 'name': 'Medical', 'description': 'GHQ', 'parent': 'AG Branch', 'organization_type': 'Child',
        'is_delete': 'No',
        'insert_date': timezone.now(), 'insert_by': 'System', 'update_date': timezone.now(), 'update_by': 'System',
        'location': 'Rawalpindi', 'datacenter_id': 1, 'username_prefix': '', 'signal_center_id': 1, 'arm_type': 1,
        'ams_type': 1, 'online_status': 'Online', 'org_code': 1, 'org_status': 'System', 'city_code': 1,
    },
    {
        'id': 3, 'name': 'PA', 'description': 'GHQ', 'parent': 'AG Branch', 'organization_type': 'Child',
        'is_delete': 'No',
        'insert_date': timezone.now(), 'insert_by': 'System', 'update_date': timezone.now(), 'update_by': 'System',
        'location': 'Rawalpindi', 'datacenter_id': 1, 'username_prefix': '', 'signal_center_id': 1, 'arm_type': 1,
        'ams_type': 1, 'online_status': 'Online', 'org_code': 1, 'org_status': 'System', 'city_code': 1,
    },
    {
        'id': 4, 'name': 'PS', 'description': 'GHQ', 'parent': 'AG Branch', 'organization_type': 'Child',
        'is_delete': 'No',
        'insert_date': timezone.now(), 'insert_by': 'System', 'update_date': timezone.now(), 'update_by': 'System',
        'location': 'Rawalpindi', 'datacenter_id': 1, 'username_prefix': '', 'signal_center_id': 1, 'arm_type': 1,
        'ams_type': 1, 'online_status': 'Online', 'org_code': 1, 'org_status': 'System', 'city_code': 1,
    },
    {
        'id': 5, 'name': 'PA-S1', 'description': 'GHQ', 'parent': 'PA', 'organization_type': 'Child', 'is_delete': 'No',
        'insert_date': timezone.now(), 'insert_by': 'System', 'update_date': timezone.now(), 'update_by': 'System',
        'location': 'Rawalpindi', 'datacenter_id': 1, 'username_prefix': '', 'signal_center_id': 1, 'arm_type': 1,
        'ams_type': 1, 'online_status': 'Online', 'org_code': 1, 'org_status': 'System', 'city_code': 1,
    },
    {
        'id': 6, 'name': 'PS-S1', 'description': 'GHQ', 'parent': 'PS', 'organization_type': 'Child', 'is_delete': 'No',
        'insert_date': timezone.now(), 'insert_by': 'System', 'update_date': timezone.now(), 'update_by': 'System',
        'location': 'Rawalpindi', 'datacenter_id': 1, 'username_prefix': '', 'signal_center_id': 1, 'arm_type': 1,
        'ams_type': 1, 'online_status': 'Online', 'org_code': 1, 'org_status': 'System', 'city_code': 1,
    },
]

users = [
    {
        'id': 1, 'username': 'suleman', 'name': 'Suleman', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-324', 'is_delete': 'No', 'rank_name': 'Lt Col', 'service_name': 'Army', 'rank_order': 4,
        'rank_id': 13, 'appointment_id': 1, 'appointment_name': 'AAG-Sw', 'appointment_order': 1, 'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'Medical', 'role': 'nu'
    },
{
        'id': 15, 'username': 'suleman', 'name': 'Suleman', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-324', 'is_delete': 'No', 'rank_name': 'Lt Col', 'service_name': 'Army', 'rank_order': 4,
        'rank_id': 13, 'appointment_id': 1, 'appointment_name': 'AAG-Sw', 'appointment_order': 1, 'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'PA', 'role': 'nu'
    },
{
        'id': 16, 'username': 'suleman', 'name': 'Suleman', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-324', 'is_delete': 'No', 'rank_name': 'Lt Col', 'service_name': 'Army', 'rank_order': 4,
        'rank_id': 13, 'appointment_id': 1, 'appointment_name': 'AAG-Sw', 'appointment_order': 1, 'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'PS', 'role': 'nu'
    },


    {
        'id': 2, 'username': 'ahmed', 'name': 'Ahmed', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-323', 'is_delete': 'No', 'rank_name': 'Col', 'service_name': 'Army', 'rank_order': 5,
        'rank_id': 13, 'appointment_id': 1, 'appointment_name': 'AAG-Sw', 'appointment_order': 1, 'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'Medical', 'role': 'nu'
    },
    {
        'id': 3, 'username': 'usman', 'name': 'Usman', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-326', 'is_delete': 'No', 'rank_name': 'Lt Col', 'service_name': 'Army', 'rank_order': 4,
        'rank_id': 15, 'appointment_id': 1, 'appointment_name': 'AAG-Sw', 'appointment_order': 1,
        'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'PA', 'role': 'nu'
    },
    {
        'id': 4, 'username': 'ali', 'name': 'Ali', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-325', 'is_delete': 'No', 'rank_name': 'Col', 'service_name': 'Army', 'rank_order': 5,
        'rank_id': 14, 'appointment_id': 2, 'appointment_name': 'AAG-Tech', 'appointment_order': 1, 'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'PA', 'role': 'nu'
    },
    {
        'id': 5, 'username': 'khan', 'name': 'Khan', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-327', 'is_delete': 'No', 'rank_name': 'Lt Col', 'service_name': 'Army', 'rank_order': 4,
        'rank_id': 13, 'appointment_id': 1, 'appointment_name': 'AAG-Sw', 'appointment_order': 1,
        'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'PS', 'role': 'nu'
    },
    {
        'id': 6, 'username': 'gul', 'name': 'Gul', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-328', 'is_delete': 'No', 'rank_name': 'Col', 'service_name': 'Army', 'rank_order': 5,
        'rank_id': 14, 'appointment_id': 2, 'appointment_name': 'AAG-Tech', 'appointment_order': 1, 'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'PS', 'role': 'nu'
    },
    {
        'id': 7, 'username': 'akram', 'name': 'Akram', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-329', 'is_delete': 'No', 'rank_name': 'Lt Col', 'service_name': 'Army', 'rank_order': 4,
        'rank_id': 13, 'appointment_id': 1, 'appointment_name': 'AAG-Sw', 'appointment_order': 1,
        'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'AG Branch', 'role': 'nu'
    },
    {
        'id': 8, 'username': 'waqar', 'name': 'Waqar', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-330', 'is_delete': 'No', 'rank_name': 'Col', 'service_name': 'Army', 'rank_order': 5,
        'rank_id': 14, 'appointment_id': 2, 'appointment_name': 'AAG-Tech', 'appointment_order': 1, 'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'AG Branch', 'role': 'nu'
    },
    {
        'id': 9, 'username': 'ag', 'name': 'AG', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-330', 'is_delete': 'No', 'rank_name': 'Col', 'service_name': 'Army', 'rank_order': 5,
        'rank_id': 14, 'appointment_id': 3, 'appointment_name': 'AG', 'appointment_order': 1, 'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'AG Branch', 'role': 'ag'
    },
    {
        'id': 10, 'username': 'akmal', 'name': 'Akmal', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-340', 'is_delete': 'No', 'rank_name': 'Col', 'service_name': 'Army', 'rank_order': 5,
        'rank_id': 14, 'appointment_id': 1, 'appointment_name': 'AAG-Sw', 'appointment_order': 1, 'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'PA-S1', 'role': 'nu'
    },
    {
        'id': 11, 'username': 'umer', 'name': 'Umer', 'profile_status': 'Current', 'telephone': '0512305922',
        'svc_number': 'PA-350', 'is_delete': 'No', 'rank_name': 'Col', 'service_name': 'Army', 'rank_order': 5,
        'rank_id': 14, 'appointment_id': 2, 'appointment_name': 'AAG-Tech', 'appointment_order': 1, 'executive_order': 34,
        'appointment_type': 'Executive', 'organization': 'PS-S1', 'role': 'nu'
    },
]

roles = [
    {
        'name': 'AG',
        'code_name': 'ag',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_read', 'petition_update',
            'petition_close', 'petition_call',  'dashboard_show',  'petition_type_read', 'rank_type_read',
            'prefix_read', 'priority_read', 'category_read', 'petition_detail_type_read',
            'petition_detail_status_read', 'document_read', 'petition_link_read', 'petition_link_update',
            'petition_link_delete', 'organization_child_read', 'petition_delete', 'message_create', 'message_read',
            'message_update', 'message_delete', 'message_show','final_approval',
        ]
    },
    {
        'name': 'DD Petition',
        'code_name': 'dd_petition',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_close', 'petition_detail_update', 'petition_call', 'marked_petition_show',
            'all_petition_show', 'dashboard_show', 'daily_report_show', 'overall_report_show', 'suggestion_create',
            'petition_type_read', 'rank_type_read', 'prefix_read', 'priority_read', 'category_read',
            'petition_detail_type_read', 'petition_detail_status_read', 'document_create', 'document_read',
            'document_show', 'approve_can', 'approve_auto', 'petition_link_create', 'petition_link_read',
            'petition_link_update', 'petition_link_delete', 'petition_link_show', 'approve_link_can',
            'approve_link_auto', 'petition_can_search', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete', 'message_create', 'message_read',
            'message_update', 'message_delete', 'message_show'
        ]
    },
    {
        'name': 'DG',
        'code_name': 'dg',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show',
            'all_petition_show', 'dashboard_show', 'daily_report_show', 'overall_report_show', 'suggestion_create',
            'petition_type_read', 'rank_type_read', 'prefix_read', 'priority_read', 'category_read',
            'petition_detail_type_read', 'petition_detail_status_read', 'document_create', 'document_read',
            'document_show', 'approve_can', 'approve_auto', 'petition_link_create', 'petition_link_read',
            'petition_link_update', 'petition_link_delete', 'petition_link_show', 'approve_link_can',
            'approve_link_auto', 'petition_can_search', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete', 'message_create', 'message_read',
            'message_update', 'message_delete', 'message_show'
        ]
    },
    {
        'name': 'Dir',
        'code_name': 'dir',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'dashboard_show',
            'daily_report_show', 'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read',
            'priority_read', 'category_read', 'petition_detail_type_read', 'petition_detail_status_read',
            'document_create', 'document_read', 'document_show', 'approve_can', 'approve_auto', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'approve_link_can', 'approve_link_auto',
            'petition_can_search', 'suggestion_create', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete', 'message_create', 'message_read',
            'message_update', 'message_delete', 'message_show'
        ]
    },
    {
        'name': 'Col',
        'code_name': 'col',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'dashboard_show',
            'daily_report_show', 'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read',
            'priority_read', 'category_read', 'petition_detail_type_read', 'petition_detail_status_read',
            'document_create', 'document_read', 'document_show', 'approve_can', 'approve_auto', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'approve_link_can', 'approve_link_auto',
            'petition_can_search', 'suggestion_create', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete', 'message_create', 'message_read',
            'message_update', 'message_delete', 'message_show'
        ]
    },
    {
        'name': 'Lt. Col',
        'code_name': 'lt.Col',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'dashboard_show',
            'daily_report_show', 'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read',
            'priority_read', 'category_read', 'petition_detail_type_read', 'petition_detail_status_read',
            'document_create', 'document_read', 'document_show', 'approve_can', 'approve_auto', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'approve_link_can', 'approve_link_auto',
            'petition_can_search', 'suggestion_create', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete', 'message_create', 'message_read',
            'message_update', 'message_delete', 'message_show'
        ]
    },
    {
        'name': 'Major',
        'code_name': 'maj',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show',
            'daily_report_show', 'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read',
            'priority_read', 'category_read', 'petition_detail_type_read', 'petition_detail_status_read',
            'document_create', 'document_read', 'document_show', 'approve_can', 'approve_auto', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'approve_link_can', 'approve_link_auto',
            'petition_can_search', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete', 'message_create', 'message_read',
            'message_update', 'message_delete', 'message_show'
        ]
    },
    {
        'name': 'Captain',
        'code_name': 'cap',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'daily_report_show',
            'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read', 'priority_read',
            'category_read', 'petition_detail_type_read', 'petition_detail_status_read', 'document_create',
            'document_read', 'document_show', 'petition_link_create', 'petition_link_read',
            'petition_link_update', 'petition_link_show', 'petition_can_search', 'organization_child_create',
            'organization_child_read', 'organization_child_update', 'organization_child_show', 'petition_delete', 'message_create', 'message_read',
            'message_update', 'message_delete', 'message_show'
        ]
    },
    {
        'name': 'Clerk',
        'code_name': 'clk',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'daily_report_show',
            'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read', 'priority_read',
            'category_read', 'petition_detail_type_read', 'petition_detail_status_read', 'document_create',
            'document_read', 'document_show', 'petition_link_create', 'petition_link_read',
            'petition_link_update', 'petition_link_show', 'petition_can_search', 'organization_child_create',
            'organization_child_read', 'organization_child_update', 'organization_child_show', 'petition_delete', 'message_create', 'message_read',
            'message_update', 'message_delete', 'message_show'
        ]
    },
    {
        'name': 'NormalUser',
        'code_name': 'nu',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'marked_petition_show', 'petition_detail_update', 'petition_call', 'petition_type_read',
            'rank_type_read', 'prefix_read', 'priority_read', 'category_read', 'petition_detail_type_read',
            'petition_detail_status_read', 'document_create', 'document_read', 'document_show', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'petition_can_search',
            'organization_child_create', 'organization_child_read', 'organization_child_update',
            'organization_child_show', 'petition_delete', 'message_create', 'message_read',
            'message_update', 'message_delete', 'message_show'
        ]
    },
    {
        'name': 'PMC',
        'code_name': 'pmc',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'dashboard_show',
            'daily_report_show', 'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read',
            'priority_read', 'category_read', 'petition_detail_type_read', 'petition_detail_status_read',
            'document_create', 'document_read', 'document_show', 'approve_can', 'approve_auto', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'approve_link_can', 'approve_link_auto',
            'petition_can_search', 'suggestion_create', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete',
            'petition_update_sponsor_organization', 'message_create', 'message_read',
            'message_update', 'message_delete', 'message_show'
        ]
    },
]

petition_types = [
    {
        'name': 'Plot',
    }
]

petition_detail_types = [
    {
        'name': 'Army',
    },
    {
        'name': 'Civilian',
    },
    {
        'name': 'Anonymous',
    },
]

petition_detail_statuses = [
    {
        'name': 'Serving',
    },
    {
        'name': 'Retired',
    },
    {
        'name': 'War-Wounded',
    },
    {
        'name': 'Shuhda',
    },
]

rank_types = [
    {
        'name': 'Lt. General',
        'category': 1,
    },
    {
        'name': 'Col',
        'category': 2,
    },
    {
        'name': 'Major',
        'category': 3,
    },
    {
        'name': 'Soldier',
        'category': 4,
    }
]

prefixes = [
    {
        'name': 'PA',
    },
    {
        'name': 'PS',
    },
]

priorities = [
    {
        'name': 'Priority 1',
    },
    {
        'name': 'Priority 2',
    },
]

categories = [
    {
        'name': 'Cat 1',
        'description': 'Mk By COAS',
        'is_active': True,
    },
    {
        'name': 'Cat 2',
        'description': 'Mk By AG',
        'is_active': True,
    },
    {
        'name': 'Cat 3',
        'description': 'Normal',
        'is_active': True,
    },
    {
        'name': 'Cat 4',
        'description': 'Mk By Gen Offr',
        'is_active': True,
    },
    {
        'name': 'Cat 5',
        'description': 'Civs',
        'is_active': True,
    },
]


def populate():
    permissions = Permission.objects.all()

    try:
        role = Role.objects.get(code_name='su')
        role.permissions.clear()
    except Role.DoesNotExist:
        role = Role.objects.create(name='SuperUser', code_name='su')

    role.permissions.add(*permissions)
    role.save()

    for organization in organizations:
        try:
            Organization.objects.get(name=organization['name'])
        except Organization.DoesNotExist:
            parent = None
            if organization['parent']:
                parent = Organization.objects.get(name=organization['parent'])
            Organization.objects.create(
                id=organization['id'],
                name=organization['name'],
                description=organization['description'],
                parent=parent,
                organization_type=organization['organization_type'],
                is_delete=organization['is_delete'],
                insert_date=organization['insert_date'],
                insert_by=organization['insert_by'],
                update_date=organization['update_date'],
                update_by=organization['update_by'],
                location=organization['location'],
                datacenter_id=organization['datacenter_id'],
                username_prefix=organization['username_prefix'],
                signal_center_id=organization['signal_center_id'],
                arm_type=organization['arm_type'],
                ams_type=organization['ams_type'],
                online_status=organization['online_status'],
                org_code=organization['org_code'],
                org_status=organization['org_status'],
                city_code=organization['city_code'],
            )

    try:
        user = User.objects.get(username='superuser')
    except User.DoesNotExist:
        user = User.objects.create_superuser(
            id=999,
            username="superuser",
            password="123",
        )
        user.name = 'Superuser'
        user.role = Role.objects.get(code_name='su')
        user.organization = Organization.objects.get(name='AG Branch')
        user.save()

    for role in roles:
        try:
            Role.objects.get(code_name=role['code_name'])
        except Role.DoesNotExist:
            r = Role.objects.create(name=role['name'], code_name=role['code_name'], created_by=User.objects.get(username='superuser'), updated_by=User.objects.get(username='superuser'),)
            for permission in role['permissions']:
                r.permissions.add(Permission.objects.get(code_name=permission))
            r.save()

    for user in users:
        try:
            User.objects.get(id=user['id'])
        except User.DoesNotExist:
            User.objects.create(
                id=user['id'],
                username=user['username'],
                name=user['name'],
                profile_status=user['profile_status'],
                telephone=user['telephone'],
                svc_number=user['svc_number'],
                is_delete=user['is_delete'],
                rank_name=user['rank_name'],
                service_name=user['service_name'],
                rank_order=user['rank_order'],
                rank_id=user['rank_id'],
                appointment_id=user['appointment_id'],
                appointment_name=user['appointment_name'],
                appointment_order=user['appointment_order'],
                executive_order=user['executive_order'],
                appointment_type=user['appointment_type'],
                organization=Organization.objects.get(name=user['organization']),
                role=Role.objects.get(code_name=user['role']),
            )

    for petition_type in petition_types:
        try:
            PetitionType.objects.get(name=petition_type['name'])
        except PetitionType.DoesNotExist:
            PetitionType.objects.create(name=petition_type['name'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for petition_detail_type in petition_detail_types:
        try:
            PetitionDetailType.objects.get(name=petition_detail_type['name'])
        except PetitionDetailType.DoesNotExist:
            PetitionDetailType.objects.create(name=petition_detail_type['name'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for petition_detail_status in petition_detail_statuses:
        try:
            PetitionDetailStatus.objects.get(name=petition_detail_status['name'])
        except PetitionDetailStatus.DoesNotExist:
            PetitionDetailStatus.objects.create(name=petition_detail_status['name'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for rank_type in rank_types:
        try:
            RankType.objects.get(name=rank_type['name'])
        except RankType.DoesNotExist:
            RankType.objects.create(name=rank_type['name'], category=rank_type['category'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for prefix in prefixes:
        try:
            Prefix.objects.get(name=prefix['name'])
        except Prefix.DoesNotExist:
            Prefix.objects.create(name=prefix['name'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for priority in priorities:
        try:
            Priority.objects.get(name=priority['name'])
        except Priority.DoesNotExist:
            Priority.objects.create(name=priority['name'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for category in categories:
        try:
            Category.objects.get(name=category['name'])
        except Category.DoesNotExist:
            Category.objects.create(name=category['name'], description=category['description'], is_active=category['is_active'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))


if __name__ == '__main__':
    print("Starting PMS population script...")
    populate()
