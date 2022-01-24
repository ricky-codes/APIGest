from dataclasses import dataclass, field

from . import product_periodicity_model
from . import product_dimensions_model

@dataclass
class Product_Description:

    id: int = field(init=False)
    name: str
    category: str
    subcategory: str
    ean: int
    internal_code: int
    product_periodicity: product_periodicity_model.Product_Periodicity = field(init=False)
    product_dimensions: product_dimensions_model.Product_Dimensions = field(init=False)

    # TODO add category and subcategory list