class Users:
    USER_A = "user_a"
    USER_B = "user_b"
    USER_C = "user_c"
    USER_D = "user_d"
    USER_E = "user_e"


class Groups:
    GROUP_A = "group_a"
    GROUP_B = "group_b"
    GROUP_C = "group_c"


class SplitMode:
    EQUALLY = "equally"
    AMOUNT = "amount"
    PERCENTAGE = "percentage"

    SPLIT_MODE_CHOICES = {
        EQUALLY: "equally",
        AMOUNT: "amount",
        PERCENTAGE: "percentage"
    }


class ExpenseStatus:
    PAID = "paid"
    OWE = "owe"

    EXPENSE_STATUS_CHOICE = {
        PAID: "paid",
        OWE: "owe"
    }


class ActivityType:
    ADD_EXPENSE = "add_expense"
    SETTLE_UP = "settle_up"

    ACTIVITY_TYPE_CHOICE = {
        ADD_EXPENSE: "add_expense",
        SETTLE_UP: "settle_up"
    }
