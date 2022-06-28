from .constants import (
    ACCOUNT_MANAGER_ROLE,
    CUSTOM_ROLE,
    STAFF_ROLE,
    CLINIC_SUPER_ROLE,
    CLINIC_ROLE,
    LABORATORY_ROLE,

)
from .group_names import (
    ACCOUNT_MANAGER,
    ADMINISTRATION,
    EVERYONE,
    CLINIC_SUPER,
    CLINIC,
    LABORATORY,
)

role_names = {
    ACCOUNT_MANAGER_ROLE: "Account Manager",
    CLINIC_SUPER_ROLE: "Clinic Super",
    CLINIC_ROLE: "Clinic",
    CUSTOM_ROLE: "Custom ...",
    STAFF_ROLE: "Staff",
    LABORATORY_ROLE: "Laboratory"
}

required_role_names = {STAFF_ROLE: "Staff"}

groups_by_role_name = {
    ACCOUNT_MANAGER_ROLE: [ACCOUNT_MANAGER, ADMINISTRATION, EVERYONE],
    CLINIC_SUPER_ROLE: [CLINIC, CLINIC_SUPER, EVERYONE],
    CLINIC_ROLE: [CLINIC, EVERYONE],
    STAFF_ROLE: [EVERYONE],
    LABORATORY_ROLE: [LABORATORY, EVERYONE],
    CUSTOM_ROLE: [],
}
