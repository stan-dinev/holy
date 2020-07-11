from enum import Enum


class UserStatus(Enum):
    A = 'Admin'
    O = 'Operator'
    C = 'Consumer'


class ProductStatus(Enum):
    G = 'Gaming'
    B = 'Business'
    S = 'Student'


class PurchaseStatus(Enum):
    D = 'Delivered'
    I = 'In progress'
    P = 'Pending'
