from dataclasses import dataclass, field

from core.models.product_periodicity_model import Product_Periodicity
from core.models.product_dimensions_model import Product_Dimensions

@dataclass
class Product_Description:

    id: int = field(init=False)
    name: str
    category: str
    subcategory: str
    ean: int
    internal_code: int
    product_periodicity: Product_Periodicity = field(init=False)
    product_dimensions: Product_Dimensions = field(init=False)

    # TODO add category and subcategory list