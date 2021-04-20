from .constants import (
    ACCOUNT_MANAGER_ROLE,
    CUSTOM_ROLE,
    STAFF_ROLE,

)
from .group_names import (
    ACCOUNT_MANAGER,
    ADMINISTRATION,
    EVERYONE,
)

role_names = {
    ACCOUNT_MANAGER_ROLE: "Account Manager",
    CUSTOM_ROLE: "Custom ...",
    STAFF_ROLE: "Staff",
}

required_role_names = {STAFF_ROLE: "Staff"}

groups_by_role_name = {
    ACCOUNT_MANAGER_ROLE: [ACCOUNT_MANAGER, ADMINISTRATION, EVERYONE],
    STAFF_ROLE: [ADMINISTRATION, EVERYONE],
    CUSTOM_ROLE: [],
}
